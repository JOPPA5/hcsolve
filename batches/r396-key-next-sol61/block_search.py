from pathlib import Path
from block_cp import solve
import json,random,sys
B=Path(__file__).resolve().parent;j=int(sys.argv[1]);truth=json.loads((B/'controls-truth.json').read_text())[j];p=truth['plaintext'];c=truth['ciphertext'];current=json.loads((B/f'cp-lns-control{j}.json').read_text());best=current['matches'];keys=current['keys'];rng=random.Random(396300+j);rows=[]
for it in range(40):
 windows=[]
 for w in [21,19,20]:
  width=7+it%4;at=rng.randrange(w-width+1);windows.append([at,at+width])
 r=solve(p,c,1.5,hints=keys,soft=True,windows=windows);r['windows']=windows;r['iteration']=it;rows.append(r)
 if r.get('matches',0)>best:
  best=r['matches'];keys=r['keys'];(B/f'block-best{j}.json').write_text(json.dumps(r,indent=2)+'\n');print(it,best,flush=True)
 if best==50:break
(B/f'block-results{j}.json').write_text(json.dumps(rows,indent=2)+'\n');print('final',j,best,flush=True)
