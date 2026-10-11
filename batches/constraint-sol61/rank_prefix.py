from pathlib import Path
import sys,time,json,random,argparse
sys.path.insert(0,'/private/tmp/hcsolve-z3')
import z3
from collections import Counter

def enc(p,k):return ''.join(p[i::len(k)] for i in k)
def solve(p,c,widths,timeout=20000,errors=0,alignments=None,known_keys=None,backend="generic",blocked_keys=None,anchors=False,explicit_vocab=False):
 N=len(p);assert len(c)==N and all(1<w<32 for w in widths)
 if backend=='eager':s=z3.Then('simplify','card2bv','bit-blast','sat').solver()
 elif backend=='native':s=z3.Then('simplify','bit-blast','sat').solver()
 else:s=z3.Solver()
 s.set(timeout=timeout,random_seed=610365)
 stages=[[z3.BitVec('unknown_'+str(i),5) if ch=='?' else z3.BitVecVal(ord(ch)-97,5) for i,ch in enumerate(p)]]
 for cell,ch in zip(stages[0],p):
  if ch=='?':s.add(z3.ULE(cell,25))
 for j in range(len(widths)-1):stages.append([z3.BitVec(f'a_{j}_{i}',5) for i in range(N)])
 stages.append([z3.BitVec('output_'+str(i),5) if errors else z3.BitVecVal(ord(ch)-97,5) for i,ch in enumerate(c)]);choices=[]
 if errors:s.add(z3.PbLe([(cell!=ord(ch)-97,1) for cell,ch in zip(stages[-1],c)],errors))
 # Preserved inventory bounds remain valid for an unspecified filler.
 count=Counter(p.replace('?',''));unknown=p.count('?')
 deficit=count-Counter(c);excess=Counter(c)-count
 if unknown==1 and sum(deficit.values())==errors:
  # Error budget is saturated by letter deficits: filler must consume excess,
  # and every changed ciphertext position must change excess -> deficit.
  for cell,ch in zip(stages[0],p):
   if ch=='?':s.add(z3.Or([cell==ord(x)-97 for x in excess]))
  if errors:
   for cell,ch in zip(stages[-1],c):
    if ch not in excess:s.add(cell==ord(ch)-97)
    else:s.add(z3.Or([cell==ord(ch)-97]+[cell==ord(x)-97 for x in deficit]))
 for cells in stages[1:-1]:
  for ch in 'abcdefghijklmnopqrstuvwxyz':
   terms=[(cell==ord(ch)-97,1) for cell in cells]
   s.add(z3.PbGe(terms,count[ch]),z3.PbLe(terms,count[ch]+unknown))
  for cell in cells:s.add(z3.ULE(cell,25))
 if anchors:
  filler=set(excess) if unknown==1 and sum(deficit.values())==errors else set('abcdefghijklmnopqrstuvwxyz') if unknown else set()
  unique=[ch for ch,amt in count.items() if amt==1 and ch not in filler]
  bits=max(1,N.bit_length())
  for ch in unique:
   for stage,cells in enumerate(stages):
    pos=z3.BitVec(f'position_{stage}_{ch}',bits);s.add(z3.ULT(pos,N))
    for i,cell in enumerate(cells):s.add((cell==ord(ch)-97)==(pos==i))
 if explicit_vocab:
  filler=set(excess) if unknown==1 and sum(deficit.values())==errors else set('abcdefghijklmnopqrstuvwxyz') if unknown else set()
  vocabulary=set(count)|filler
  for cells in stages[1:]:
   for cell in cells:s.add(z3.Or([cell==ord(ch)-97 for ch in vocabulary]))
 for j,w in enumerate(widths):
  q,r=divmod(N,w)
  if r<=w-r:base=q;sign=1;special=set(range(r))
  else:base=q+1;sign=-1;special=set(range(r,w))
  m=len(special);bits=max(1,(m+1).bit_length())
  A=[[z3.Bool(f'a_{j}_{col}_{rank}') for rank in range(w)] for col in range(w)]
  for col in range(w):s.add(z3.PbEq([(b,1) for b in A[col]],1))
  for rank in range(w):s.add(z3.PbEq([(A[col][rank],1) for col in range(w)],1))
  pref=[z3.BitVec(f'prefix_{j}_{rank}',bits) for rank in range(w+1)]
  s.add(pref[0]==0,pref[w]==m)
  for rank in range(w+1):
   s.add(z3.UGE(pref[rank],max(0,rank-(w-m))),z3.ULE(pref[rank],min(rank,m)))
  for rank in range(w):
   selected_special=z3.Or([A[col][rank] for col in special])
   s.add(pref[rank+1]==pref[rank]+z3.If(selected_special,z3.BitVecVal(1,bits),z3.BitVecVal(0,bits)))
  for col in range(w):
   L=q+(col<r);is_special=col in special
   for rank in range(w):
    low=max(0,rank-(w-m-(not is_special)));high=min(rank,m-is_special)
    s.add(z3.Implies(A[col][rank],z3.Or([pref[rank]==x for x in range(low,high+1)])))
    for count_before in range(low,high+1):
     at=base*rank+sign*count_before
     if not 0<=at<=N-L:
      s.add(z3.Not(z3.And(A[col][rank],pref[rank]==count_before)));continue
     for row in range(L):s.add(z3.Implies(z3.And(A[col][rank],pref[rank]==count_before),stages[j+1][at+row]==stages[j][row*w+col]))
  if alignments:s.add(A[0][alignments[j]-1])
  if known_keys:
   for rank,col in enumerate(known_keys[j]):s.add(A[col][rank])
  choices.append([list(enumerate(A[col])) for col in range(w)])
 if blocked_keys:
  for banned in blocked_keys:
   equal_terms=[]
   for j,key in enumerate(banned):
    starts={col:rank for rank,col in enumerate(key)}
    for col,opts in enumerate(choices[j]):
     equal_terms.extend(b for start,b in opts if start==starts[col])
   s.add(z3.Not(z3.And(equal_terms)))
 t=time.monotonic();res=s.check();out={'status':str(res),'seconds':time.monotonic()-t,'widths':widths,'timeout_ms':timeout,'backend':backend,'encoding':'rank_prefix'}
 if res==z3.sat:
  m=s.model();ks=[]
  for cols in choices:
   starts=[(at,col) for col,opts in enumerate(cols) for at,b in opts if z3.is_true(m.eval(b))];ks.append([col for at,col in sorted(starts)])
  conditional=''.join(chr(m.eval(cell).as_long()+97) for cell in stages[0]);predicted=conditional
  for k in ks:predicted=enc(predicted,k)
  mismatches=[i for i,(a,b) in enumerate(zip(predicted,c)) if a!=b];assert len(mismatches)<=errors
  out.update(keys=ks,re_encryption_exact=not mismatches,conditional_plaintext=conditional,predicted_ciphertext=predicted,mismatch_positions=mismatches,error_bound=errors)
  inverse=predicted
  for k in ks[::-1]:
   cells=['']*len(inverse);at=0
   for col in k:
    for pos in range(col,len(cells),len(k)):cells[pos]=inverse[at];at+=1
   inverse=''.join(cells)
  assert inverse==conditional;out['independent_inverse_exact']=True
 else:out['reason']=s.reason_unknown() if res==z3.unknown else 'proved unsatisfiable in this fixed model'
 return out
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--widths',default='16,17,18');ap.add_argument('--timeout',type=int,default=20000);args=ap.parse_args();ws=list(map(int,args.widths.split(',')));p='kontrolnytextjeuplnenezavislyodhistorickehozadaniapoznameceleslovaabc'[:65];assert len(p)==65
 rng=random.Random(610365891);true=[];c=p
 for w in ws:
  k=rng.sample(range(w),w);true.append(k);c=enc(c,k)
 result=solve(p,c,ws,args.timeout);result.update(plaintext=p,ciphertext=c,planted_keys=true,mode='independent_synthetic_known_plaintext_control')
 path=Path(__file__).parent/f'cover-cardinality-{args.widths.replace(",","-")}.json';path.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
