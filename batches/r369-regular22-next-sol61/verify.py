from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parent
def encrypt(s,key):
 out=[]
 for col in key:
  for row in range((len(s)+len(key)-1)//len(key)):
   i=row*len(key)+col
   if i<len(s):out.append(s[i])
 return ''.join(out)
records=[]
for f in B.glob('control*-eager.json'):
 result=json.loads(f.read_text())
 if result['status']!='sat':continue
 truth=json.loads((B/(f.name.split('-')[0]+'-truth.json')).read_text());v=truth['plaintext']
 for key in result['keys']:v=encrypt(v,key)
 assert v==truth['ciphertext']==result['predicted_ciphertext']
 assert result['keys']==truth['keys']
 records.append(dict(file=f.name,all_three_truth_keys_equal=True,independent_full_encrypt_exact=True,recovered_n=result['recovered_n'],truth_n=truth['n']))
target=B/'target.json'
if target.exists():
 t=json.loads(target.read_text())
 if t['status']=='sat':
  row=t['conditional_preparation'];v=row['plaintext']
  for key in t['keys']:v=encrypt(v,key)
  mis=[i+1 for i,(a,b)in enumerate(zip(v,row['ciphertext']))if a!=b]
  assert v==t['predicted_ciphertext'] and len(mis)==1
  assert v[mis[0]-1]=='n' and row['ciphertext'][mis[0]-1]=='u'
  records.append(dict(file='target.json',independent_full_encrypt_exact_with_declared_error=True,mismatch_position1=mis[0]))
(B/'independent-verification.json').write_text(json.dumps(records,indent=2)+'\n')
paths=[Path('ciphers/hcp-369/source/cryptogram.jpg'),Path('batches/solved-context-main/365/plaintext.jpg'),B/'engine.py']
(B/'hashes.json').write_text(json.dumps({str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths},indent=2)+'\n')
print(records)
