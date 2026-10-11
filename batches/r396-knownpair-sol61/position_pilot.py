from position_model import solve
from pathlib import Path
import json,concurrent.futures
B=Path(__file__).resolve().parent;controls=json.loads((B/'fresh-controls.json').read_text())
def run(c):
 r=solve(c['plaintext'],c['ciphertext'],timeout=30000);r.update(control=c,blind=True);(B/f"position-{c['label']}.json").write_text(json.dumps(r,indent=2)+'\n');return r
if __name__=='__main__':
 c=controls[0];r=solve(c['plaintext'],c['ciphertext'],known_keys=c['planted_keys'],timeout=5000);assert r['status']=='sat';(B/'position-known-key.json').write_text(json.dumps(r,indent=2)+'\n')
 with concurrent.futures.ProcessPoolExecutor(max_workers=2)as pool:
  for r in pool.map(run,controls):print(r['control']['label'],r['status'],r['seconds'],flush=True)
