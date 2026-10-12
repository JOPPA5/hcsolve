from pathlib import Path
import json
B=Path(__file__).resolve().parent
def encoder(s,key):
 out=[]
 for col in key:
  for row in range((len(s)+len(key)-1)//len(key)):
   i=row*len(key)+col
   if i<len(s):out.append(s[i])
 return ''.join(out)
def decoder(s,key):
 out=['']*len(s);at=0
 for col in key:
  for row in range((len(s)+len(key)-1)//len(key)):
   i=row*len(key)+col
   if i<len(s):out[i]=s[at];at+=1
 return ''.join(out)
truth=json.loads((B/'control-truth.json').read_text());r=json.loads((B/'control.json').read_text());assert r['status']=='sat';s=truth['plaintext']
for key in r['keys']:s=encoder(s,key)
assert s==truth['ciphertext']==r['selected_ciphertext'] and r['keys']==truth['keys'] and r['recovered_n']==truth['n']
for key in reversed(r['keys']):s=decoder(s,key)
assert s==truth['plaintext'];(B/'independent-verification.json').write_text(json.dumps(dict(all_three_planted_keys_equal=True,hidden_n_equal=True,true_variant_equal=True,full65_encoder_inverse=True),indent=2)+'\n');print('Full65 control, all keys/n/variant independently exact')
