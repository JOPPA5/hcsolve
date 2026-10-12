from pathlib import Path
from itertools import permutations,product
import random,json
from exact_cover_insert import solve
b=Path(__file__).resolve().parent;base='abcuvd';rng=random.Random(364161333);rows=[];total=0
for n in [1,2,3]:
 orders=[k for k in permutations(range(3))if k.index(0)==n-1];possible=set()
 for insertion in range(7):
  p=base[:insertion]+'x'+base[insertion:]
  for keys in product(orders,repeat=3):
   c=p
   for k in keys:c=''.join(c[i]for col in k for i in range(col,len(c),len(k)))
   possible.add(c);total+=1
 for i in range(6):
  c=rng.choice(sorted(possible))if i<3 else ''.join(rng.sample(list(base+'x'),7));a=list(c);u=c.index('u');v=c.index('v');a[u],a[v]=a[v],a[u];alt=''.join(a);variants=[c,alt];expected=any(v in possible for v in variants)
  r=solve('?'*7,c,[3]*3,3000,alignments=[n]*3,backend='eager',insert_x_template=base,cipher_variants=variants);assert r['status']!='unknown'and(r['status']=='sat')==expected;rows.append(dict(alignment=n,variants=variants,exhaustive_expected=expected,result=r))
(b/'small-exhaustive-audit.json').write_text(json.dumps(dict(independently_enumerated_insertion_keysets=total,cases=rows),indent=2)+'\n');print('All18 cases match independent enumeration of168 insertion/keysets.')
