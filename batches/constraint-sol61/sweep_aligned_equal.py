from pathlib import Path
import random,json
from exact_cover import solve,enc
P=Path(__file__).parent;root=P.parents[1];q='nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcislox';gs=(root/'ciphers/hcp-364/work/transcription.txt').read_text().split();log=P/'aligned-equal-sweep.jsonl';rng=random.Random(6103641617);ws=[16,16,16]
def record(out):
 with log.open('a') as f:f.write(json.dumps(out)+'\n')
for n in range(1,17):
 if n==11:continue # Already separately validated and target-tested.
 ns=[n]*3;ks=[];c=q+'r'
 for w in ws:
  k=rng.sample(range(1,w),w-1);k.insert(n-1,0);ks.append(k);c=enc(c,k)
 ctrl=solve(q+'r',c,ws,20000,0,ns);ctrl.update(mode='independent_aligned_triple_control',alignments=ns,planted_keys=ks,plaintext=q+'r',ciphertext=c,keys_equal_planted=ctrl.get('keys')==ks);record(ctrl);print('control',n,ctrl['status'],round(ctrl['seconds'],3),flush=True)
 if ctrl['status']!='sat':continue
 for kind,errors in [('conditional-glyph-variant',0),('raw',3)]:
  g=gs[:]
  if errors==0:g[7]='tsnnd';g[9]='eloen';g[11]='ercuv'
  ct=''.join(x for i,x in enumerate(g) if i!=2);out=solve(q+'?',ct,ws,20000,errors,ns);out.update(mode='conditional_target',source_quote_is_assumed=True,reading=kind,omitted_group=3,alignments=ns,alignment_is_hypothesis=True);record(out);print('target',n,kind,out['status'],round(out['seconds'],3),flush=True)
