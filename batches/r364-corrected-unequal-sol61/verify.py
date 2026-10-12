from pathlib import Path
import json
B=Path(__file__).resolve().parent
def encrypt(s,key):
 out=[]
 for col in key:
  for row in range((len(s)+len(key)-1)//len(key)):
   i=row*len(key)+col
   if i<len(s):out.append(s[i])
 return ''.join(out)
def inverse(s,key):
 out=['']*len(s);at=0
 for col in key:
  for row in range((len(s)+len(key)-1)//len(key)):
   i=row*len(key)+col
   if i<len(s):out[i]=s[at];at+=1
 return ''.join(out)
records=[]
for mode in ['free-X','fixed-end-X']:
 result=json.loads((B/(mode+'-control.json')).read_text())
 if result['status']!='sat':continue
 truth=json.loads((B/(mode+'-control-truth.json')).read_text());pred=result['conditional_plaintext']
 for key in result['keys']:pred=encrypt(pred,key)
 assert pred==result['selected_ciphertext_variant']==truth['ciphertext'];assert result['keys']==truth['keys']
 d=pred
 for key in reversed(result['keys']):d=inverse(d,key)
 assert d==truth['plaintext'];assert all(key.index(0)+1==11 for key in result['keys'])
 records.append(dict(mode=mode,whole65_encoder_inverse=True,all_planted_keys_equal=True,planted_plaintext_equal=True,planted_variant_equal=True))
(B/'independent-verification.json').write_text(json.dumps(records,indent=2)+'\n');print(records)
