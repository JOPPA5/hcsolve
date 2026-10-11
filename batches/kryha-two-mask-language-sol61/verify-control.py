from pathlib import Path
import json
b=Path(__file__).resolve().parent;r=b.parents[1];inp=json.load(open(b/'control-input.json'));truth=json.load(open(b/'control-truth.json'));candidates=json.load(open(b/'control-neighbors.json'));coord=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'))['unwrapped_effective_coordinates'];adj=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'))['adjacent_distances'];lines=(b/'control-profile.txt').read_text().splitlines();good=[]
for num,row in enumerate(candidates):
 if row['plaintexts'] != [truth['plaintexts'][0][:-1],truth['plaintexts'][1][1:]]:continue
 vals=lines[row['profile_rank']].split();hs=[list(map(int,vals[q::2])) for q in (1,2)];hs[1]=hs[1][-1:]+hs[1][:-1];beta=(inp['K'][0]-(coord[hs[1][1]]-coord[hs[1][0]]+(179 if hs[1][1]<hs[1][0] else 0)))%26;P=row['P'];O=inp['O'];plains=[];cts=[]
 for side in (0,1):
  h=hs[side];pt=''
  for i,c in enumerate(inp['ciphertexts'][side]):
   D=coord[h[i%23]]-coord[h[0]]+(179 if h[i%23]<h[0] else 0)+179*(i//23)+(beta if side else 0)
   pt+=chr(97+P[(O[ord(c)-97]-D)%26])
  plains.append(pt);ip={x:i for i,x in enumerate(P)};io={x:i for i,x in enumerate(O)};d=beta if side else 0;ct=''
  for i,c in enumerate(pt):
   ct+=chr(97+io[(ip[ord(c)-97]+d)%26]);x=h[i%23];end=h[(i+1)%23]
   while True:
    d=(d+adj[x])%26;x=(x+1)%52
    if x==end:break
  cts.append(ct)
 assert plains==truth['plaintexts'] and cts==inp['ciphertexts'] and beta==0
 good.append(dict(blind_candidate_rank=num+1,profile_rank=row['profile_rank'],swap=row['swap'],beta=beta,P=P,O=O,masks=hs,plaintexts=plains,full_385_each_exact=True,independent_adjacent_walk_reencryption_exact=True))
assert good;(b/'control-full-verification.json').write_text(json.dumps(good,indent=2)+'\n');print('Exact full controls',len(good))
