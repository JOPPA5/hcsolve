"""Independent CP-SAT interval model; conditional known-plaintext only.
Dependency ortools9.15.6755 in /private/tmp/hcsolve-ortools (PyPI).
Google official CP-SAT docs: https://developers.google.com/optimization/cp/cp_solver
Every column is one fixed-length interval in the output, with NoOverlap tiling.
"""
import sys,json,random,time,argparse
from pathlib import Path
from collections import Counter
sys.path.insert(0,'/private/tmp/hcsolve-ortools')
from ortools.sat.python import cp_model
P=Path(__file__).parent
quote='nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcisloxr'
def enc(p,k):return ''.join(p[i::len(k)] for i in k)
def solve(p,c,widths,timeout=20,align=None):
 n=len(p);m=cp_model.CpModel();chars=sorted({ord(t)-97 for t in p});domain=cp_model.Domain.from_values(chars)
 stages=[[ord(t)-97 for t in p]]
 for j in range(len(widths)-1):
  cells=[m.new_int_var_from_domain(domain,f'char{j}_{i}') for i in range(n)]
  for ch,count in Counter(p).items():
   flags=[]
   for i,cell in enumerate(cells):
    b=m.new_bool_var(f'eq{j}_{i}_{ch}');m.add(cell==ord(ch)-97).only_enforce_if(b);m.add(cell!=ord(ch)-97).only_enforce_if(b.negated());flags.append(b)
   m.add(sum(flags)==count)
  stages.append(cells)
 stages.append([ord(t)-97 for t in c]);allstarts=[]
 for j,w in enumerate(widths):
  q,r=divmod(n,w);starts=[];ivs=[]
  feasible=set()
  for before in range(w):
   for longs in range(max(0,before-(w-r)),min(before,r)+1):feasible.add(q*before+longs)
  for col in range(w):
   size=q+(col<r);sd=cp_model.Domain.from_values(sorted(v for v in feasible if v+size<=n))
   start=m.new_int_var_from_domain(sd,f'start{j}_{col}');starts.append(start)
   ivs.append(m.new_fixed_size_interval_var(start,size,f'interval{j}_{col}'))
   for row in range(size):m.add_element(start+row,stages[j+1],stages[j][row*w+col])
  m.add_no_overlap(ivs)
  if align is not None:
   before=[]
   for col in range(1,w):
    b=m.new_bool_var(f'before{j}_{col}');m.add(starts[col]<starts[0]).only_enforce_if(b);m.add(starts[col]>starts[0]).only_enforce_if(b.negated());before.append(b)
   m.add(sum(before)==align-1)
  allstarts.append(starts)
 s=cp_model.CpSolver();s.parameters.max_time_in_seconds=timeout;s.parameters.num_search_workers=2;s.parameters.random_seed=364621
 begin=time.monotonic();status=s.solve(m)
 out=dict(status=s.status_name(status),seconds=time.monotonic()-begin,widths=widths,alignment=align,timeout_seconds=timeout)
 if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):
  keys=[sorted(range(len(starts)),key=lambda col:s.value(starts[col])) for starts in allstarts];pred=p
  for k in keys:pred=enc(pred,k)
  assert pred==c
  out.update(keys=keys,re_encryption_exact=True)
 return out
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--widths',default='16,17,18');ap.add_argument('--timeout',type=int,default=20);ap.add_argument('--alignment',type=int);args=ap.parse_args();widths=list(map(int,args.widths.split(',')))
 rng=random.Random(364628);keys=[];c=quote
 for w in widths:
  k=rng.sample(range(w),w)
  if args.alignment:
   k.remove(0);k.insert(args.alignment-1,0)
  keys.append(k);c=enc(c,k)
 out=solve(quote,c,widths,args.timeout,args.alignment);out.update(mode='independent_planted_control',planted_keys=keys,exact_planted_keys=out.get('keys')==keys)
 name='cp-control-'+args.widths.replace(',','-')+('-align'+str(args.alignment) if args.alignment else '')+'.json'
 (P/name).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
