"""Exact three-columnar endpoint clauses, no intermediate letters or trajectories."""
import sys,time,json
from collections import Counter
sys.path.insert(0,'/private/tmp/hcsolve-z3')
import z3

def enc(p,k):return ''.join(p[c::len(k)]for c in k)
def domain(n,w,col):
 q,r=divmod(n,w);L=q+(col<r);starts=set()
 for before in range(w):
  for longs in range(max(0,before-(w-r-(col>=r))),min(before,r-(col<r))+1):
   at=q*before+longs
   if at+L<=n:starts.add(at)
 return sorted(starts)
def solve(p,c,widths=(21,19,20),seconds=60,reverse_support=False,common_rank=False,rank_partition=False,direct_rank_link=False):
 assert len(p)==len(c) and Counter(p)==Counter(c);n=len(p);begin=time.monotonic();s=z3.SolverFor('QF_FD') if rank_partition else z3.Then('simplify','card2bv','bit-blast','sat').solver();s.set(timeout=int(seconds*1000),random_seed=364231111)
 opts=[];literals=0
 for stage,w in enumerate(widths):
  cols=[];occupy=[[]for _ in range(n)]
  for col in range(w):
   values={at:z3.Bool(f's{stage}c{col}a{at}')for at in domain(n,w,col)};cols.append(values);literals+=len(values);s.add(z3.PbEq([(v,1)for v in values.values()],1))
   for at,v in values.items():
    for row in range(len(range(col,n,w))):occupy[at+row].append(v)
  for occupied in occupy:s.add(z3.PbEq([(v,1)for v in occupied],1))
  opts.append(cols)
 if common_rank:
  shared=z3.BitVec('common_alignment_rank',5);s.add(z3.ULT(shared,min(widths)))
  for stage,w in enumerate(widths):
   ranks=[z3.BitVec(f'rank{stage}_{i}',5)for i in range(n+1)];s.add(ranks[0]==0,ranks[n]==w)
   for rank in ranks:s.add(z3.ULE(rank,w))
   for col,values in enumerate(opts[stage]):
    length=len(range(col,n,w))
    for at,V in values.items():
     s.add(z3.Implies(V,ranks[at+length]==ranks[at]+1))
     if col==0:
      s.add(z3.Implies(V,ranks[at]==shared))
      if direct_rank_link:
       q,rem=divmod(n,w);lo=rem-(0<rem);short=w-rem-(0>=rem)
       allowed=[before for before in range(w)if max(0,before-short)<=at-q*before<=min(before,lo)]
       s.add(z3.Implies(V,z3.Or(*[shared==before for before in allowed])))
 w0,w1,w2=widths;clauses=0;disallowed=0
 # Compose stages zero and one exactly, constrain final placement directly.
 for i,ch in enumerate(p):
  col0,row0=i%w0,i//w0
  for a,A in opts[0][col0].items():
   x=a+row0;col1,row1=x%w1,x//w1
   for bb,B in opts[1][col1].items():
    y=bb+row1;col2,row2=y%w2,y//w2
    allowed=[V for at,V in opts[2][col2].items()if c[at+row2]==ch]
    s.add(z3.Or(z3.Not(A),z3.Not(B),*allowed));clauses+=1;disallowed+=not allowed
 reverse_clauses=0
 if reverse_support:
  occurrences={ch:[i for i,x in enumerate(p)if x==ch]for ch in set(c)}
  for col2,values in enumerate(opts[2]):
   for at,C in values.items():
    for row2 in range(len(range(col2,n,w2))):
     final=at+row2;y=row2*w2+col2;ch=c[final]
     for col1,valuesB in enumerate(opts[1]):
      length=len(range(col1,n,w1))
      for bb,B in valuesB.items():
       if not bb<=y<bb+length:continue
       x=(y-bb)*w1+col1
       allowed=[opts[0][pos%w0][x-pos//w0]for pos in occurrences[ch]if x-pos//w0 in opts[0][pos%w0]]
       s.add(z3.Or(z3.Not(C),z3.Not(B),*allowed));reverse_clauses+=1
 build=time.monotonic()-begin;at=time.monotonic();checks=[]
 if rank_partition:
  assert common_rank
  guards=[z3.Bool(f'assume_alignment_{j}')for j in range(min(widths))]
  for rank,g in enumerate(guards):s.add(z3.Implies(g,shared==rank))
  for rank in range(min(widths)):
   step=time.monotonic();status=s.check(guards[rank]);checks.append(dict(rank=rank+1,status=str(status),seconds=time.monotonic()-step))
   if status==z3.sat:break
  if status!=z3.sat and any(v['status']=='unknown'for v in checks):status=z3.unknown
 else:status=s.check()
 out=dict(status=str(status),seconds=time.monotonic()-at,build_seconds=build,widths=list(widths),selected_start_variables=literals,endpoint_clauses=clauses,reverse_support_clauses=reverse_clauses,empty_support_clauses=disallowed,truth_key_seed=False,rank_partition_checks=checks,common_unknown_alignment_rank=common_rank,direct_column0_rank_start_link=direct_rank_link,intermediate_character_variables=0)
 if status==z3.sat:
  m=s.model();keys=[sorted(range(w),key=lambda col:next(at for at,v in opts[j][col].items()if z3.is_true(m.eval(v))))for j,w in enumerate(widths)];v=p
  for k in keys:v=enc(v,k)
  assert v==c;out.update(keys=keys,full_reencryption=True)
  if common_rank:out['recovered_alignment']=m.eval(shared).as_long()+1;assert all(k.index(0)+1==out['recovered_alignment']for k in keys)
 else:out['reason']=('at least one alignment rank timed out'if rank_partition else s.reason_unknown())if status==z3.unknown else 'exact UNSAT'
 return out
