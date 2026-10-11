from pathlib import Path
from collections import Counter
import sys,time,json
sys.path.insert(0,'/private/tmp/hcsolve-ortools')
from ortools.sat.python import cp_model
import ortools

def enc(s,key):return ''.join(s[col::len(key)] for col in key)
def dec(s,key):
 a=['']*len(s);at=0
 for col in key:
  for i in range(col,len(s),len(key)):a[i]=s[at];at+=1
 return ''.join(a)
def solve(plain,cipher,widths,seconds=60,errors=0,alignments=None,known_keys=None,hint_keys=None, optimize_errors=False):
 assert len(plain)==len(cipher);N=len(cipher);m=cp_model.CpModel();counts=Counter(plain.replace('?',''));extra=plain.count('?');alphabet=set(counts)|set('abcdefghijklmnopqrstuvwxyz' if extra else '');domain=cp_model.Domain.from_values(sorted(ord(c)-97 for c in alphabet))
 stages=[];first=[]
 for i,c in enumerate(plain):first.append(ord(c)-97 if c!='?' else m.new_int_var(0,25,f'filler{i}'))
 stages.append(first)
 for j in range(len(widths)-1):stages.append([m.new_int_var_from_domain(domain,f'char{j}_{i}') for i in range(N)])
 out=[m.new_int_var(0,25,f'out{i}') for i in range(N)] if errors or optimize_errors else [ord(c)-97 for c in cipher];stages.append(out)
 if errors or optimize_errors:
  mismatch=[]
  for i,(v,c) in enumerate(zip(out,cipher)):
   b=m.new_bool_var(f'wrong{i}');m.add(v!=ord(c)-97).only_enforce_if(b);m.add(v==ord(c)-97).only_enforce_if(b.Not());mismatch.append(b)
  m.add(sum(mismatch)<=errors)
  if optimize_errors:m.minimize(sum(mismatch))
 # Inventory constraints propagate through every intermediate stage.
 for j,cells in enumerate(stages[1:-1]):
  for ch in alphabet:
   bs=[]
   for i,v in enumerate(cells):
    b=m.new_bool_var(f'count{j}_{ch}_{i}');m.add(v==ord(ch)-97).only_enforce_if(b);m.add(v!=ord(ch)-97).only_enforce_if(b.Not());bs.append(b)
   m.add(sum(bs)>=counts[ch]);m.add(sum(bs)<=counts[ch]+extra)
 allstarts=[]
 for j,w in enumerate(widths):
  q,r=divmod(N,w);starts=[];intervals=[]
  for col in range(w):
   length=q+(col<r);possible=set()
   for before in range(w):
    longs_other=r-(col<r);shorts_other=w-r-(col>=r)
    for lo in range(max(0,before-shorts_other),min(before,longs_other)+1):
     at=q*before+lo
     if at+length<=N:possible.add(at)
   start=m.new_int_var_from_domain(cp_model.Domain.from_values(sorted(possible)),f'start{j}_{col}');starts.append(start);intervals.append(m.new_interval_var(start,length,start+length,f'interval{j}_{col}'))
   for row in range(length):m.add_element(start+row,stages[j+1],stages[j][row*w+col])
  m.add_no_overlap(intervals)
  if alignments:
   before=[]
   for col in range(1,w):
    b=m.new_bool_var(f'beforezero{j}_{col}');m.add(starts[col]<starts[0]).only_enforce_if(b);m.add(starts[col]>starts[0]).only_enforce_if(b.Not());before.append(b)
   m.add(sum(before)==alignments[j]-1)
  for keys,is_hint in [(known_keys,False),(hint_keys,True)]:
   if keys:
    at=0
    for col in keys[j]:
     if is_hint:m.add_hint(starts[col],at)
     else:m.add(starts[col]==at)
     at+=q+(col<r)
  allstarts.append(starts)
 if hint_keys and '?' not in plain:
  hinted=plain
  for j,key in enumerate(hint_keys):
   hinted=enc(hinted,key)
   for var,ch in zip(stages[j+1],hinted):
    if not isinstance(var,int):m.add_hint(var,ord(ch)-97)
  if errors or optimize_errors:
   for b,x,y in zip(mismatch,hinted,cipher):m.add_hint(b,int(x!=y))
 validation=m.validate();assert not validation,validation
 solver=cp_model.CpSolver();solver.parameters.max_time_in_seconds=seconds;solver.parameters.num_search_workers=4;solver.parameters.random_seed=364611;solver.parameters.log_search_progress=False
 if optimize_errors:solver.parameters.use_lns_only=True
 t=time.monotonic();status=solver.solve(m);result=dict(status=solver.status_name(status),seconds=time.monotonic()-t,widths=widths,timeout_seconds=seconds,errors=errors,alignments=alignments,ortools_version=ortools.__version__,model_validation=validation,booleans=solver.num_booleans,conflicts=solver.num_conflicts,branches=solver.num_branches)
 if status in [cp_model.OPTIMAL,cp_model.FEASIBLE]:
  keys=[sorted(range(w),key=lambda col:solver.value(starts[col])) for w,starts in zip(widths,allstarts)];p=''.join(chr(v+97) if isinstance(v,int) else chr(solver.value(v)+97) for v in first);s=p
  for key in keys:s=enc(s,key)
  mismatches=[i for i,(x,y) in enumerate(zip(s,cipher)) if x!=y];assert len(mismatches)<=errors
  d=s
  for key in reversed(keys):d=dec(d,key)
  assert d==p
  if alignments:assert all(k.index(0)+1==n for k,n in zip(keys,alignments))
  result.update(objective=solver.objective_value,best_objective_bound=solver.best_objective_bound,exact_wholetext=len(mismatches)==0,keys=keys,conditional_plaintext=p,predicted_ciphertext=s,mismatches=mismatches,inverse_exact=True)
 return result
