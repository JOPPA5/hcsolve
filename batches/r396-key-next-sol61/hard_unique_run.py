from hard_unique_cp import solve
from pathlib import Path
import json,sys
B=Path(__file__).resolve().parent;j=int(sys.argv[1]);p,c=(B/f'control{j}.txt').read_text().split();candidates=[]
def assess(ks,source):
 if [len(k)for k in ks]!=[21,19,20]:return
 x=p
 for k in ks:x=''.join(x[i]for col in k for i in range(col,len(x),len(k)))
 unique=[ch for ch in set(p)if p.count(ch)==1]
 if not all(x.index(ch)==c.index(ch)for ch in unique):return
 candidates.append(dict(keys=ks,source=source,matches=sum(a==b for a,b in zip(x,c))))
for name in [f'control{j}-result.txt',f'middle-control{j}-result.txt',f'coordinate-control{j}-result.txt',f'hybrid-control{j}-result.txt',f'fragment-control{j}-result.txt']:
 path=B/name
 if path.exists():assess([list(map(int,s.split()))for s in path.read_text().splitlines()[1:4]],name)
for name in [f'cp-lns-control{j}.json',f'error-best{j}.json',f'error-results{j}.json',f'rank-bridge-results{j}.json',f'block-results{j}.json']:
 path=B/name
 if path.exists():
  data=json.loads(path.read_text());rows=data if isinstance(data,list)else[data]
  for index,r in enumerate(rows):
   if'keys'in r:assess(r['keys'],name+':'+str(index))
assert candidates,'no generic healthy-unique seed';seed=max(candidates,key=lambda r:r['matches']);(B/f'hard-unique-seed{j}.json').write_text(json.dumps({'selected':seed,'selection':'known PT/CT unique endpoints hard; then highest known-pair Hamming; no planted-key comparison','permitted_sources_only':True},indent=2)+'\n');r=solve(p,c,40,hints=seed['keys'],max_errors=50-seed['matches']);r.update(seed=seed,unique_endpoints_hard=True);(B/f'hard-unique-control{j}.json').write_text(json.dumps(r,indent=2)+'\n');print(j,seed['matches'],r['status'],r.get('matches'),flush=True)
