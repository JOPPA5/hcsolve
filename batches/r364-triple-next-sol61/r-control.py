from pathlib import Path
import json,random
from direct import solve
b=Path(__file__).resolve().parent;v=json.loads(Path('batches/r364-review-collation-sol61/variants.json').read_text());base=v['four_sentence_X_template64'];rng=random.Random(364231133);at=rng.randrange(65);p=base[:at]+'x'+base[at:];n=rng.randrange(1,20);keys=[]
for w in [21,19,20]:
 k=rng.sample(range(1,w),w-1);k.insert(n-1,0);keys.append(k)
c=p
for k in keys:c=''.join(c[i]for col in k for i in range(col,len(c),len(k)))
(b/'r-control-input.json').write_text(json.dumps(dict(plaintext=p,ciphertext=c,widths=[21,19,20],common_unknown_alignment=True),indent=2)+'\n');(b/'r-control-truth.json').write_text(json.dumps(dict(keys=keys,alignment=n,extra_x=at),indent=2)+'\n');r=solve(p,c,seconds=60,reverse_support=True,common_rank=True)
if r['status']=='sat':
 x=c
 for k in r['keys'][::-1]:
  a=['']*len(x);z=0
  for col in k:
   for i in range(col,len(x),len(k)):a[i]=x[z];z+=1
  x=''.join(a)
 assert x==p;r['independent_inverse_full65']=True
(b/'r-control-result.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
