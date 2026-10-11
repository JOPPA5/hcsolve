from pathlib import Path
from exact_cover_insert import solve
import json
B=Path(__file__).resolve().parent;data=json.loads((B/'variants.json').read_text());p=data['four_sentence_X_template64']+'x';variants=[v['omit3']for v in data['variants']if v['name']in['EXCUV','EXCVU']];rows=[]
for mode,alignment in [('constant',[11,11,11]),('progressive',[11,12,13])]:
 r=solve(p,variants[0],[21,19,20],20000,alignments=alignment,backend='eager',cipher_variants=variants);r.update(mode=mode,n=11,alignment=alignment,subset='fifthX at suffix; unrestricted insertion main37cases continues independently',fifth_x_boundary=64,known_key_seed=False,quote_is_conditional=True);rows.append(r);(B/'suffix-priority-subset.json').write_text(json.dumps(rows,indent=2));print(mode,r['status'],r['seconds'],flush=True)
