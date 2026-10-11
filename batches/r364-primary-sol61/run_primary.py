from pathlib import Path
import json,time,random
from exact_cover import solve,enc
p=Path(__file__).resolve().parent;repo=p.parents[1];widths=[21,19,20];rng=random.Random(21192036461011)
plain='nezavislykontrolnytelegramoverujepresnosttrojitehoprehadzovaniapismenx'[:65];assert len(plain)==65
cases=json.loads((repo/'batches/constraint-sol61/target-cases.json').read_text());out=p/'results.jsonl'
def record(r):
 with out.open('a')as f:f.write(json.dumps(r)+'\n')
 print(json.dumps({k:v for k,v in r.items()if k in ['stage','mode','n','reading','status','seconds','error_bound']}),flush=True)
def keys_for(align):
 keys=[]
 for w,n in zip(widths,align):
  k=list(range(1,w));rng.shuffle(k);k.insert(n-1,0);keys.append(k)
 return keys
# Fresh checks independent of historical target template and readings.
for mode,align in [('constant',[7,7,7]),('progressive',[5,6,7])]:
 keys=keys_for(align);c=plain
 for k in keys:c=enc(c,k)
 r=solve(plain,c,widths,3000,alignments=align,known_keys=keys,backend='eager');r.update(stage='known-key-encoding-check',mode=mode,plaintext=plain,ciphertext=c,planted_keys=keys);record(r);assert r['status']=='sat'
 r=solve(plain,c,widths,60000,alignments=align,backend='eager');r.update(stage='fresh-blind-control',mode=mode,plaintext=plain,ciphertext=c,planted_keys=keys);record(r)
# Exhaustive daily-rank domain for these unequal widths only, bounded checks.
for mode,ns in [('constant',range(1,20)),('progressive',range(1,19))]:
 for n in ns:
  align=[n]*3 if mode=='constant'else[n,n+1,n+2]
  for reading,omit,c,errors in cases['cases']:
   r=solve(cases['template'],c,widths,60000,errors=errors,alignments=align,backend='eager');r.update(stage='conditional-target',mode=mode,n=n,alignment=align,reading=reading,omitted_group=omit,assumptions='unproved cover quote, fixed four sentence X, unknown final filler, omit group 3; arbitrary key permutations constrained only by daily column0 ranks');record(r)
   if r['status']=='sat':
    other=solve(cases['template'],c,widths,60000,errors=errors,alignments=align,backend='eager',blocked_keys=[r['keys']]);other.update(stage='blocked-first-keyset-alternative',mode=mode,n=n,reading=reading);record(other)
