from pathlib import Path
import json
B=Path(__file__).resolve().parent;R=B.parents[1];S=R/'batches/kryha-two-mask-language-sol61';data=json.loads((S/'control-input.json').read_text());coord=json.loads((R/'batches/kryha-wheel-sol61/wheel52.json').read_text())['unwrapped_effective_coordinates'];rows=(S/'control-profile.txt').read_text().splitlines()[1:];neighbors=json.loads((S/'control-neighbors.json').read_text());ranked=json.loads((B/'blind-ranked.json').read_text());out=[]
for metric in ('pure6','pure7'):
 win=max(ranked,key=lambda x:x[metric]);c=neighbors[win['index']];nums=rows[c['profile_rank']-1].split();ha=list(map(int,nums[1::2]));hb=list(map(int,nums[2::2]));m=len(ha);masks=[ha,[hb[-1]]+hb[:-1]];arc=(coord[hb[0]]-coord[hb[-1]])%179;beta=(data['K'][0]-arc)%26;P=c['P'];O=data['O'];pts=[]
 for q,(ct,h)in enumerate(zip(data['ciphertexts'],masks)):
  shifts=[coord[h[i%m]]-coord[h[0]]+(179 if h[i%m]<h[0]else 0)+179*(i//m)+(beta if q else 0)for i in range(len(ct))];pt=''.join(chr(97+P[(O[ord(x)-97]-d)%26])for x,d in zip(ct,shifts));pts.append(pt)
  # Independent adjacent-arc encoder, no coordinate formula.
  adj=json.loads((R/'batches/kryha-wheel-sol61/wheel52.json').read_text())['adjacent_distances'];jumps=[]
  for a,b in zip(h,h[1:]+h[:1]):
   z=a;v=0
   while True:
    v+=adj[z];z=(z+1)%52
    if z==b:break
   jumps.append(v)
  ip={x:i for i,x in enumerate(P)};io={x:i for i,x in enumerate(O)};d=beta if q else 0;re=''
  for i,x in enumerate(pt):re+=chr(97+io[(ip[ord(x)-97]+d)%26]);d=(d+jumps[i%m])%26
  assert re==ct and sum(jumps)==179
 out.append(dict(metric=metric,index=win['index'],P=P,O=O,masks=masks,beta=beta,plaintexts=pts,full_adjacent_encoder_exact=True))
# Truth is used only now, after the language-selected keys and exact encoders are frozen.
truth=json.loads((S/'control-truth.json').read_text())
for x in out:x['full_plaintext_exact']=x['plaintexts']==truth['plaintexts'];x['matches']=[sum(a==b for a,b in zip(p,t))for p,t in zip(x['plaintexts'],truth['plaintexts'])]
(B/'full-control-verification.json').write_text(json.dumps(out,indent=2));print([(x['metric'],x['matches'],x['full_plaintext_exact'])for x in out])
