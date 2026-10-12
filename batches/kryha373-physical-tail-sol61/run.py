from pathlib import Path
import json,functools,hashlib
root=Path(__file__).resolve().parents[2];out=Path(__file__).resolve().parent
kp=root/'batches/kryha373-tail-sliding-sol61/SAT-(2, 462, 23).json';key=json.loads(kp.read_text());geo=json.loads((root/'batches/kryha-wheel-sol61/wheel52.json').read_text());edges=geo['adjacent_distances'];assert len(edges)==52 and sum(edges)==179
P,O,K=key['P'],key['O'],key['K'];assert len(K)==23
steps=[(K[(j+1)%23]+(179 if j==22 else 0)-K[j])%26 for j in range(23)];assert sum(steps)==179
masks=[];counts=[]
for start in range(52):
 coords=[0]
 for j in range(52):coords.append(coords[-1]+edges[(start+j)%52])
 @functools.lru_cache(None)
 def ways(j,index):
  if j==23:return int(index==52)
  if index==52:return 0
  return sum(ways(j+1,k)for k in range(index+1,53)if (coords[k]-coords[index])%26==steps[j] and 52-k>=22-j)
 count=ways(0,0);counts.append(count)
 def emit(j,index,path):
  if j==23:
   if index==52:masks.append([start]+[(start+k)%52 for k in path[:-1]])
   return
  for k in range(index+1,53):
   if (coords[k]-coords[index])%26==steps[j]and 52-k>=22-j and ways(j+1,k):emit(j+1,k,path+[k])
 if count:emit(0,0,[])
assert len(masks)==sum(counts)
inputs=json.loads((root/'batches/kryha373-tail-sliding-sol61/inputs.json').read_text());p=inputs['preparations'][key['case'][0]]['p'];offset=key['case'][1];c=inputs['ciphertext'][offset:offset+len(p)];erase=set(inputs['erased_absolute_onebased']);oi={v:chr(97+i)for i,v in enumerate(O)};pi={v:chr(97+i)for i,v in enumerate(P)}
records=[]
for holes in masks:
 d=K[0];encoded='';decoded='';hole=holes[0]
 for i,(a,b)in enumerate(zip(p,c)):
  encoded+=oi[(P[ord(a)-97]+d)%26];decoded+=pi[(O[ord(b)-97]-d)%26]
  end=holes[(i+1)%23]
  while hole!=end:d+=edges[hole];hole=(hole+1)%52
 generic=''.join(oi[(P[ord(a)-97]+K[i%23]+179*(i//23))%26]for i,a in enumerate(p));assert encoded==generic
 good=[i for i in range(len(p))if offset+i+1 not in erase];assert all(encoded[i]==c[i]and decoded[i]==p[i]for i in good)
 records.append(dict(holes=holes,beta=K[0],physical_cycle=179,full_generic_cipher_exact=encoded==generic,source_unerased_reencryption_exact=True,source_unerased_inverse_exact=True,published_prepared=p,literal_cipher=c,physical_cipher=encoded,literal_decoded=decoded,source_mismatches=[dict(source_position_1based=offset+i+1,literal=c[i],predicted=encoded[i],erased=offset+i+1 in erase)for i in range(len(p))if encoded[i]!=c[i]]))
(out/'masks.json').write_text(json.dumps(records,indent=2)+'\n');(out/'summary.json').write_text(json.dumps(dict(m=len(K),steps_mod26=steps,sum_minimal_steps=sum(steps),mask_count=len(masks),counts_by_start=counts,fit_length=len(p),offset=offset,erased_fit_positions=[i+1 for i in range(len(p))if offset+i+1 in erase],P=P,O=O,K=K,geometry=edges,input_sha256={str(f.relative_to(root)):hashlib.sha256(f.read_bytes()).hexdigest()for f in [kp,root/'batches/kryha-wheel-sol61/wheel52.json',root/'batches/kryha373-tail-sliding-sol61/inputs.json']}),indent=2)+'\n')
print('steps',steps,'masks',len(masks),'length',len(p));print('holes',masks)
