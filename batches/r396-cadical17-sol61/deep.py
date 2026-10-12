from run import *
from pysat.formula import CNF

def one(backend,n):
 inp=json.loads((b/'control-input.json').read_text());names=json.loads((b/'names.json').read_text());formula=CNF(from_file=str(b/'control.cnf'))
 with Solver(name=backend,bootstrap_with=formula.clauses,use_timer=True)as s:
  s.conf_budget(500000);t=time.monotonic();status=s.solve_limited(assumptions=[names[f'r0_0_{n-1}']]);r=dict(backend=backend,known_n=n,keys_seeded=False,conflict_budget=500000,status='sat'if status is True else'unsat'if status is False else'unknown',seconds=time.monotonic()-t,stats=s.accum_stats())
  if status:r.update(witness(s.get_model(),names,inp['p'],inp['c'],17))
  (b/f'{backend}-deep-conditioned.json').write_text(json.dumps(r,indent=2)+'\n');print(backend,r['status'],r['seconds'],flush=True)
if __name__=='__main__':
 # Public calibration truth is used only for declared daily-n conditioning, never a key hint.
 n=json.loads(Path('batches/r396-rank-support17-sol61/control-truth.json').read_text())['n']
 for backend in ['cadical195','cadical300']:
  p=mp.Process(target=one,args=(backend,n));p.start();p.join(45)
  if p.is_alive():p.terminate();p.join();(b/f'{backend}-deep-conditioned.json').write_text(json.dumps(dict(backend=backend,known_n=n,keys_seeded=False,status='unknown',worker_wall_cap_seconds=45,process_terminated=True,conflict_budget=500000))+'\n');print(backend,'WALLTIME UNKNOWN',flush=True)
