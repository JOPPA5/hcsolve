from run import *
from threading import Timer

def worker(n):
 inp=json.loads((b/'control-input.json').read_text());names=json.loads((b/'control-names.json').read_text());formula=CNF(from_file=str(b/'control.cnf'))
 with Solver(name='glucose42',bootstrap_with=formula.clauses,use_timer=True)as s:
  s.conf_budget(2000000);timer=Timer(45,s.interrupt);t=time.monotonic();timer.start()
  try:status=s.solve_limited(assumptions=[names[f'n{n-1}']],expect_interrupt=True)
  finally:timer.cancel()
  r=dict(backend='glucose42',status='sat'if status is True else'unsat'if status is False else'unknown',known_n=n,keys_seeded=False,conflict_budget=2000000,timer_seconds=45,seconds=time.monotonic()-t,stats=s.accum_stats())
  if status:r.update(witness(s.get_model(),names,inp['p'],inp['raw'],[21,19,20],False))
  (b/'control-glucose42.json').write_text(json.dumps(r,indent=2)+'\n');print('glucose42',r['status'],r['seconds'],flush=True)
if __name__=='__main__':
 audit(backends=['glucose42'],filename='glucose-exhaustive-audit.json');n=json.loads((b/'control-truth.json').read_text())['n'];proc=mp.Process(target=worker,args=(n,));proc.start();proc.join(55)
 if proc.is_alive():proc.terminate();proc.join();(b/'control-glucose42.json').write_text(json.dumps(dict(backend='glucose42',status='unknown',known_n=n,keys_seeded=False,worker_wall_cap_seconds=55,process_terminated=True))+'\n')
