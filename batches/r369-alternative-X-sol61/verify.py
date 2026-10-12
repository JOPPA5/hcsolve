from pathlib import Path
import json
B=Path(__file__).resolve().parent;prep=json.loads((B/'alternative-preparation.json').read_text());p,c=prep['plaintext'],prep['ciphertext']
def enc(s,keys):
 for key in keys:
  result=[]
  for col in key:
   for row in range(5):result.append(s[row*22+col])
  s=''.join(result)
 return s
def dec(s,keys):
 for key in reversed(keys):
  result=['']*110
  for rank,col in enumerate(key):
   for row in range(5):result[row*22+col]=s[rank*5+row]
  s=''.join(result)
 return s
results=[]
for name in ['common-target','progressive-target']:
 path=B/(name+'.json')
 if not path.exists():continue
 data=json.loads(path.read_text());hits=[x for x in data['ranks']if x['status']=='sat']if'ranks'in data else([data]if data['status']=='sat'else[])
 for hit in hits:
  prediction=enc(p,hit['keys']);assert prediction==hit['predicted_ciphertext'];assert dec(prediction,hit['keys'])==p
  mismatch=[i+1 for i,(a,b)in enumerate(zip(prediction,c))if a!=b];assert len(mismatch)==1 and prediction[mismatch[0]-1]=='n'and c[mismatch[0]-1]=='u'
  literal=dec(c,hit['keys']);pm=[i+1 for i,(a,b)in enumerate(zip(p,literal))if a!=b];assert len(pm)==1
  results.append(dict(branch=name,independent_full_encode_inverse=True,cipher_mismatch_position1=mismatch[0],plain_mismatch_position1=pm[0],literal_source_inverse=literal,keys=hit['keys']))
  (B/(name+'-literal-inverse.txt')).write_text(literal+'\n')
(B/'independent-verification.json').write_text(json.dumps(results,indent=2)+'\n');print(results)
