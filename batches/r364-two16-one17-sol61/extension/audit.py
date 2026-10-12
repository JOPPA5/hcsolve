from pathlib import Path
from itertools import permutations,product
import random,json,importlib.util
B=Path(__file__).resolve().parent;sp=importlib.util.spec_from_file_location('audit_engine',B.parent/'engine.py');e=importlib.util.module_from_spec(sp);sp.loader.exec_module(e)
p='abcuvdx';rng=random.Random(3641616223);cases=[]
for w in[5,6]:
 widths=(3,3,w);legal=[]
 for keys in product(*(list(permutations(range(x)))for x in widths)):
  if len(set(k.index(0)for k in keys))!=1:continue
  c=p
  for key in keys:c=''.join(c[i]for col in key for i in range(col,len(c),len(key)))
  legal.append(c)
 possible=set(legal)
 for i in range(12):
  c=rng.choice(sorted(possible))if i<6 else''.join(rng.sample(list(p),7));a=list(c);u=c.index('u');v=c.index('v');a[u],a[v]=a[v],a[u];variants=[c,''.join(a)];expected=any(v in possible for v in variants)
  r=e.solve(p,variants,widths=widths,seconds=5);assert r['status']!='unknown'and(r['status']=='sat')==expected
  if r['status']=='sat':
   x=p
   for key in r['keys']:x=''.join(x[i]for col in key for i in range(col,len(x),len(key)))
   assert x==r['selected_ciphertext']
  cases.append(dict(widths=widths,enumerated_legal_keysets=len(legal),expected=expected,result=r))
save=json.dumps(cases,indent=2)+'\n';(B/'audit.json').write_text(save);print('24 additional ragged-third cases agree')
