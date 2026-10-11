from pathlib import Path
import random,json
from exact_cover import solve,enc
P=Path(__file__).parent;q='nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcislox';groups=(P.parents[1]/'ciphers/hcp-364/work/transcription.txt').read_text().split();log=P/'lower-width-sweep.jsonl'
def save(out):
 with log.open('a') as f:f.write(json.dumps(out)+'\n')
 print(out['mode'],out['widths'],out['status'],out['seconds'],flush=True)
for w in [11,12,14,15]:
 rng=random.Random(6103644400+w);keys=[rng.sample(range(w),w) for _ in range(3)];ct=q+'r'
 for key in keys:ct=enc(ct,key)
 out=solve(q+'r',ct,[w]*3,60000);out.update(mode='independent_unaligned_triple_control',planted_keys=keys,keys_equal_planted=out.get('keys')==keys,plaintext=q+'r',ciphertext=ct);save(out)
 if out['status']!='sat':continue
 for errors in [0,3]:
  gs=groups[:]
  if not errors:gs[7]='tsnnd';gs[9]='eloen';gs[11]='ercuv'
  target=''.join(x for i,x in enumerate(gs) if i!=2)
  out=solve(q+'?',target,[w]*3,60000,errors);out.update(mode='conditional_unaligned_target',source_quote_is_assumed=True,omitted_group=3,literal_input=target,reading='raw' if errors else 'conditional-glyph-variant',alignment_restricted=False,error_bound=errors);save(out)
  if out['status']=='sat':
   second=solve(q+'?',target,[w]*3,60000,errors,blocked_keys=[out['keys']]);second.update(mode='conditional_unaligned_second_witness',blocked_first_keyset=out['keys']);save(second)
