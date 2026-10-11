from pathlib import Path
import random,json
from exact_cover import solve,enc
P=Path(__file__).parent;p=('kontrolnytextjeuplnenezavislyodhistorickehozadaniapoznameceleslovatentorazpreverujemedlhsitextktorymaodlisnerozlozeniepismennaoverenieprogramu')*3;p=p[:280];rng=random.Random(61028016);ws=[16,17,18];ks=[rng.sample(range(w),w) for w in ws];c=p
for k in ks:c=enc(c,k)
out=solve(p,c,ws,20000);out.update(mode='independent_long_triple_control',planted_keys=ks,plaintext=p,ciphertext=c,keys_equal_planted=out.get('keys')==ks);(P/'long-triple-control.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
