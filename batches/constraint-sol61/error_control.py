from pathlib import Path
import json,random
from exact_cover import solve,enc
q='nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcislox';p=q+'r';rng=random.Random(610364995);ws=[16,17];ks=[rng.sample(range(w),w) for w in ws];c=p
for k in ks:c=enc(c,k)
damaged=list(c)
for i in [5,21,44]:damaged[i]=chr((ord(damaged[i])-97+1)%26+97)
out=solve(q+'?',''.join(damaged),ws,20000,3);out.update(mode='independent_unknown_filler_3_error_control',planted_keys=ks,true_plaintext=p,undamaged_ciphertext=c,damaged_ciphertext=''.join(damaged),keys_equal_planted=out.get('keys')==ks,undamaged_re_encryption_exact=out.get('predicted_ciphertext')==c);Path(__file__).with_name('error-control.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
