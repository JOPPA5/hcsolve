from pathlib import Path
import random,json
from rank_prefix import solve,enc
P=Path(__file__).parent;q='nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcislox';log=P/'rank-prefix-control-results.jsonl'
for w in [21,22,17,18,19,20]:
 rng=random.Random(6103642200+w);ks=[];ct=q+'r'
 for _ in range(3):
  k=rng.sample(range(1,w),w-1);k.insert(10,0);ks.append(k);ct=enc(ct,k)
 out=solve(q+'r',ct,[w]*3,60000,0,[11]*3,backend='eager');out.update(mode='matched_rank_prefix_control',alignments=[11]*3,planted_keys=ks,plaintext=q+'r',ciphertext=ct,keys_equal_planted=out.get('keys')==ks)
 with log.open('a') as f:f.write(json.dumps(out)+'\n')
 print(w,out['status'],round(out['seconds'],3),flush=True)
