import sys,time
from collections import Counter
sys.path.insert(0,'/private/tmp/hcsolve-z3')
import z3
def enc(s,k):return ''.join(s[c::len(k)]for c in k)
def dec(s,k):
 out=['']*len(s);at=0
 for col in k:
  for i in range(col,len(s),len(k)):out[i]=s[at];at+=1
 return ''.join(out)
def solve(p,c,w=22,seconds=120,backend='eager',known_keys=None,blocked_keys=None):
 assert len(p)==len(c) and len(p)%w==0
 assert Counter(p)-Counter(c)==Counter(n=1) and Counter(c)-Counter(p)==Counter(u=1)
 begin=time.monotonic();height=len(p)//w
 s=z3.Then('simplify','card2bv','bit-blast','sat').solver() if backend=='eager' else z3.SolverFor('QF_FD');s.set(timeout=seconds*1000,random_seed=36961222)
 R=[[[z3.Bool(f'r{j}_{col}_{rank}')for rank in range(w)]for col in range(w)]for j in range(3)]
 for stage in R:
  for row in stage:s.add(z3.PbEq([(v,1)for v in row],1))
  for rank in range(w):s.add(z3.PbEq([(stage[col][rank],1)for col in range(w)],1))
 for rank in range(w):
  if rank+2>=w:s.add(z3.Not(R[0][0][rank]))
  else:s.add(R[0][0][rank]==R[1][0][rank+1],R[0][0][rank]==R[2][0][rank+2])
 s.add(z3.Not(R[1][0][0]),z3.Not(R[1][0][w-1]),z3.Not(R[2][0][0]),z3.Not(R[2][0][1]))
 E={i:z3.Bool(f'error{i}')for i,ch in enumerate(c)if ch=='u'};s.add(z3.PbEq([(v,1)for v in E.values()],1))
 if known_keys:
  for stage,key in zip(R,known_keys):
   for rank,col in enumerate(key):s.add(stage[col][rank])
 if blocked_keys:s.add(z3.Or(*[z3.Not(R[j][col][rank])for j,key in enumerate(blocked_keys)for rank,col in enumerate(key)]))
 clauses=0
 for i,ch in enumerate(p):
  col0,row0=i%w,i//w
  for r0,A in enumerate(R[0][col0]):
   x=height*r0+row0;col1,row1=x%w,x//w
   for r1,B in enumerate(R[1][col1]):
    y=height*r1+row1;col2,row2=y%w,y//w;allowed=[]
    for r2,V in enumerate(R[2][col2]):
     pos=height*r2+row2
     if ch==c[pos]:allowed.append(z3.And(V,z3.Not(E[pos]))if pos in E else V)
     elif ch=='n' and c[pos]=='u':allowed.append(z3.And(V,E[pos]))
    s.add(z3.Or(z3.Not(A),z3.Not(B),*allowed));clauses+=1
 build=time.monotonic()-begin;at=time.monotonic();status=s.check();out=dict(status=str(status),solve_seconds=time.monotonic()-at,build_seconds=build,widths=[w]*3,height=height,backend=backend,timeout=seconds,rank_bool_variables=3*w*w,endpoint_clauses=clauses,unknown_progressive_alignment=True,error_channel='predictedN->literalU')
 if status==z3.sat:
  m=s.model();keys=[sorted(range(w),key=lambda col:next(r for r,V in enumerate(stage[col])if z3.is_true(m.eval(V))))for stage in R];v=p
  for key in keys:v=enc(v,key)
  mis=[i for i,(a,b)in enumerate(zip(v,c))if a!=b];assert len(mis)==1 and v[mis[0]]=='n'and c[mis[0]]=='u'
  inverse=v
  for key in reversed(keys):inverse=dec(inverse,key)
  assert inverse==p and [k.index(0)for k in keys]==[keys[0].index(0)+j for j in range(3)]
  out.update(keys=keys,recovered_n=keys[0].index(0)+1,predicted_ciphertext=v,mismatch_position1=mis[0]+1,inverse_exact=True,reencryption_exact_with_declared_error=True)
 else:out['reason']=s.reason_unknown()if status==z3.unknown else'UNSAT under exact assumptions'
 return out
