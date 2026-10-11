from exact_cover_insert import solve,enc
from pathlib import Path
import json,random
B=Path(__file__).resolve().parent;rng=random.Random(364121200);base=''.join(rng.choice('abcdefghijklmnopqrstuvwxyz')for _ in range(64));keys=[rng.sample(range(w),w)for w in [5,6]];rows=[]
for at in [0,64]:
 plain=base[:at]+'x'+base[at:];cipher=plain
 for key in keys:cipher=enc(cipher,key)
 r=solve('?'*65,cipher,[5,6],5000,known_keys=keys,backend='eager',insert_x_template=base);assert r['status']=='sat'and r['conditional_plaintext']==plain;r.update(true_insertion_boundary=at,control_plaintext=plain,source_template=base,full_recovery_exact=True);rows.append(r)
(B/'endpoint-insertion-controls.json').write_text(json.dumps(rows,indent=2));print('PASS extraX first/last boundary exact encoding checks')
