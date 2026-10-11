from pathlib import Path
import random,json
from exact_cover import solve,enc
P=Path(__file__).parent;w=21;q='nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcisloxr';rng=random.Random(6103642200+w);ks=[];ct=q
for _ in range(3):
 k=rng.sample(range(1,w),w-1);k.insert(10,0);ks.append(k);ct=enc(ct,k)
out=solve(q,ct,[w]*3,60000,0,[11]*3,backend='eager',explicit_vocab=True);out.update(mode='matched_explicit_vocabulary_control',planted_keys=ks,keys_equal_planted=out.get('keys')==ks,plaintext=q,ciphertext=ct);(P/'vocab-control21.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
