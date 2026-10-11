from pathlib import Path
import json,random,unicodedata
b=Path(__file__).resolve().parent;r=b.parents[1];digits=['nula','jedna','dva','tri','styri','pat','sest','sedem','osem','devat'];ns={'digits':digits,'unicodedata':unicodedata};s=(r/'batches/kryha-mask-sol61/prepare.py').read_text();exec(s[s.index('def prep('):s.index('train=r/')],ns);prep=ns['prep'];excluded={prep(s) for s in (r/'ciphers/hcp-393/work/sk_snk-ud-train.conllu').read_text().strip().split('\n\n')};text=''.join(prep(s) for s in (r/'ciphers/hcp-393/work/square10/sk_snk-ud-test.conllu').read_text().strip().split('\n\n') if prep(s) not in excluded);a=text[40000:40385];assert len(a)==385;pts=[a,'q'+a[:-1]];rng=random.Random(2335035110);P=rng.sample(range(26),26);O=rng.sample(range(26),26);invP={x:i for i,x in enumerate(P)};invO={x:i for i,x in enumerate(O)};w=json.loads((r/'batches/kryha-wheel-sol61/wheel52.json').read_text());coords=w['unwrapped_effective_coordinates'];adj=w['adjacent_distances'];cts=[];holes=[];ds=[]
for pt in pts:
 h=sorted(rng.sample(range(52),23));k=rng.randrange(23);h=h[k:]+h[:k];holes.append(h);jumps=[]
 for x,y in zip(h,h[1:]+h[:1]):
  q=x;v=0
  while True:
   v+=adj[q];q=(q+1)%52
   if q==y:break
  jumps.append(v)
 d=0;ct='';schedule=[]
 for i,c in enumerate(pt):
  schedule.append(d);ct+=chr(97+invO[(invP[ord(c)-97]+d)%26]);d=(d+jumps[i%23])%26
 recovered=''
 for i,c in enumerate(ct):
  dis=coords[h[i%23]]-coords[h[0]]+(179 if h[i%23]<h[0] else 0)+179*(i//23)
  recovered+=chr(97+P[(O[ord(c)-97]-dis)%26])
 assert recovered==pt;ds.append(schedule);cts.append(ct)
K=[(ds[1][j+1]-ds[0][j])%26 for j in range(23)];delta=[(K[(j+1)%23]-K[j])%26 for j in range(23)]
(b/'control-input.json').write_text(json.dumps(dict(ciphertexts=cts,O=O,K=K,delta=delta,known_output_ring=True,unknown_input_ring_masks=True),indent=2)+'\n');(b/'control-truth.json').write_text(json.dumps(dict(plaintexts=pts,P=P,O=O,masks=holes,seed=2335035110,TEST_offset=40000,TRAIN_excluded=True,independent_physical_inverse_exact=True),indent=2)+'\n')
