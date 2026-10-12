from run import *

def worker(n):
 inp=json.loads((b/'control-input.json').read_text());names=json.loads((b/'control-names.json').read_text());formula=CNF(from_file=str(b/'control.cnf'))
 with Solver(name='cadical195',bootstrap_with=formula.clauses,use_timer=True)as s:
  s.conf_budget(2000000);t=time.monotonic();status=s.solve_limited(assumptions=[names[f'n{n-1}']]);r=dict(backend='cadical195',known_n=n,keys_seeded=False,conflict_budget=2000000,status='sat'if status is True else'unsat'if status is False else'unknown',seconds=time.monotonic()-t,stats=s.accum_stats())
  if status:r.update(witness(s.get_model(),names,inp['p'],inp['raw'],[21,19,20],False))
  (b/'control-cadical195-deep.json').write_text(json.dumps(r,indent=2)+'\n');print('deepcontrol',r['status'],r['seconds'],flush=True)
if __name__=='__main__':
 n=json.loads((b/'control-truth.json').read_text())['n'];proc=mp.Process(target=worker,args=(n,));proc.start();proc.join(45)
 if proc.is_alive():print('deepworker stillactive at45s',flush=True);proc.join(45)
 if proc.is_alive():proc.terminate();proc.join();(b/'control-cadical195-deep.json').write_text(json.dumps(dict(backend='cadical195',known_n=n,keys_seeded=False,status='unknown',conflict_budget=2000000,worker_wall_cap_seconds=90,process_terminated=True))+'\n');print('deepworker90s wallcapUNKNOWN',flush=True)
