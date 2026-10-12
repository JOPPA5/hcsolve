from pathlib import Path
from itertools import permutations,product
import sys,json,time,hashlib,multiprocessing as mp
sys.path.insert(0,'/private/tmp/hcsolve-pysat')
from pysat.solvers import Solver
from model import build,z3
b=Path(__file__).resolve().parent

def encode(p,keys):
 for k in keys:p=''.join(p[i]for col in k for i in range(col,len(p),len(k)))
 return p
def inverse(c,keys):
 for k in keys[::-1]:
  a=['']*len(c);at=0
  for col in k:
   for i in range(col,len(c),len(k)):a[i]=c[at];at+=1
  c=''.join(a)
 return c
def cnf(p,c,w=17,progressive=False,errorPF=False):
 t=time.monotonic();s,ranks,clauses=build(p,c,w,progressive=progressive,errorPF=errorPF);g=z3.Goal();g.add(*s.assertions());cg=z3.Then('simplify','card2bv','bit-blast','tseitin-cnf')(g)[0];dimacs=cg.dimacs(include_names=True);lines=dimacs.splitlines();names={};clauses=[]
 for line in lines:
  if line.startswith('c '):_,num,name=line.split(' ',2);names[name]=int(num)
  elif line and not line.startswith('p '):clauses.append([int(x)for x in line.split()[:-1]])
 assert all(f'r{st}_{col}_{r}'in names for st in range(3)for col in range(w)for r in range(w))
 return dimacs,names,clauses,time.monotonic()-t

def witness(model,names,p,c,w):
 yes=set(x for x in model if x>0);ks=[]
 for st in range(3):
  ranks={col:next(r for r in range(w)if names[f'r{st}_{col}_{r}']in yes)for col in range(w)};k=sorted(range(w),key=ranks.__getitem__);assert sorted(ranks.values())==list(range(w));ks.append(k)
 assert encode(p,ks)==c and inverse(c,ks)==p
 return dict(keys=ks,p=p,c=c,n=ks[0].index(0)+1,full_observed_encoder_inverse_exact=True)
def audit():
 p='aaaabbbb';w=3;outputs={}
 for n in range(1,4):
  orders=[k for k in permutations(range(w))if k.index(0)==n-1]
  for ks in product(orders,repeat=3):outputs.setdefault(encode(p,ks),set()).add(n)
 cs=sorted(set(''.join(x)for x in permutations(p)));rows=[]
 for c in cs:
  _,names,clauses,_=cnf(p,c,w)
  for backend in ['cadical195','cadical300']:
   with Solver(name=backend,bootstrap_with=clauses)as solver:
    for n in range(1,4):
     r=solver.solve(assumptions=[names[f'r0_0_{n-1}']]);expected=n in outputs.get(c,set());assert r==expected
     if r:witness(solver.get_model(),names,p,c,w)
     rows.append(dict(c=c,n=n,backend=backend,sat=r))
 (b/'exhaustive-audit.json').write_text(json.dumps(dict(p=p,w=w,cipher_inventory_permutations=len(cs),direct_fullkey_cartesian_enumerated=True,case_count=len(rows),all_statuses_agree=True,all_SAT_witnesses_encoder_inverse_exact=True,rows=rows),indent=2)+'\n');print('audit PASS',len(rows),flush=True)
def worker(backend,conditioned):
 from pysat.formula import CNF
 inp=json.loads((b/'control-input.json').read_text());names=json.loads((b/'names.json').read_text());formula=CNF(from_file=str(b/'control.cnf'));p,c=inp['p'],inp['c'];rows=[]
 with Solver(name=backend,bootstrap_with=formula.clauses,use_timer=True)as s:
  ns=[conditioned]if conditioned else range(1,18)
  for n in ns:
   s.conf_budget(20000);t=time.monotonic();status=s.solve_limited(assumptions=[names[f'r0_0_{n-1}']]);r=dict(n=n,status='sat'if status is True else'unsat'if status is False else'unknown',seconds=time.monotonic()-t,conflict_budget=20000,stats=s.accum_stats())
   if status:r.update(witness(s.get_model(),names,p,c,17))
   rows.append(r)
   f=b/f'{backend}-{"conditioned"if conditioned else"blind"}.json';f.write_text(json.dumps(dict(backend=backend,known_n=conditioned,keys_seeded=False,results=rows),indent=2)+'\n');print(backend,'conditioned'if conditioned else'blind',n,r['status'],flush=True)
   if status:break
if __name__=='__main__':
 audit();inp=json.loads(Path('batches/r396-rank-support17-sol61/control-input.json').read_text());truth=json.loads(Path('batches/r396-rank-support17-sol61/control-truth.json').read_text());(b/'control-input.json').write_text(json.dumps(inp,indent=2)+'\n');d,names,clauses,bt=cnf(inp['p'],inp['c']);(b/'control.cnf').write_text(d);(b/'names.json').write_text(json.dumps(names));(b/'cnf-summary.json').write_text(json.dumps(dict(clauses=len(clauses),variables=max(names.values()),build_seconds=bt,source_frozen_control_sha256=hashlib.sha256(Path('batches/r396-rank-support17-sol61/control-input.json').read_bytes()).hexdigest()),indent=2)+'\n');print('converted',len(clauses),bt,flush=True)
 for backend in ['cadical195','cadical300']:
  for conditioned in [truth['n'],None]:
   process=mp.Process(target=worker,args=(backend,conditioned));process.start();process.join(60)
   if process.is_alive():process.terminate();process.join();(b/f'{backend}-{"conditioned"if conditioned else"blind"}-worker-timeout.json').write_text(json.dumps(dict(worker_wall_cap_seconds=60,status='unknown',process_terminated=True))+'\n');print('wallcap',backend,conditioned,flush=True)
