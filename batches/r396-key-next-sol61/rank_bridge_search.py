from rank_bridge import solve
from pathlib import Path
import json,random,sys
B=Path(__file__).resolve().parent;j=int(sys.argv[1]);tr=json.loads((B/'controls-truth.json').read_text())[j];p=tr['plaintext'];c=tr['ciphertext'];extraPath=B/f'error-best{j}.json'
if extraPath.exists():seed=json.loads(extraPath.read_text());keys=seed['keys'];best=seed['matches']
else:
 lines=(B/f'coordinate-control{j}-result.txt').read_text().splitlines();keys=[list(map(int,x.split()))for x in lines[1:4]];best=int(lines[0])
rng=random.Random(396900+j);rows=[]
def support(keys):
 maps=[]
 for k in keys:
  d=[0]*50;at=0
  for col in k:
   for i in range(col,50,len(k)):d[i]=at;at+=1
  maps.append(d)
 free=[set()for _ in range(3)]
 for i in range(50):
  path=[i];n=i
  for d in maps:n=d[n];path.append(n)
  if p[i]!=c[n]:
   for stage,w in enumerate([21,19,20]):free[stage].add(path[stage]%w)
 return free
for it in range(24):
 free=support(keys)
 for stage,w in enumerate([21,19,20]):
  for _ in range(it%4):free[stage].add(rng.randrange(w))
 r=solve(p,c,2,hints=keys,free_columns=free,max_errors=50-best);r.update(iteration=it,free_columns=[sorted(s)for s in free]);rows.append(r)
 if r.get('matches',0)>best:
  best=r['matches'];keys=r['keys'];(B/f'rank-bridge-best{j}.json').write_text(json.dumps(r,indent=2)+'\n');print(it,best,[len(s)for s in free],flush=True)
 if best==50:break
(B/f'rank-bridge-results{j}.json').write_text(json.dumps(rows,indent=2)+'\n');print('final',j,best,flush=True)
