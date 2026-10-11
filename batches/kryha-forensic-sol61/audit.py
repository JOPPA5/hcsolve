from pathlib import Path
import json
b=Path(__file__).resolve().parent;r=json.load(open('batches/kryha-two-mask-refine-sol61/actual-row5-pure6-r7-full.json'))[0];co=json.load(open('batches/kryha-wheel-sol61/wheel52.json'))['unwrapped_effective_coordinates'];adj=json.load(open('batches/kryha-wheel-sol61/wheel52.json'))['adjacent_distances'];cts=[''.join(c.lower() for c in Path(f'batches/kryha-shift23-sol61/{n}-pixel-strong.txt').read_text() if c.isalpha())[20:375] for n in (350,351)];rows=[]
for filename in ('generic325.txt','rare120-plus325.txt'):
 ls=(b/filename).read_text().splitlines();i=0;ng=0;rank=0
 while i<len(ls):
  if ls[i].startswith('N '):ng=int(ls[i].split()[1]);rank=0;i+=1;continue
  score,ident,a,bb=ls[i].split();P=list(map(int,ls[i+1].split()));pts=ls[i+2:i+4];assert sorted(P)==list(range(26));rank+=1;ip={v:k for k,v in enumerate(P)};io={v:k for k,v in enumerate(r['O'])};encoded=[]
  for side in (0,1):
   h=r['masks'][side];d=0;ct=''
   for j,c in enumerate(pts[side]):
    ct+=chr(97+io[(ip[ord(c)-97]+d)%26]);x=h[j%23];end=h[(j+1)%23]
    while True:
     d=(d+adj[x])%26;x=(x+1)%52
     if x==end:break
   encoded.append(ct)
  assert encoded==cts;rows.append(dict(file=filename,ngram=ng,rank=rank,score=float(score),P=P,plaintexts=pts,all355_each_literal_source_reencryption_exact=True));i+=4
(b/'verified-candidates.json').write_text(json.dumps(rows,indent=2)+'\n');print('Verified',len(rows),'whole355 pairs')
