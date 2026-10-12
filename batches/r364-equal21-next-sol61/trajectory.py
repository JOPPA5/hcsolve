from collections import Counter
import time,sys
sys.path.insert(0,'/private/tmp/hcsolve-ortools')
from ortools.sat.python import cp_model

def solve(plain,variants,width=21,progressive=False,seconds=60):
 assert len(variants)==1;n=len(plain);q,r=divmod(n,width);assert r==2 and Counter(plain)==Counter(variants[0]);ct=variants[0];m=cp_model.CpModel();shared=m.new_int_var(0,width-3 if progressive else width-1,'alignment');ranks=[]
 for j in range(3):
  rr=[m.new_int_var(0,width-1,f'rank{j}_{col}')for col in range(width)];inv=[m.new_int_var(0,width-1,f'col{j}_{rank}')for rank in range(width)];m.add_inverse(rr,inv);m.add(rr[0]==shared+(j if progressive else 0));ranks.append(rr)
 positions=[list(range(n))]
 for j in range(2):
  vv=[m.new_int_var(0,n-1,f'position{j}_{i}')for i in range(n)];m.add_all_different(vv);positions.append(vv)
 final=[m.new_int_var_from_domain(cp_model.Domain.from_values([i for i,c in enumerate(ct)if c==ch]),f'final{i}')for i,ch in enumerate(plain)];m.add_all_different(final);positions.append(final)
 for stage in range(3):
  for i in range(n):
   src=positions[stage][i];dst=positions[stage+1][i]
   if isinstance(src,int):row=src//width;rank=ranks[stage][src%width]
   else:
    col=m.new_int_var(0,width-1,f'sourcecol{stage}_{i}');row=m.new_int_var(0,q,f'sourcerow{stage}_{i}');rank=m.new_int_var(0,width-1,f'sourcerank{stage}_{i}');m.add_modulo_equality(col,src,width);m.add_division_equality(row,src,width);m.add_element(col,ranks[stage],rank)
   before=[]
   for longcol in [0,1]:
    flag=m.new_bool_var(f'longbefore{stage}_{i}_{longcol}');m.add(ranks[stage][longcol]<rank).only_enforce_if(flag);m.add(ranks[stage][longcol]>=rank).only_enforce_if(flag.Not());before.append(flag)
   m.add(dst==q*rank+row+sum(before))
 assert not m.validate();solver=cp_model.CpSolver();solver.parameters.max_time_in_seconds=seconds;solver.parameters.num_search_workers=4;solver.parameters.random_seed=3642112;t=time.monotonic();status=solver.solve(m);out=dict(status=solver.status_name(status),seconds=time.monotonic()-t,widths=[width]*3,progressive=progressive,truth_key_seed=False,closed_r2_trajectories=True,intermediate_characters=0,branches=solver.num_branches,conflicts=solver.num_conflicts)
 if status in [cp_model.OPTIMAL,cp_model.FEASIBLE]:
  keys=[sorted(range(width),key=lambda col:solver.value(rr[col]))for rr in ranks];c=plain
  for k in keys:c=''.join(c[i]for col in k for i in range(col,len(c),width))
  assert c==ct;x=ct
  for k in keys[::-1]:
   arr=['']*n;at=0
   for col in k:
    for i in range(col,n,width):arr[i]=x[at];at+=1
   x=''.join(arr)
  assert x==plain;out.update(keys=keys,alignment=solver.value(shared)+1,full_encoder_inverse=True,plaintext=plain)
 return out
