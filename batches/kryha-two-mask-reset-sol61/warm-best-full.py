from pathlib import Path
import json
b=Path(__file__).resolve().parent;w=json.load(open('batches/kryha-wheel-sol61/wheel52.json'));co=w['unwrapped_effective_coordinates'];adj=w['adjacent_distances'];out=[]
for variant in ('pixel-strong','pixel-strong-plus-moderate'):
 name=variant+'-row5';inp=json.load(open(b/f'{name}-input.json'));profiles=(b/f'{name}-warm-profile.txt').read_text().splitlines();ls=(b/f'{name}-warm-reranked.txt').read_text().splitlines()
 for i,line in enumerate(ls):
  if not line.startswith('N '):continue
  ng=int(line.split()[1]);score,index,a,bb=ls[i+1].split();P=list(map(int,ls[i+2].split()));v=profiles[int(index)+1].split();h=[list(map(int,v[q::2])) for q in (1,2)];arc=(co[h[1][0]]-co[h[1][-1]]+(179 if h[1][0]<h[1][-1] else 0));beta=(inp['K'][0]-arc)%26;assert beta==0;h[1]=h[1][-1:]+h[1][:-1];pts=[];encoded=[];ip={x:j for j,x in enumerate(P)};io={x:j for j,x in enumerate(inp['O'])}
  for side in (0,1):
   hs=h[side];pt=''
   for j,c in enumerate(inp['ciphertexts'][side]):
    d=co[hs[j%23]]-co[hs[0]]+(179 if hs[j%23]<hs[0] else 0)+179*(j//23)
    pt+=chr(97+P[(inp['O'][ord(c)-97]-d)%26])
   pts.append(pt);d=0;ct=''
   for j,c in enumerate(pt):
    ct+=chr(97+io[(ip[ord(c)-97]+d)%26]);x=hs[j%23];end=hs[(j+1)%23]
    while True:
     d=(d+adj[x])%26;x=(x+1)%52
     if x==end:break
   encoded.append(ct)
  assert encoded==inp['ciphertexts'];assert pts[0][:-1]==ls[i+3] and pts[1][1:]==ls[i+4];out.append(dict(variant=variant,ngram=ng,score=float(score),profile_rank=int(index)+1,P=P,O=inp['O'],masks=h,beta=beta,plaintexts=pts,full355_literal_reencryption_exact=True,unreviewed_near_plaintext=True))
(b/'warm-best-full.json').write_text(json.dumps(out,indent=2)+'\n');print('Verified warm keys',len(out))
