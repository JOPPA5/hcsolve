from pathlib import Path
import json
from exact_cover import solve
P=Path(__file__).parent;root=P.parents[1];q='nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcislox';gs=(root/'ciphers/hcp-364/work/transcription.txt').read_text().split();outs=[]
# Gated by exact recovered aligned16/17/18 n11 control, eager59.38s.
control=json.loads((P/'aligned-eager-control-results.json').read_text())[0]
assert control['status']=='sat' and control['keys_equal_planted'] and control['re_encryption_exact']
for kind,errors in [('conditional-glyph-variant',0),('raw',3)]:
 g=gs[:]
 if errors==0:g[7]='tsnnd';g[9]='eloen';g[11]='ercuv'
 ct=''.join(x for i,x in enumerate(g) if i!=2);out=solve(q+'?',ct,[16,17,18],60000,errors,[11,11,11],backend='eager');out.update(mode='conditional_target',source_quote_is_assumed=True,reading=kind,omitted_group=3,alignments=[11,11,11],header11_not_established_as_alignment=True);outs.append(out);(P/'aligned-eager-target-results.json').write_text(json.dumps(outs,indent=2)+'\n');print(json.dumps(out),flush=True)
