from pathlib import Path
import json,time
from exact_cover import solve
P=Path(__file__).parent;q='nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcislox';groups=(P.parents[1]/'ciphers/hcp-364/work/transcription.txt').read_text().split();controls=[json.loads(x) for x in (P/'equal17-22-n11.jsonl').read_text().splitlines()];log=P/'exploratory-equal-targets.jsonl'
def save(out):
 with log.open('a') as f:f.write(json.dumps(out)+'\n')
 print(out['mode'],out['widths'],out['status'],out['seconds'],flush=True)
for w in range(17,23):
 src=next(x for x in controls if x['widths']==[w]*3)
 check=solve(src['plaintext'],src['ciphertext'],[w]*3,20000,0,[11]*3,known_keys=src['planted_keys'],backend='eager');check.update(mode='known_key_encoding_check_only',not_blind_key_recovery=True);save(check);assert check['status']=='sat' and check['re_encryption_exact']
 for errors in [0,3]:
  gs=groups[:]
  if not errors:gs[7]='tsnnd';gs[9]='eloen';gs[11]='ercuv'
  target=''.join(x for i,x in enumerate(gs) if i!=2)
  (P/'exploratory-state.json').write_text(json.dumps(dict(width=w,error_bound=errors,started_unix=time.time(),phase='solving'))+'\n')
  out=solve(q+'?',target,[w]*3,60000,errors,[11]*3,backend='eager');out.update(mode='exploratory_conditional_target',source_quote_is_assumed=True,omitted_group=3,literal_input=target,reading='raw' if errors else 'conditional-glyph-variant',alignments=[11]*3,error_bound=errors,blind_control_status='unknown',encoding_known_key_check='sat');save(out)
  if out['status']=='sat':
   second=solve(q+'?',target,[w]*3,60000,errors,[11]*3,backend='eager',blocked_keys=[out['keys']]);second.update(mode='exploratory_second_witness',blocked_first_keyset=out['keys']);save(second)
(P/'exploratory-state.json').write_text(json.dumps(dict(phase='complete',finished_unix=time.time()))+'\n')
