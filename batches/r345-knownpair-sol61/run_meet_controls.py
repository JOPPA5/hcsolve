from pathlib import Path
import json,concurrent.futures
from meet_model import solve
B=Path(__file__).resolve().parent
def run(label):
 c=json.loads((B/f'{label}.json').read_text());r=solve(c['plaintext'],c['ciphertext'],timeout=60000);r.update(control_label=label,known_keys_not_supplied=True,planted_keys=c['planted_keys']);(B/f'meet-{label}.json').write_text(json.dumps(r,indent=2));return label,r['status'],r['seconds']
if __name__=='__main__':
 with concurrent.futures.ProcessPoolExecutor(max_workers=2)as pool:
  for r in pool.map(run,['matched_inventory_shuffled60','independent_TEST60']):print(r,flush=True)
