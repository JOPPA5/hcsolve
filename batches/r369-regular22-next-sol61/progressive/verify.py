from pathlib import Path
import json
B=Path(__file__).resolve().parent
def encrypt(s,keys):
 for key in keys:s=''.join(s[22*row+col]for col in key for row in range(5))
 return s
def decrypt(s,keys):
 for key in reversed(keys):
  out=['']*110
  for rank,col in enumerate(key):
   for row in range(5):out[22*row+col]=s[5*rank+row]
  s=''.join(out)
 return s
truth=json.loads((B/'control-truth.json').read_text());control=json.loads((B/'control-blind.json').read_text());records=[]
if control['status']=='sat':
 pred=encrypt(truth['plaintext'],control['keys']);assert pred==truth['ciphertext']==control['predicted_ciphertext'];assert decrypt(pred,control['keys'])==truth['plaintext'];assert truth['keys']==control['keys']
 records.append(dict(case='control',all_planted_keys_recovered=True,independent_full_encrypt_inverse_exact=True,recovered_n=control['recovered_n']))
if (B/'target.json').exists():
 t=json.loads((B/'target.json').read_text())
 if t['status']=='sat':
  row=t['conditional_preparation'];pred=encrypt(row['plaintext'],t['keys']);assert pred==t['predicted_ciphertext'];assert decrypt(pred,t['keys'])==row['plaintext'];mis=[i+1 for i,(x,y)in enumerate(zip(pred,row['ciphertext']))if x!=y]
  assert len(mis)==1 and pred[mis[0]-1]=='n'and row['ciphertext'][mis[0]-1]=='u'
  literal=decrypt(row['ciphertext'],t['keys']);plainmis=[i+1 for i,(x,y)in enumerate(zip(row['plaintext'],literal))if x!=y];assert len(plainmis)==1
  (B/'literal-source-inverse110.txt').write_text(literal+'\n')
  records.append(dict(case='target',independent_full_encrypt_inverse_exact_with_declared_error=True,cipher_mismatch_position1=mis[0],plaintext_mismatch_position1=plainmis[0],literal_source_inverse=literal))
(B/'independent-verification.json').write_text(json.dumps(records,indent=2)+'\n');print(records)
