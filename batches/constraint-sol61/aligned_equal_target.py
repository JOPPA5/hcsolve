from pathlib import Path
import json
from exact_cover import solve
P=Path(__file__).parent;root=P.parents[1];q='nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcislox';gs=(root/'ciphers/hcp-364/work/transcription.txt').read_text().split();control=json.loads((P/'aligned-equal-control.json').read_text());assert control['status']=='sat' and control['keys_equal_planted'] and control['re_encryption_exact'];outs=[]
for kind,errors in [('raw',3),('conditional-glyph-variant',0)]:
 g=gs[:]
 if errors==0:g[7]='tsnnd';g[9]='eloen';g[11]='ercuv'
 ct=''.join(x for i,x in enumerate(g) if i!=2);out=solve(q+'?',ct,[16,16,16],20000,errors,[11,11,11]);out.update(mode='conditional_target',source_quote_is_assumed=True,reading=kind,omitted_group=3,alignments=[11,11,11],header11_not_established_as_alignment=True);outs.append(out);print(json.dumps(out),flush=True)
(P/'aligned-equal-target-results.json').write_text(json.dumps(outs,indent=2)+'\n')
