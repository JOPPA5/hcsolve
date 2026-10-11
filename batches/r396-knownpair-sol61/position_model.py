from pathlib import Path
import sys,time,json,random
sys.path.insert(0,'/private/tmp/hcsolve-z3')
import z3
from collections import Counter

def enc(p,key):return ''.join(p[j::len(key)]for j in key)
def inverse(c,key):
 out=['']*len(c);at=0
 for col in key:
  for i in range(col,len(c),len(key)):out[i]=c[at];at+=1
 assert at==len(c);return ''.join(out)
def selector(xs,index):
 value=xs[-1]
 for i in reversed(range(len(xs)-1)):value=z3.If(index==i,xs[i],value)
 return value

def solve(p,c,widths=(21,19,20),timeout=60000,known_keys=None,alignments=None,backend='eager'):
 N=len(p);assert len(c)==N and Counter(c)==Counter(p)
 s=z3.Then('simplify','solve-eqs','bit-blast','sat').solver()if backend=='eager'else z3.Solver();s.set(timeout=timeout,random_seed=34548621)
 b=max(6,N.bit_length()+1);ranks=[];starts=[]
 for phase,w in enumerate(widths):
  rank=[z3.BitVec(f'k{phase}_{col}',b)for col in range(w)];ranks.append(rank);s.add(*[rank[a]!=rank[d]for a in range(w)for d in range(a+1,w)]);s.add(*[z3.ULT(x,w)for x in rank]);q,r=divmod(N,w)
  # q*rank plus number of longer columns read earlier. This expresses exact irregular chunks.
  start=[((q+1)*rank[col]-sum(z3.If(z3.ULT(rank[j],rank[col]),z3.BitVecVal(1,b),z3.BitVecVal(0,b))for j in range(r,w)))if r>w//2 else(q*rank[col]+sum(z3.If(z3.ULT(rank[j],rank[col]),z3.BitVecVal(1,b),z3.BitVecVal(0,b))for j in range(r)))for col in range(w)];starts.append(start)
  if known_keys:
   inv={col:i for i,col in enumerate(known_keys[phase])};s.add(*[rank[col]==inv[col]for col in range(w)])
  if alignments:s.add(rank[0]==alignments[phase]-1)
 # No artificial intermediate letters/inventory: trace each known plaintext occurrence through exact permutation positions.
 unique=[];freq=Counter(p)
 for i,ch in enumerate(p):
  pos=z3.BitVecVal(i,b)
  for w,start in zip(widths,starts):
   rows=N//w;row=z3.BitVecVal(0,b)
   for j in range(1,rows+1):row=z3.If(z3.UGE(pos,j*w),z3.BitVecVal(j,b),row)
   col=pos-row*w;pos=selector(start,col)+row
  occurrences=[j for j,x in enumerate(c)if x==ch]
  s.add(z3.Or([pos==j for j in occurrences]));
  if freq[ch]==1:unique.append(dict(letter=ch,input=i,output=occurrences[0]))
 t=time.monotonic();r=s.check();out=dict(status=str(r),seconds=time.monotonic()-t,widths=list(widths),timeout_ms=timeout,backend=backend,unique_anchors=unique,alignments=alignments,known_keys_supplied=known_keys is not None)
 if r==z3.sat:
  m=s.model();keys=[]
  for rank in ranks:keys.append(sorted(range(len(rank)),key=lambda col:m.eval(rank[col]).as_long()))
  pred=p
  for k in keys:pred=enc(pred,k)
  assert pred==c;rev=c
  for k in reversed(keys):rev=inverse(rev,k)
  assert rev==p;out.update(keys=keys,plaintext=p,ciphertext=c,full_reencryption_exact=True,full_inverse_exact=True)
 else:out['reason']=s.reason_unknown()if r==z3.unknown else'UNSAT in precise family'
 return out
