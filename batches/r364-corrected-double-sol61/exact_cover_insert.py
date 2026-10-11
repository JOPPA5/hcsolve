from pathlib import Path
import sys,time,json,random,argparse
sys.path.insert(0,'/private/tmp/hcsolve-z3')
import z3
from collections import Counter

def enc(p,k):return ''.join(p[i::len(k)] for i in k)
def solve(p,c,widths,timeout=20000,errors=0,alignments=None,known_keys=None,backend="generic",blocked_keys=None,anchors=False,explicit_vocab=False,insert_x_template=None,cipher_variants=None):
 N=len(p);assert len(c)==N and all(1<w<32 for w in widths)
 if backend=='eager':s=z3.Then('simplify','card2bv','bit-blast','sat').solver()
 elif backend=='eager_chb':s=z3.Then('simplify','card2bv','bit-blast',z3.With('sat',**{'branching.heuristic':'chb'})).solver()
 elif backend=='native':s=z3.Then('simplify','bit-blast','sat').solver()
 else:s=z3.Solver()
 s.set(timeout=timeout,random_seed=610365)
 stages=[[z3.BitVec('unknown_'+str(i),5) if ch=='?' else z3.BitVecVal(ord(ch)-97,5) for i,ch in enumerate(p)]]
 for cell,ch in zip(stages[0],p):
  if ch=='?':s.add(z3.ULE(cell,25))
 if insert_x_template is not None:
  assert p=='?'*N and len(insert_x_template)==N-1
  insertion=z3.BitVec('fifth_x_position',max(1,N.bit_length()));s.add(z3.ULE(insertion,N-1))
  for i,cell in enumerate(stages[0]):
   left=z3.BitVecVal(ord(insert_x_template[max(0,i-1)])-97,5)
   right=z3.BitVecVal(ord(insert_x_template[min(i,N-2)])-97,5)
   s.add(cell==z3.If(insertion==i,z3.BitVecVal(23,5),z3.If(z3.ULT(insertion,i),left,right)))
 for j in range(len(widths)-1):stages.append([z3.BitVec(f'a_{j}_{i}',5) for i in range(N)])
 if cipher_variants is not None:
  assert not errors and c in cipher_variants and all(len(v)==N for v in cipher_variants)
  stages.append([z3.BitVec('output_'+str(i),5) if len({v[i]for v in cipher_variants})>1 else z3.BitVecVal(ord(ch)-97,5) for i,ch in enumerate(c)])
  differing=[i for i in range(N)if len({v[i]for v in cipher_variants})>1]
  s.add(z3.Or([z3.And([stages[-1][i]==ord(v[i])-97 for i in differing])for v in cipher_variants]))
 else:stages.append([z3.BitVec('output_'+str(i),5) if errors else z3.BitVecVal(ord(ch)-97,5) for i,ch in enumerate(c)])
 choices=[]
 if errors:s.add(z3.PbLe([(cell!=ord(ch)-97,1) for cell,ch in zip(stages[-1],c)],errors))
 # Preserved inventory bounds remain valid for an unspecified filler.
 count=Counter(p.replace('?',''));unknown=p.count('?')
 if insert_x_template is not None:count=Counter(insert_x_template)+Counter({'x':1});unknown=0
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
  q,r=divmod(N,w);occupy=[[] for _ in range(N)];cols=[]
  # Feasible starts of chunks of lengths q or q+1 after preceding columns.
  starts=set()
  for before in range(w):
   for long in range(max(0,before-(w-r)),min(before,r)+1):starts.add(q*before+long)
  for col in range(w):
   L=q+(col<r);opts=[]
   for at in sorted(starts):
    if at+L>N:continue
    if col==0 and alignments:
     before=alignments[j]-1;long_other=r-(r>0);short_other=w-r-(r==0)
     allowed={q*before+x for x in range(max(0,before-short_other),min(before,long_other)+1)}
     if at not in allowed:continue
    b=z3.Bool(f'b_{j}_{col}_{at}');opts.append((at,b))
    for row in range(L):
     occupy[at+row].append(b);s.add(z3.Implies(b,stages[j+1][at+row]==stages[j][row*w+col]))
   s.add(z3.PbEq([(b,1) for _,b in opts],1));cols.append(opts)
  if known_keys:
   key=known_keys[j];at=0;known_starts={}
   for col in key:known_starts[col]=at;at+=q+(col<r)
   for col,opts in enumerate(cols):
    for start,b in opts:s.add(b==(start==known_starts[col]))
  if alignments:
   ranks=[z3.BitVec(f'rank_{j}_{at}',5) for at in range(N+1)]
   s.add(ranks[0]==0,ranks[N]==w)
   for rank in ranks:s.add(z3.ULE(rank,w))
   for col,opts in enumerate(cols):
    L=q+(col<r)
    for at,chosen in opts:s.add(z3.Implies(chosen,ranks[at+L]==ranks[at]+1))
   for at,chosen in cols[0]:s.add(z3.Implies(chosen,ranks[at]==alignments[j]-1))
  for opts in occupy:s.add(z3.PbEq([(b,1) for b in opts],1))
  choices.append(cols)
 if blocked_keys:
  for banned in blocked_keys:
   equal_terms=[]
   for j,key in enumerate(banned):
    q,r=divmod(N,widths[j]);at=0;starts={}
    for col in key:starts[col]=at;at+=q+(col<r)
    for col,opts in enumerate(choices[j]):
     equal_terms.extend(b for start,b in opts if start==starts[col])
   s.add(z3.Not(z3.And(equal_terms)))
 t=time.monotonic();res=s.check();out={'status':str(res),'seconds':time.monotonic()-t,'widths':widths,'timeout_ms':timeout,'backend':backend}
 if res==z3.sat:
  m=s.model();ks=[]
  for cols in choices:
   starts=[(at,col) for col,opts in enumerate(cols) for at,b in opts if z3.is_true(m.eval(b))];ks.append([col for at,col in sorted(starts)])
  conditional=''.join(chr(m.eval(cell).as_long()+97) for cell in stages[0]);predicted=conditional
  for k in ks:predicted=enc(predicted,k)
  selected_cipher=c
  if cipher_variants is not None:
   selected_cipher=''.join(chr(m.eval(cell).as_long()+97)for cell in stages[-1]);assert selected_cipher in cipher_variants
  mismatches=[i for i,(a,b) in enumerate(zip(predicted,selected_cipher)) if a!=b];assert len(mismatches)<=errors
  if insert_x_template is not None:out['fifth_x_position']=m.eval(insertion).as_long();assert conditional==insert_x_template[:out['fifth_x_position']]+'x'+insert_x_template[out['fifth_x_position']:]
  if cipher_variants is not None:out.update(selected_ciphertext_variant=selected_cipher,selected_variant_index=cipher_variants.index(selected_cipher))
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
