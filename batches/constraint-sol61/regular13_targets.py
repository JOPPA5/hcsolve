from pathlib import Path
import json,os,time
from exact_cover import solve
P=Path(__file__).parent;root=P.parents[1];q='nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcislox';gs=(root/'ciphers/hcp-364/work/transcription.txt').read_text().split();(P/'regular13.pid').write_text(str(os.getpid()));control=json.loads((P/'quote-control-results.json').read_text())[1];assert control['status']=='sat' and control['keys_equal_planted'] and control['re_encryption_exact'];log=P/'regular13-targets.jsonl'
def run(kind,errors,blocked=None):
 g=gs[:]
 if errors==0:g[7]='tsnnd';g[9]='eloen';g[11]='ercuv'
 ct=''.join(x for i,x in enumerate(g) if i!=2)
 (P/'regular13-state.json').write_text(json.dumps({'phase':'building_and_solving','reading':kind,'error_bound':errors,'widths':[13,13,13],'alignments':None,'backend':'generic','timeout_ms':60000,'second_witness':blocked is not None,'started_unix':time.time()},indent=2)+'\n')
 out=solve(q+'?',ct,[13,13,13],60000,errors,None,backend='generic',blocked_keys=blocked);out.update(mode='regular13_conditional_target_second_witness' if blocked else 'regular13_conditional_target',source_quote_is_assumed=True,alignment_is_hypothesis=False,alignments=None,reading=kind,omitted_group=3,indicator_position_is_hypothesis=True,literal_input=ct,explicit_glyph_variant=errors==0)
 if blocked:out['blocked_first_keyset']=blocked[0]
 with log.open('a') as f:f.write(json.dumps(out)+'\n')
 print(json.dumps(out),flush=True)
 return out
for kind,errors in [('conditional-glyph-variant',0),('raw',3)]:
 out=run(kind,errors)
 if out['status']=='sat':run(kind,errors,[out['keys']])
(P/'regular13-state.json').write_text(json.dumps({'phase':'complete','finished_unix':time.time()},indent=2)+'\n')
