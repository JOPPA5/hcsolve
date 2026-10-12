from itertools import permutations,product
from pathlib import Path
import random,json
from closed import solve
b=Path(__file__).resolve().parent;p='abcabcde';width=3;rng=random.Random(36421334);rows=[];count=0
for progressive in [False,True]:
 reachable=set()
 for keys in product(list(permutations(range(width))),repeat=3):
  ranks=[k.index(0)for k in keys]
  if progressive:
   if ranks!=[ranks[0],ranks[0]+1,ranks[0]+2]:continue
  elif len(set(ranks))!=1:continue
  count+=1;c=p
  for k in keys:c=''.join(c[i]for col in k for i in range(col,len(c),width))
  reachable.add(c)
 for i in range(10):
  c=rng.choice(sorted(reachable))if i<5 else ''.join(rng.sample(list(p),len(p)));r=solve(p,[c],width,progressive,seconds=3);expected=c in reachable;assert r['status']!='UNKNOWN'and(r['status']in ['OPTIMAL','FEASIBLE'])==expected;rows.append(dict(progressive=progressive,ciphertext=c,exhaustive_expected=expected,result=r))
(b/'small-exhaustive-audit.json').write_text(json.dumps(dict(admissible_key_triples=count,cases=rows),indent=2)+'\n');print('20 cases agree with all32 admissible common/progressive triples.')
