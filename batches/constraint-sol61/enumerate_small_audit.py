from pathlib import Path
from itertools import permutations,product
from collections import Counter
import json,time
P=Path(__file__).parent;q='nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcislox';gs=(P.parents[1]/'ciphers/hcp-364/work/transcription.txt').read_text().split();rows=[]
for w in range(2,5):
 orders=list(permutations(range(w)));maps=[sum((list(range(col,65,w)) for col in key),[]) for key in orders]
 for errors in [0,3]:
  g=gs[:]
  if not errors:g[7]='tsnnd';g[9]='eloen';g[11]='ercuv'
  c=''.join(x for i,x in enumerate(g) if i!=2);excess=Counter(c)-Counter(q);fillers=list(excess);minimum=65;witness=None;tested=0;t=time.monotonic()
  for a,b,d in product(maps,repeat=3):
   composed=[a[b[d[i]]] for i in range(65)];fillerposition=composed.index(64);fixed=sum(q[j]!=c[i] for i,j in enumerate(composed) if j!=64);distance=fixed+(c[fillerposition] not in fillers);minimum=min(minimum,distance);tested+=1
   if distance<=errors:witness=composed;break
  rows.append(dict(width=w,reading='raw' if errors else 'glyph',error_bound=errors,keys_tested=tested,total_keysets=len(orders)**3,minimum_distance=minimum,admissible_fillers=fillers,witness=witness,status='unsat' if witness is None else 'sat',seconds=time.monotonic()-t))
(P/'enumerate-small-audit.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows))
