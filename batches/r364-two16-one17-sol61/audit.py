from pathlib import Path
from itertools import permutations,product
import random,json
from engine import solve
B=Path(__file__).resolve().parent;p='abcuvdx';widths=(3,3,4);legal=[]
for keys in product(*(list(permutations(range(w)))for w in widths)):
 if len(set(k.index(0)for k in keys))!=1:continue
 c=p
 for key in keys:c=''.join(c[i]for col in key for i in range(col,len(c),len(key)))
 legal.append((keys,c))
possible={c for _,c in legal};rng=random.Random(3641616173);cases=[]
for i in range(24):
 c=rng.choice(sorted(possible))if i<12 else''.join(rng.sample(list(p),len(p)));a=list(c);u=c.index('u');v=c.index('v');a[u],a[v]=a[v],a[u];variants=[c,''.join(a)];expected=any(v in possible for v in variants)
 r=solve(p,variants,widths=widths,seconds=5);assert r['status']!='unknown'and(r['status']=='sat')==expected
 if r['status']=='sat':
  pred=p
  for key in r['keys']:pred=''.join(pred[i]for col in key for i in range(col,len(pred),len(key)))
  assert pred==r['selected_ciphertext']
 cases.append(dict(variants=variants,enumerated_expected=expected,result=r))
(B/'audit.json').write_text(json.dumps(dict(all_key_triples=864,legal_common_alignment_triples=len(legal),cases=cases),indent=2)+'\n');print('24 cases agree against',len(legal),'legal triples')
