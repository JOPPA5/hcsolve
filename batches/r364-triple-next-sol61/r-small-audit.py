from pathlib import Path
from itertools import permutations
from direct import solve
import random,json
b=Path(__file__).resolve().parent;rng=random.Random(364321445);p='abcabca';widths=[2,3,4];reachable=set()
for keys in __import__('itertools').product(*(list(permutations(range(w)))for w in widths)):
 if len({k.index(0)for k in keys})!=1:continue
 t=p
 for k in keys:t=''.join(t[i]for col in k for i in range(col,len(t),len(k)))
 reachable.add(t)
rows=[]
for i in range(20):
 c=rng.choice(sorted(reachable))if i<10 else ''.join(rng.sample(list(p),len(p)));r=solve(p,c,widths,seconds=3,reverse_support=True,common_rank=True);expected=c in reachable;assert (r['status']=='sat')==expected and r['status']!='unknown';rows.append(dict(ciphertext=c,expected=expected,result=r))
(b/'r-small-audit.json').write_text(json.dumps(dict(all24_common_rank_triples_exhaustively_enumerated=True,reachable_ciphertexts=len(reachable),cases=rows),indent=2)+'\n');print('20 small cases agree with all24 independently enumerated key triples.')
