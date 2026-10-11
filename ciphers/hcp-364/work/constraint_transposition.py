"""Exact constraint model of cascaded irregular columnar transpositions.
Known source quote is conditional, never labeled a recovered plaintext.
Requires z3-solver (PyPI), staged in /private/tmp/hcsolve-z3 in this run.
"""
import sys,json,random,time,argparse
from pathlib import Path
sys.path.insert(0,'/private/tmp/hcsolve-z3')
import z3
P=Path(__file__).parent
quote='nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcislox'
assert len(quote)==64

def enc(p,k):return ''.join(p[i::len(k)] for i in k)
def dec(c,k):
 out=['']*len(c);pos=0
 for i in k:
  inds=list(range(i,len(c),len(k)))
  for j in inds:out[j]=c[pos];pos+=1
 return ''.join(out)
def solve(p,c,widths,errors,timeout,seed):
 n=len(c);s=z3.SolverFor("QF_ABV");s.set(timeout=timeout,random_seed=seed)
 idx=z3.BitVecSort(7);char=z3.BitVecSort(5)
 arrays=[z3.Array('a'+str(j),idx,char) for j in range(len(widths)+1)]
 for i,t in enumerate(p):
  if t=='?':s.add(z3.ULE(z3.Select(arrays[0],i),25))
  else:s.add(z3.Select(arrays[0],i)==ord(t)-97)
 allkeys=[]
 for stage,w in enumerate(widths):
  q,r=divmod(n,w)
  keys=[z3.BitVec('k%d_%d'%(stage,i),5) for i in range(w)]
  s.add(z3.Distinct(keys))
  for k in keys:s.add(z3.ULT(k,w))
  allkeys.append(keys);off=z3.BitVecVal(0,7)
  for k in keys:
   kk=z3.ZeroExt(2,k)
   for row in range(q):
    s.add(z3.Select(arrays[stage+1],off+row)==z3.Select(arrays[stage],row*w+kk))
   if r:
    s.add(z3.Implies(z3.ULT(k,r),z3.Select(arrays[stage+1],off+q)==z3.Select(arrays[stage],q*w+kk)))
    off=off+q+z3.If(z3.ULT(k,r),z3.BitVecVal(1,7),z3.BitVecVal(0,7))
   else:off=off+q
 mism=[z3.Select(arrays[-1],i)!=ord(t)-97 for i,t in enumerate(c)]
 if errors:s.add(z3.PbLe([(m,1) for m in mism],errors))
 else:s.add(z3.And([z3.Not(m) for m in mism]))
 begin=time.monotonic();res=s.check();out={'result':str(res),'seconds':round(time.monotonic()-begin,3),'widths':widths,'error_bound':errors}
 if res==z3.sat:
  m=s.model();ks=[[m.eval(k).as_long() for k in keys] for keys in allkeys]
  plain=''.join(chr(m.eval(z3.Select(arrays[0],i)).as_long()+97) for i in range(n))
  predicted=plain
  for k in ks:predicted=enc(predicted,k)
  out.update(keys=ks,conditional_plaintext=plain,predicted_ciphertext=predicted,mismatch_positions=[i for i,(a,b) in enumerate(zip(c,predicted)) if a!=b])
  assert len(out['mismatch_positions'])<=errors
  recovered=predicted
  for k in ks[::-1]:recovered=dec(recovered,k)
  assert recovered==plain
 if res==z3.unknown:out['reason']=s.reason_unknown()
 return out
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--widths',default='5,6');ap.add_argument('--timeout',type=int,default=20000);ap.add_argument('--target',action='store_true');ap.add_argument('--glyph-variant',action='store_true');ap.add_argument('--omit',type=int,default=3);ap.add_argument('--errors',type=int,default=3);args=ap.parse_args()
 widths=list(map(int,args.widths.split(',')))
 if args.target:
  gs=(P/'transcription.txt').read_text().split()
  if args.glyph_variant:
   gs[7]='tsnnd';gs[9]='eloen';gs[11]='ercuv'
  c=''.join(g for i,g in enumerate(gs,1) if i!=args.omit);p=quote+'?' 
  out=solve(p,c,widths,args.errors,args.timeout,36461);out.update(mode='conditional_target',omitted_group=args.omit,source_quote_not_decryption=True,conditional_glyph_variant=args.glyph_variant)
 else:
  rng=random.Random(364610);p=quote+'r';c=p;true=[]
  for w in widths:
   k=list(range(w));rng.shuffle(k);true.append(k);c=enc(c,k)
  out=solve(p,c,widths,0,args.timeout,36461);out.update(mode='independent_planted_control',planted_keys=true,exact_planted_keys=out.get('keys')==true)
 print(json.dumps(out,indent=2))
