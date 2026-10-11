from pathlib import Path
import json,sys
B=Path(__file__).resolve().parent;R=B.parents[1];data=json.load(open(sys.argv[1]));paths=Path(sys.argv[2]).read_text().splitlines()[1:];lines=Path(sys.argv[3]).read_text().splitlines();label=sys.argv[4];geom=json.loads((R/'batches/kryha-wheel-sol61/wheel52.json').read_text());co=geom['unwrapped_effective_coordinates'];adj=geom['adjacent_distances'];out=[]
for pos,line in enumerate(lines):
 if not line.startswith('N '):continue
 n=int(line.split()[1]);v=lines[pos+1].split();rank=int(v[1]);P=list(map(int,lines[pos+2].split()));row=paths[rank].split();A=list(map(int,row[1::2]));BB=list(map(int,row[2::2]));h=[A,[BB[-1]]+BB[:-1]];beta=(data['K'][0]-(co[BB[0]]-co[BB[-1]])%179)%26;pts=[];jumps=[]
 for mask in h:
  j=[]
  for a,b in zip(mask,mask[1:]+mask[:1]):
   x=a;val=0
   while True:
    val+=adj[x];x=(x+1)%52
    if x==b:break
   j.append(val)
  assert sum(j)==179;jumps.append(j)
 assert [(jumps[1][(j+1)%23]-jumps[0][j])%26 for j in range(23)]==data['delta']
 for q,ct in enumerate(data['ciphertexts']):
  d=beta if q else 0;pt=''
  for i,c in enumerate(ct):pt+=chr(97+P[(data['O'][ord(c)-97]-d)%26]);d=(d+jumps[q][i%23])%26
  pts.append(pt);ip={x:i for i,x in enumerate(P)};io={x:i for i,x in enumerate(data['O'])};d=beta if q else 0;enc=''
  for i,c in enumerate(pt):enc+=chr(97+io[(ip[ord(c)-97]+d)%26]);d=(d+jumps[q][i%23])%26
  assert enc==ct
 out.append(dict(n=n,path_rank=rank+1,P=P,O=data['O'],masks=h,beta=beta,plaintexts=pts,full_reencryption_exact=True,delta_exact=True))
(B/f'{label}-full.json').write_text(json.dumps(out,indent=2));print([(x['n'],x['path_rank'],x['beta'])for x in out])
if len(sys.argv)>5:
 truth=json.load(open(sys.argv[5]));checks=[dict(n=x['n'],plaintext_exact=x['plaintexts']==truth['plaintexts'],matches=[sum(a==b for a,b in zip(p,t))for p,t in zip(x['plaintexts'],truth['plaintexts'])])for x in out];(B/f'{label}-verification.json').write_text(json.dumps(checks,indent=2));print(checks)
