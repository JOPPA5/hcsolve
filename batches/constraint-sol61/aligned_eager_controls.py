from pathlib import Path
import random,json
from exact_cover import solve,enc
P=Path(__file__).parent;q='nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcislox';p=q+'r';rng=random.Random(610364110);results=[]
for alignment in [[11,11,11],[11,12,13]]:
 ws=[16,17,18];ks=[];c=p
 for w,n in zip(ws,alignment):
  k=rng.sample(list(range(1,w)),w-1);k.insert(n-1,0);ks.append(k);c=enc(c,k)
 out=solve(p,c,ws,60000,0,alignment,backend="eager");out.update(mode='independent_aligned_triple_control',alignments=alignment,planted_keys=ks,plaintext=p,ciphertext=c,keys_equal_planted=out.get('keys')==ks);results.append(out);print(json.dumps(out),flush=True)
(P/'aligned-eager-control-results.json').write_text(json.dumps(results,indent=2)+'\n')
