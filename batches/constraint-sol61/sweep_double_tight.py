from pathlib import Path
from collections import Counter
import json,random,time
from exact_cover import solve,enc
P=Path(__file__).parent;root=P.parents[1];quote='nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcislox';template=quote+'?';gs=(root/'ciphers/hcp-364/work/transcription.txt').read_text().split();q=Counter(quote);cases=[]
for omit in range(14):
 ct=''.join(g for i,g in enumerate(gs) if i!=omit);deficit=sum((q-Counter(ct)).values())
 if deficit<=3:cases.append(('raw',omit+1,ct,3))
variants=gs[:];variants[7]='tsnnd';variants[9]='eloen';variants[11]='ercuv'
ct=''.join(g for i,g in enumerate(variants) if i!=2);assert sum((q-Counter(ct)).values())==0;cases.append(('conditional-glyph-variant',3,ct,0))
(P/'target-cases.json').write_text(json.dumps({'template':template,'assumption':'Cover quote is conditional, not decrypted plaintext','cases':cases,'raw_inventory_feasible_omissions':[x[1] for x in cases if x[0]=='raw']},indent=2)+'\n')
rng=random.Random(610364994);log=P/'double-sweep-tight.jsonl'
for a in range(16,23):
 for b in range(16,23):
  ws=[a,b];keys=[rng.sample(range(w),w) for w in ws];cp=quote+'r';cc=cp
  for k in keys:cc=enc(cc,k)
  control=solve(cp,cc,ws,20000);control.update(mode='known_plaintext_positive_control',planted_keys=keys,keys_equal_planted=control.get('keys')==keys,plaintext=cp,ciphertext=cc)
  with log.open('a') as f:f.write(json.dumps(control)+'\n')
  print('control',ws,control['status'],round(control['seconds'],3),flush=True)
  if control['status']!='sat':continue
  for kind,omit,ct,errors in cases:
   out=solve(template,ct,ws,20000,errors);out.update(mode='conditional_target',reading=kind,omitted_group=omit,source_quote_is_assumed=True,error_bound=errors)
   with log.open('a') as f:f.write(json.dumps(out)+'\n')
   print('target',ws,kind,out['status'],round(out['seconds'],3),flush=True)
