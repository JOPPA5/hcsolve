from pathlib import Path
import json,random
from closed import solve
b=Path(__file__).resolve().parent;v=json.loads(Path('batches/r364-review-collation-sol61/variants.json').read_text());p=v['four_sentence_X_template64']+'x';rng=random.Random(364211223);n=rng.randrange(1,22);keys=[];c=p
for _ in range(3):
 k=rng.sample(range(1,21),20);k.insert(n-1,0);keys.append(k);c=''.join(c[i]for col in k for i in range(col,len(c),21))
(b/'control-input.json').write_text(json.dumps(dict(plaintext=p,ciphertext=c,width=21,common_unknown_alignment=True),indent=2)+'\n');(b/'control-truth.json').write_text(json.dumps(dict(keys=keys,alignment=n),indent=2)+'\n');r=solve(p,[c],seconds=60);(b/'control-result.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
