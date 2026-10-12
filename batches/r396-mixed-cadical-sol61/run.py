from pathlib import Path
from itertools import permutations,product
from collections import Counter
import sys,json,time,hashlib,random,multiprocessing as mp
sys.path.insert(0,'/private/tmp/hcsolve-pysat')
from pysat.solvers import Solver
from pysat.formula import CNF
from model import build,enc,dec,z3
b=Path(__file__).resolve().parent

def encode(p,keys):
 for k in keys:p=enc(p,k)
 return p
def inverse(c,keys):
 for k in keys[::-1]:c=dec(c,k)
 return c
def cnf(p,c,widths=(21,19,20),progressive=False):
 s,opts,ns,stats=build(p,c,widths=widths,progressive=progressive);g=z3.Goal();g.add(*s.assertions());t=time.monotonic();cg=z3.Then('simplify','card2bv','bit-blast','tseitin-cnf')(g)[0];d=cg.dimacs(include_names=True);names={};clauses=[]
 for line in d.splitlines():
  if line.startswith('c '):_,num,name=line.split(' ',2);names[name]=int(num)
  elif line and not line.startswith('p '):clauses.append([int(x)for x in line.split()[:-1]])
 stats.update(cnf_seconds=time.monotonic()-t,cnf_clauses=len(clauses),cnf_variables=max(names.values()));assert all(str(n)in names for n in ns)
 return d,names,clauses,stats

def witness(model,names,p,raw,widths,progressive):
 yes=set(i for i in model if i>0);keys=[]
 for st,w in enumerate(widths):
  starts=[]
  for col in range(w):
   matches=[int(name.split('_')[2])for name,v in names.items()if name.startswith(f'A{st}_{col}_')and v in yes];assert len(matches)==1;starts.append((matches[0],col))
  keys.append([col for at,col in sorted(starts)])
 error=[int(name[1:])for name,v in names.items()if name.startswith('E')and name[1:].isdigit()and v in yes];assert len(error)==1;at=error[0];assert raw[at]=='p';expected=raw[:at]+'f'+raw[at+1:];assert encode(p,keys)==expected and inverse(expected,keys)==p;literal=inverse(raw,keys);assert encode(literal,keys)==raw;diff=[i for i,(a,c)in enumerate(zip(p,literal))if a!=c];assert len(diff)==1 and p[diff[0]]=='f'and literal[diff[0]]=='p';n=keys[0].index(0)+1;assert[key.index(0)+1 for key in keys]==[n+st if progressive else n for st in range(3)]
 return dict(keys=keys,n=n,p=p,raw_ciphertext=raw,expected_ciphertext=expected,raw_literal_plaintext=literal,full_expected_encoder_inverse_exact=True,full_literal_reencode_exact=True,ciphertext_P_F_position1=at+1,literal_plaintext_P_for_F_position1=diff[0]+1)
def audit(backends=('cadical195','cadical300'),filename='exhaustive-audit.json'):
 p='fppaaaaa';widths=[3,4,3];outputs={False:{},True:{}}
 for prog in [False,True]:
  bound=min(w-st if prog else w for st,w in enumerate(widths))
  for n in range(1,bound+1):
   orders=[[k for k in permutations(range(w))if k.index(0)==n-1+(st if prog else 0)]for st,w in enumerate(widths)]
   for ks in product(*orders):outputs[prog].setdefault(encode(p,ks).replace('f','p'),set()).add(n)
 rows=[]
 for raw in sorted(set(''.join(p)for p in permutations('pppaaaaa'))):
  for prog in [False,True]:
   _,names,clauses,stats=cnf(p,raw,widths,prog);bound=min(w-st if prog else w for st,w in enumerate(widths))
   for backend in backends:
    with Solver(name=backend,bootstrap_with=clauses)as s:
     for n in range(1,bound+1):
      r=s.solve(assumptions=[names[f'n{n-1}']]);assert r==(n in outputs[prog].get(raw,set()))
      if r:witness(s.get_model(),names,p,raw,widths,prog)
      rows.append(dict(raw=raw,progressive=prog,n=n,backend=backend,sat=r))
 (b/filename).write_text(json.dumps(dict(cases=len(rows),widths=widths,all_direct_fullkey_reference_agrees=True,all_literal_witnesses_exact=True,rows=rows),indent=2)+'\n');print('mixed audit PASS',len(rows),flush=True)
def calibration(backend,n):
 inp=json.loads((b/'control-input.json').read_text());names=json.loads((b/'control-names.json').read_text());cn=CNF(from_file=str(b/'control.cnf'))
 with Solver(name=backend,bootstrap_with=cn.clauses,use_timer=True)as s:
  s.conf_budget(500000);t=time.monotonic();status=s.solve_limited(assumptions=[names[f'n{n-1}']]);r=dict(backend=backend,status='sat'if status is True else'unsat'if status is False else'unknown',known_n=n,keys_seeded=False,conflict_budget=500000,seconds=time.monotonic()-t,stats=s.accum_stats())
  if status:r.update(witness(s.get_model(),names,inp['p'],inp['raw'],[21,19,20],False))
  (b/f'control-{backend}.json').write_text(json.dumps(r,indent=2)+'\n');print('mixedcontrol',backend,r['status'],flush=True)
if __name__=='__main__':
 audit();p=Path('batches/repeat396-387-sol61/preferred-prepared-plaintext50.txt').read_text().strip();rng=random.Random(3962119206261);n=rng.randrange(1,20);keys=[]
 for w in [21,19,20]:k=rng.sample(range(1,w),w-1);k.insert(n-1,0);keys.append(k)
 c=encode(p,keys);err=c.index('f');raw=c[:err]+'p'+c[err+1:];assert Counter(p)-Counter(raw)==Counter(f=1)and Counter(raw)-Counter(p)==Counter(p=1);(b/'control-input.json').write_text(json.dumps(dict(p=p,raw=raw,widths=[21,19,20],only_daily_n_conditioning=True),indent=2)+'\n');(b/'control-truth.json').write_text(json.dumps(dict(keys=keys,n=n,ciphertext=c,injected_F_P_position1=err+1,seed=3962119206261),indent=2)+'\n');d,names,clauses,stats=cnf(p,raw);(b/'control.cnf').write_text(d);(b/'control-names.json').write_text(json.dumps(names));(b/'cnf-summary.json').write_text(json.dumps(stats,indent=2)+'\n');print('mixedconverted',stats,flush=True)
 for backend in ['cadical195','cadical300']:
  proc=mp.Process(target=calibration,args=(backend,n));proc.start();proc.join(45)
  if proc.is_alive():proc.terminate();proc.join();(b/f'control-{backend}.json').write_text(json.dumps(dict(backend=backend,status='unknown',known_n=n,keys_seeded=False,process_terminated=True,worker_wall_cap_seconds=45,conflict_budget=500000))+'\n');print('mixedcontrolwallcap',backend,flush=True)
