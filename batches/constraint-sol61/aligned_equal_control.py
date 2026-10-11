from pathlib import Path
import json,random
from exact_cover import solve,enc
p='nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcisloxr';rng=random.Random(6103641616);ws=[16,16,16];ns=[11,11,11];keys=[];c=p
for w,n in zip(ws,ns):
 k=rng.sample(range(1,w),w-1);k.insert(n-1,0);keys.append(k);c=enc(c,k)
out=solve(p,c,ws,20000,0,ns);out.update(mode='independent_aligned_equal_width_control',alignments=ns,planted_keys=keys,plaintext=p,ciphertext=c,keys_equal_planted=out.get('keys')==keys);Path(__file__).with_name('aligned-equal-control.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
