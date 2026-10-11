from pathlib import Path
import json,random
from exact_cover import solve,enc
p=Path(__file__).resolve().parent;rng=random.Random(364211920611);plain='kontrolamusiostatnezavislapreovereniekazdehodennehozaciatkutranspozic'[:65];assert len(plain)==65
for mode,ns in [('constant',range(1,20)),('progressive',range(1,19))]:
 for n in ns:
  align=[n]*3 if mode=='constant'else[n,n+1,n+2];keys=[];ct=plain
  for w,kpos in zip([21,19,20],align):
   k=list(range(1,w));rng.shuffle(k);k.insert(kpos-1,0);keys.append(k);ct=enc(ct,k)
  r=solve(plain,ct,[21,19,20],3000,alignments=align,known_keys=keys,backend='eager');r.update(mode=mode,n=n,alignment=align,plaintext=plain,ciphertext=ct,planted_keys=keys)
  with(p/'all-alignment-encoding-checks.jsonl').open('a')as f:f.write(json.dumps(r)+'\n')
  assert r['status']=='sat'
print('All 37 independently planted known-key encoding checks passed; these are not blind key recovery.')
