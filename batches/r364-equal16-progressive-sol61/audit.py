from pathlib import Path
from itertools import permutations,product
from collections import Counter
import random,json
from exact_cover_insert import solve
b=Path(__file__).resolve().parent;base='abcuvd';rng=random.Random(364161995);orders=[[k for k in permutations(range(3))if k.index(0)==j]for j in range(3)];reachable=set();total=0
for insertion in range(7):
 p=base[:insertion]+'x'+base[insertion:]
 for keys in product(*orders):
  c=p
  for k in keys:c=''.join(c[i]for col in k for i in range(col,len(c),len(k)))
  reachable.add(c);total+=1
rows=[]
for i in range(20):
 c=rng.choice(sorted(reachable))if i<10 else ''.join(rng.sample(list(base+'x'),7));a=list(c);u=c.index('u');v=c.index('v');a[u],a[v]=a[v],a[u];alt=''.join(a);variants=[c,alt];expected=any(x in reachable for x in variants);r=solve('?'*7,c,[3]*3,3000,alignments=[1,2,3],backend='eager',insert_x_template=base,cipher_variants=variants);assert r['status']!='unknown'and(r['status']=='sat')==expected;rows.append(dict(variants=variants,exhaustive_expected=expected,result=r))
(b/'small-exhaustive-audit.json').write_text(json.dumps(dict(insertion_keysets=total,progressive_no_wrap=True,cases=rows),indent=2)+'\n');print('20 progressive UV/unknownX cases agree with all56 independently enumerated insertion/keysets.')
