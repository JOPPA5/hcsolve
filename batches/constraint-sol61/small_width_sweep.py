from pathlib import Path
import random,json,time
from exact_cover import solve,enc
P=Path(__file__).parent;q='nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcislox';groups=(P.parents[1]/'ciphers/hcp-364/work/transcription.txt').read_text().split();log=P/'small-width-sweep.jsonl';previous=[json.loads(x) for x in (P/'lower-width-sweep.jsonl').read_text().splitlines()]
def save(out):
 with log.open('a') as f:f.write(json.dumps(out)+'\n')
 print(out['mode'],out['widths'],out['status'],round(out['seconds'],3),flush=True)
for w in list(range(2,11))+[12,14,15]:
 if w>10:
  control=next(x for x in previous if x['mode']=='independent_unaligned_triple_control' and x['widths']==[w]*3);keys=control['planted_keys'];ct=control['ciphertext'];out=dict(control);out.update(mode='prior_independent_control_reused',reused_from='lower-width-sweep.jsonl',not_rerun=True);save(out)
 else:
  rng=random.Random(6103648800+w);keys=[rng.sample(range(w),w) for _ in range(3)];ct=q+'r'
  for key in keys:ct=enc(ct,key)
  control=solve(q+'r',ct,[w]*3,60000);control.update(mode='independent_unaligned_triple_control',planted_keys=keys,keys_equal_planted=control.get('keys')==keys,plaintext=q+'r',ciphertext=ct);save(control)
 check=solve(q+'r',ct,[w]*3,60000,known_keys=keys);check.update(mode='known_key_encoding_check_only',not_blind_key_recovery=True,planted_keys=keys,plaintext=q+'r',ciphertext=ct);save(check);assert check['status']=='sat' and check['re_encryption_exact'] and check['independent_inverse_exact']
 for errors in [0,3]:
  gs=groups[:]
  if not errors:gs[7]='tsnnd';gs[9]='eloen';gs[11]='ercuv'
  target=''.join(x for i,x in enumerate(gs) if i!=2)
  (P/'small-width-state.json').write_text(json.dumps(dict(width=w,error_bound=errors,started_unix=time.time(),phase='solving'))+'\n')
  out=solve(q+'?',target,[w]*3,60000,errors);out.update(mode='conditional_unaligned_target',source_quote_is_assumed=True,omitted_group=3,literal_input=target,reading='raw' if errors else 'conditional-glyph-variant',alignment_restricted=False,error_bound=errors,blind_control_status=control['status'],encoding_known_key_check='sat');save(out)
  if out['status']=='sat':
   second=solve(q+'?',target,[w]*3,60000,errors,blocked_keys=[out['keys']]);second.update(mode='conditional_unaligned_second_witness',width=w,reading=out['reading'],blocked_first_keyset=out['keys']);save(second)
(P/'small-width-state.json').write_text(json.dumps(dict(phase='complete',finished_unix=time.time()))+'\n')
