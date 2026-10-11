from pathlib import Path
import json
b=Path(__file__).resolve().parent;r=b.parents[1];geom=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'));co=geom['unwrapped_effective_coordinates'];adj=geom['adjacent_distances'];checks=[]
for variant in ('pixel-strong','pixel-strong-plus-moderate'):
 for ix in (5,6):
  name=f'{variant}-row{ix}';inp=json.load(open(b/f'{name}-input.json'));prof=(b/f'{name}-profile.txt').read_text().splitlines();l=(b/f'{name}-masc.txt').read_text().splitlines();out=[]
  for k in range(0,len(l),4):
   index,score=l[k].split();v=prof[int(index)+1].split();h=[list(map(int,v[q::2])) for q in (1,2)];arc=(co[h[1][0]]-co[h[1][-1]]+(179 if h[1][0]<h[1][-1] else 0));beta=(inp['K'][0]-arc)%26;h[1]=h[1][-1:]+h[1][:-1];P=list(map(int,l[k+1].split()));O=inp['O'];pts=[];reen=[]
   for side in (0,1):
    holes=h[side];pt=''
    for i,c in enumerate(inp['ciphertexts'][side]):
     d=co[holes[i%23]]-co[holes[0]]+(179 if holes[i%23]<holes[0] else 0)+179*(i//23)+(beta if side else 0)
     pt+=chr(97+P[(O[ord(c)-97]-d)%26])
    pts.append(pt);ip={x:i for i,x in enumerate(P)};io={x:i for i,x in enumerate(O)};d=beta if side else 0;ct=''
    for i,c in enumerate(pt):
     ct+=chr(97+io[(ip[ord(c)-97]+d)%26]);x=holes[i%23];end=holes[(i+1)%23]
     while True:
      d=(d+adj[x])%26;x=(x+1)%52
      if x==end:break
    reen.append(ct)
   assert reen==inp['ciphertexts'];assert pts[0][:-1]==l[k+2] and pts[1][1:]==l[k+3];out.append(dict(profile_rank=int(index)+1,score=float(score),P=P,O=O,masks=h,beta=beta,plaintexts=pts,full_body_reencryption_exact=True,omitted30_each_undecoded=True))
  out.sort(key=lambda x:x['score'],reverse=True);(b/f'{name}-full-candidates.json').write_text(json.dumps(out,indent=2)+'\n');checks.append(dict(name=name,candidates=len(out),physical_body_inverse_and_reencryption_exact=True,best_score=out[0]['score'],best_rank=out[0]['profile_rank']))
(b/'actual-verification.json').write_text(json.dumps(checks,indent=2)+'\n');print(checks)
