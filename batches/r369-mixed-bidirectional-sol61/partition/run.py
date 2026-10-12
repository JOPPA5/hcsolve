from pathlib import Path
import json,importlib.util,os
B=Path(__file__).resolve().parent;(B/'owned-pid.txt').write_text(str(os.getpid())+'\n')
source=(B.parent/'engine.py').read_text().replace('blocked_keys=None,verbose=False):','blocked_keys=None,verbose=False,rank_partition=False,rank_cap=8):')
old='at=time.monotonic();status=s.check();out=dict('
new='''at=time.monotonic();checks=[]
 if rank_partition:
  for k,V in enumerate(nvars):
   s.set(timeout=rank_cap*1000);step=time.monotonic();status=s.check(V)
   checks.append(dict(n=k+1,status=str(status),seconds=time.monotonic()-step))
   if verbose:print('rank',k+1,str(status),round(checks[-1]['seconds'],2),flush=True)
   if status==z3.sat:break
  if status!=z3.sat and any(r['status']=='unknown'for r in checks):status=z3.unknown
 else:status=s.check()
 out=dict(rank_partition_checks=checks,rank_cap_seconds=rank_cap if rank_partition else None,'''
assert old in source;source=source.replace(old,new).replace("else:out['reason']=s.reason_unknown()if status==z3.unknown else'UNSAT under stated conditions'","else:out['reason']=('some rank checks timed out'if rank_partition else s.reason_unknown())if status==z3.unknown else'UNSAT under stated conditions'")
(B/'engine.py').write_text(source)
sp=importlib.util.spec_from_file_location('partition',B/'engine.py');e=importlib.util.module_from_spec(sp);sp.loader.exec_module(e)
def save(name,obj):(B/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n')
# Same frozen control input, no truth-key/n hints. One compiled solver retained
# across ascending rank assumptions; not a collection of fresh restarts.
truth=json.loads((B.parent/'control-truth.json').read_text());p=truth['plaintext'];c=truth['observed_ciphertext']
control=e.solve(p,c,seconds=120,rank_partition=True,rank_cap=8,verbose=True)
if control['status']=='sat':control['all_planted_keys_recovered']=control['keys']==truth['keys']
save('control',control);print('partition control',control['status'],flush=True)
if control['status']!='sat':print('Actual target gated off.',flush=True);raise SystemExit(0)
rows=json.loads(Path('batches/repeat369-365-sol61/closest-inventory.json').read_text());row=next(x for x in rows if x['first_sentence_X']==1 and x['second_sentence_X']==1)
target=e.solve(row['plaintext'],row['ciphertext'],rank_partition=True,rank_cap=15,verbose=True);target['conditional_preparation']=row;save('target',target);print('partition target',target['status'],flush=True)
if target['status']=='sat':save('target-second-witness',e.solve(row['plaintext'],row['ciphertext'],rank_partition=True,rank_cap=8,blocked_keys=target['keys'],verbose=True))
