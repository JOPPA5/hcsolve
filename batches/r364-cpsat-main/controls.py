from solve import solve,enc
from pathlib import Path
import random,json
P=Path(__file__).parent;rng=random.Random(364611211);p='nezavislykontrolnytelegramoverujepresnosttrojitehoprehadzovaniapismenx'[:65];rows=[]
for widths,align in [([8,9],[4,5]),([21,19,20],[7,7,7])]:
 keys=[]
 for w,n in zip(widths,align):
  k=list(range(1,w));rng.shuffle(k);k.insert(n-1,0);keys.append(k)
 ct=p
 for k in keys:ct=enc(ct,k)
 for known in [True,False]:
  r=solve(p,ct,widths,3 if known else 60,alignments=align,known_keys=keys if known else None);r.update(stage='known-key-consistency' if known else 'fresh-blind-control',plaintext=p,ciphertext=ct,planted_keys=keys);rows.append(r);(P/'controls.json').write_text(json.dumps(rows,indent=2));print(widths,r['stage'],r['status'],r['seconds'],flush=True)
  if known:assert r['status'] in ['OPTIMAL','FEASIBLE']
