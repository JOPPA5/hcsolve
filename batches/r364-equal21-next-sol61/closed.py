from collections import Counter
import time,sys
sys.path.insert(0,'/private/tmp/hcsolve-ortools')
from ortools.sat.python import cp_model

def solve(plain,variants,width=21,progressive=False,seconds=60,inventory=True,pattern_first=False):
 n=len(plain);q,r=divmod(n,width);assert r==2 and all(len(c)==n for c in variants)and all(Counter(c)==Counter(plain)for c in variants)
 m=cp_model.CpModel();alpha=sorted(set(plain));domain=cp_model.Domain.from_values([ord(c)-97 for c in alpha]);stages=[[ord(c)-97 for c in plain]]
 for j in range(2):stages.append([m.new_int_var_from_domain(domain,f'char{j}_{i}')for i in range(n)])
 if len(variants)==1:out=[ord(c)-97 for c in variants[0]]
 else:
  choice=m.new_int_var(0,len(variants)-1,'source_variant');out=[]
  for i in range(n):
   values=[ord(c[i])-97 for c in variants]
   if len(set(values))==1:out.append(values[0])
   else:
    x=m.new_int_var_from_domain(cp_model.Domain.from_values(sorted(set(values))),f'out{i}');m.add_element(choice,values,x);out.append(x)
 stages.append(out)
 if inventory:
  for j,cells in enumerate(stages[1:-1]):
   for ch,count in Counter(plain).items():
    flags=[]
    for i,cell in enumerate(cells):
     yes=m.new_bool_var(f'count{j}_{ch}_{i}');m.add(cell==ord(ch)-97).only_enforce_if(yes);m.add(cell!=ord(ch)-97).only_enforce_if(yes.Not());flags.append(yes)
    m.add(sum(flags)==count)
 shared=m.new_int_var(0,width-3 if progressive else width-1,'unknown_alignment_zero');allranks=[];special=[]
 for j in range(3):
  ranks=[m.new_int_var(0,width-1,f'rank{j}_{c}')for c in range(width)];inverse=[m.new_int_var(0,width-1,f'col{j}_{k}')for k in range(width)];m.add_inverse(ranks,inverse);m.add(ranks[0]==shared+(j if progressive else 0));allranks.append(ranks);special.append(ranks[1])
  for col in range(width):
   flags=[]
   for longcol in [0,1]:
    if longcol==col:flags.append(0)
    else:
     flag=m.new_bool_var(f'before{j}_{longcol}_{col}');m.add(ranks[longcol]<ranks[col]).only_enforce_if(flag);m.add(ranks[longcol]>ranks[col]).only_enforce_if(flag.Not());flags.append(flag)
   length=q+(col<2);start=m.new_int_var(0,n-length,f'start{j}_{col}');m.add(start==q*ranks[col]+sum(flags))
   for row in range(length):m.add_element(start+row,stages[j+1],stages[j][row*width+col])
 m.add_decision_strategy([shared]+special,cp_model.CHOOSE_FIRST,cp_model.SELECT_MIN_VALUE)
 if pattern_first:m.add_decision_strategy([rank for ranks in allranks for rank in ranks[2:]],cp_model.CHOOSE_MIN_DOMAIN_SIZE,cp_model.SELECT_MIN_VALUE)
 assert not m.validate()
 solver=cp_model.CpSolver();solver.parameters.max_time_in_seconds=seconds;solver.parameters.num_search_workers=4;solver.parameters.random_seed=3642112
 if pattern_first:solver.parameters.search_branching=cp_model.FIXED_SEARCH;solver.parameters.num_search_workers=1
 t=time.monotonic();status=solver.solve(m);result=dict(status=solver.status_name(status),seconds=time.monotonic()-t,widths=[width]*3,progressive=progressive,unknown_alignment=True,truth_key_seed=False,closed_rank_start_formula=True,inventory=inventory,pattern_first_fixed_search=pattern_first,branches=solver.num_branches,conflicts=solver.num_conflicts)
 if status in [cp_model.OPTIMAL,cp_model.FEASIBLE]:
  keys=[sorted(range(width),key=lambda c:solver.value(ranks[c]))for ranks in allranks];pred=plain
  for k in keys:pred=''.join(pred[i]for col in k for i in range(col,len(pred),width))
  assert pred in variants;x=pred
  for k in keys[::-1]:
   a=['']*n;at=0
   for col in k:
    for i in range(col,n,width):a[i]=x[at];at+=1
   x=''.join(a)
  assert x==plain;result.update(keys=keys,alignment=solver.value(shared)+1,full_encoder_inverse=True,plaintext=plain,selected_ciphertext=pred)
 return result
