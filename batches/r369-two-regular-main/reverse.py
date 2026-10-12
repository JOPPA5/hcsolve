"""Separate changed-model calibration. Preserve forward-only timeouts."""
from pathlib import Path
import json,sys
from engine import run
b=Path(__file__).resolve().parent
truth=json.loads((b/'control-truth.json').read_text())
def callback(name):
    def fn(result):
        (b/(name+'.json')).write_text(json.dumps(result,indent=2)+'\n');r=result['rows'][-1]
        print(name,r['n'],r['status'],round(r['seconds'],2),flush=True)
    return fn
control=run(truth['plaintext'],truth['observed_ciphertext'],cap=8,bidirectional=True,on_row=callback('reverse-control'))
if not any(row['status']=='sat' for row in control['rows']):
    print('No full blind control recovery; actual target gated off',flush=True);sys.exit(0)
rows=json.loads(Path('batches/repeat369-365-sol61/closest-inventory.json').read_text());cases={row['plaintext']:row for row in rows}
for j,case in enumerate(cases.values()):
    run(case['plaintext'],case['ciphertext'],cap=15,bidirectional=True,on_row=callback('reverse-target'+str(j)))
