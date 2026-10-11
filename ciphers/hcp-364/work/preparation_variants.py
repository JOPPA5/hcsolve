"""Conditional known-quote single-columnar tests; sentence-X is optional.
All sixteen subsets of four sentence markers, with unknown final padding.
This extends the earlier narrow fixed four-X preparation, not the source.
"""
from pathlib import Path
import json,random
from known_quote_test import solve,enc,groups
P=Path(__file__).parent
sentences=['nelustitelne','neudalsicislopredtextom','vidbodtripokynov','uvedcislo']
assert sum(map(len,sentences))==60
results=[];hits=[]
for mask in range(16):
 p=''.join(s+('x' if mask>>i&1 else '') for i,s in enumerate(sentences))
 p+='?'*(65-len(p))
 rng=random.Random(364620+mask);k=list(range(19));rng.shuffle(k)
 c=enc(p.replace('?','r'),k);control=solve(c,p,19,0)
 assert control['key'] is not None
 complete=0
 for omit in range(14):
  c=''.join(g for i,g in enumerate(groups) if i!=omit)
  for rev in [False,True]:
   ct=c[::-1] if rev else c
   for w in range(2,23):
    r=solve(ct,p,w,3);complete+=r['complete']
    if r['key'] is not None:hits.append(dict(mask=mask,prepared=p,omit=omit+1,reverse=rev,width=w,**r))
 results.append(dict(sentence_x_mask=mask,prepared=p,target_cases=588,complete_cases=complete,control=control))
 print('mask',mask,'complete',complete,'total_hits',len(hits),flush=True)
(P/'preparation-variants-results.json').write_text(json.dumps(dict(status='conditional_crib_tests_not_decryption',tested_error_bound=3,cases=results,hits=hits),indent=2)+'\n')
