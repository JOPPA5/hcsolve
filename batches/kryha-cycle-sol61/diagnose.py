from pathlib import Path
from collections import Counter
import json,random
b=Path(__file__).resolve().parent
def profile(ct,m,O,order):
 hist=[Counter() for _ in range(m)]
 for i,c in enumerate(ct):hist[i%m][(O[ord(c)-97]-23*(i//m))%26]+=1
 return sum(n*(n-1)//2 if order==2 else n*(n-1)*(n-2)//6 for row in hist for n in row.values())
records=[]
for c in json.load(open(b/'controls.json')):
 m=c['m'];ct=c['ciphertext'];true=c['output_positions'];g=true[0];true=[(v-g)%26 for v in true]
 explicit=sum((true[ord(ct[j])-97]-true[ord(ct[i])-97])%26==(23*((j-i)//m))%26 for i in range(len(ct)) for j in range(i+m,len(ct),m))
 assert explicit==profile(ct,m,true,2)
 for order in (2,3):
  rng=random.Random(520000+m);null=[]
  for _ in range(1000):key=list(range(26));rng.shuffle(key);null.append(profile(ct,m,key,order))
  candidates=[];path=b/f'order{order}-m{m}.tsv'
  if path.exists():
   for line in path.read_text().splitlines():
    parts=line.split('\t')
    if len(parts)!=3:continue
    restart,s,key=parts;key=list(map(int,key.split(',')))
    if len(key)!=26:continue
    assert sorted(key)==list(range(26));assert float(s)==profile(ct,m,key,order)
    candidates.append({'restart':int(restart),'score':int(float(s)),'key':key,'true_positions':sum(a==z for a,z in zip(key,true)),'equivalent_pairs':sum((key[a]-key[z])%26==(true[a]-true[z])%26 for a in range(26) for z in range(a+1,26)),'exact_ring_up_to_rotation':key==true})
  candidates.sort(key=lambda x:x['score'],reverse=True);truth=profile(ct,m,true,order);rec={'control':c['label'],'order':order,'true_score':truth,'random_max':max(null),'random_mean':sum(null)/len(null),'blind_starts_completed':len(candidates),'optimized_above_truth':sum(x['score']>truth for x in candidates),'true_ring_recovered':any(x['exact_ring_up_to_rotation'] for x in candidates),'candidates':candidates};records.append(rec)
(b/'diagnostics.json').write_text(json.dumps(records,indent=2)+'\n')
for x in records:print(x['control'],x['order'],'truth',x['true_score'],'null max',x['random_max'],'blind',x['blind_starts_completed'],'above truth',x['optimized_above_truth'],'exact',x['true_ring_recovered'],'top',[(v['score'],v['true_positions']) for v in x['candidates'][:3]])
