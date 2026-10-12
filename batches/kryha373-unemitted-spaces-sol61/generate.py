from pathlib import Path
from itertools import product
import json,random
from schedule import prepare
b=Path(__file__).resolve().parent;geo=json.loads(Path('batches/kryha-wheel-sol61/wheel52.json').read_text());edges=geo['adjacent_distances'];coords=geo['unwrapped_effective_coordinates'];inputs=[]
for j,(unamended,extra,policy)in enumerate(product([False,True],[1,2],['lexical','whitespace'])):
 ca=prepare(unamended=unamended,ji=bool(j%2),extra=extra,policy=policy);rng=random.Random(373162012+j);m=[20,23,30][j%3];P=rng.sample(range(26),26);O=rng.sample(range(26),26);holes=sorted(rng.sample(range(52),m));phase=rng.randrange(m);holes=holes[phase:]+holes[:phase];invO={v:chr(97+i)for i,v in enumerate(O)};ct='';press=0;disp=0
 for ch,index in zip(ca['p'],ca['press_indices']):
  while press<index:
   x=holes[press%m];end=holes[(press+1)%m]
   while x!=end:disp+=edges[x];x=(x+1)%52
   press+=1
  ct+=invO[(P[ord(ch)-97]+disp)%26]
 # Independent absolute coordinate encoder checks the full generated prefix.
 alt=''
 for ch,t in zip(ca['p'],ca['press_indices']):
  h=holes[t%m];D=coords[h]-coords[holes[0]]+179*(h<holes[0])+179*(t//m);alt+=invO[(P[ord(ch)-97]+D)%26]
 assert alt==ct
 inp=dict(case=ca,ciphertext=ct,period_family=[2,52]);(b/f'control{j}-input.json').write_text(json.dumps(inp,indent=2,ensure_ascii=False)+'\n');(b/f'control{j}-truth.json').write_text(json.dumps(dict(m=m,P=P,O=O,holes=holes,seed=373162012+j,independent_encoder_exact=True),indent=2)+'\n');inputs.append(inp)
print('8 fresh physical-mask controls generated; each n93/92 and invisible schedule preserved.')
