from pathlib import Path
import json,random
from direct import solve
b=Path(__file__).resolve().parent
# Fresh arbitrary full-alphabet65 plaintext, not historical quote; only pair enters search.
rng=random.Random(364231111);p=''.join(rng.sample('abcdefghijklmnopqrstuvwxyz',26))+''.join(rng.choice('abcdefghijklmnopqrstuvwxyz')for _ in range(39));keys=[rng.sample(range(w),w)for w in [21,19,20]]
c=p
# Independent explicit positional-index encoder.
for k in keys:c=''.join(c[pos]for col in k for pos in range(col,len(c),len(k)))
(b/'control-input.json').write_text(json.dumps(dict(plaintext=p,ciphertext=c,widths=[21,19,20]),indent=2)+'\n');(b/'control-truth.json').write_text(json.dumps(dict(keys=keys),indent=2)+'\n')
r=solve(p,c,seconds=60)
if r['status']=='sat':
 x=c
 for k in r['keys'][::-1]:
  arr=['']*len(x);at=0
  for col in k:
   for i in range(col,len(x),len(k)):arr[i]=x[at];at+=1
  x=''.join(arr)
 assert x==p;r['independent_inverse_full65']=True
(b/'control-result.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2),flush=True)
