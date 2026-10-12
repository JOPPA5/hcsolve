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
rows=[]
for w in [18,19,21,22]:
 truth=json.loads((B/f'width{w}-control-truth.json').read_text());r=json.loads((B/f'width{w}-control.json').read_text());s=truth['plaintext']
 for key in r['keys']:s=encoder(s,key)
 assert s==truth['ciphertext']==r['selected_ciphertext'] and r['keys']==truth['keys'] and r['recovered_n']==truth['n']
 for key in reversed(r['keys']):s=decoder(s,key)
 assert s==truth['plaintext']
 t=json.loads((B/f'width{w}-target.json').read_text());assert t['status']=='unsat' and len(t['rank_partition_checks'])==16 and all(x['status']=='unsat'for x in t['rank_partition_checks'])
 rows.append(dict(width=w,all_planted_keys_equal=True,hidden_n_equal=True,true_variant_equal=True,full65_encoder_inverse=True,all16_target_ranks_unsat=True))
(B/'independent-verification.json').write_text(json.dumps(rows,indent=2)+'\n');print('Independent checks passed',len(rows))
