from pathlib import Path
import random,json
from exact_cover import solve,enc
quote='nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcislox';p=quote+'r';rng=random.Random(610364892)
results=[]
for widths in [[16,17],[13,13,13]]:
 ks=[rng.sample(range(w),w) for w in widths];c=p
 for k in ks:c=enc(c,k)
 out=solve(p,c,widths,20000);out.update(planted_keys=ks,plaintext=p,ciphertext=c,keys_equal_planted=out.get('keys')==ks,control=True);results.append(out);print(json.dumps(out),flush=True)
Path(__file__).with_name('quote-control-results.json').write_text(json.dumps(results,indent=2)+'\n')
