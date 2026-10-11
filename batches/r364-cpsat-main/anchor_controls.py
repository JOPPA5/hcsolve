from anchor_engine import solve,enc
from pathlib import Path
import json,random
P=Path(__file__).parent;controls=[r for r in json.loads((P/'controls.json').read_text()) if r['stage']=='fresh-blind-control' and len(r['widths'])==3];quote=json.loads(Path('batches/constraint-sol61/target-cases.json').read_text())['template'][:-1];rng=random.Random(364621502);ks=[]
for w in [21,19,20]:
 k=list(range(1,w));rng.shuffle(k);k.insert(4,0);ks.append(k)
pt=quote+'r';ct=pt
for k in ks:ct=enc(ct,k)
controls.append(dict(plaintext=pt,ciphertext=ct,planted_keys=ks,widths=[21,19,20],alignments=[5,5,5]));rows=[]
for c in controls:
 r=solve(c['plaintext'],c['ciphertext'],c['widths'],seconds=60,alignments=c['alignments']);r.update(stage='unique-coordinate-blind-control',fixture=c,truth_keys_used_for_search=False);rows.append(r);(P/'anchor-controls.json').write_text(json.dumps(rows,indent=2));print(r['status'],r['seconds'],flush=True)
