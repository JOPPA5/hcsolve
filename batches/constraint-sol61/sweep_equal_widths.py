from pathlib import Path
import random,json,os
from exact_cover import solve,enc
P=Path(__file__).parent;root=P.parents[1];q='nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcislox';gs=(root/'ciphers/hcp-364/work/transcription.txt').read_text().split();log=P/'equal17-22-n11.jsonl';(P/'equal-width-sweep.pid').write_text(str(os.getpid()))
def record(out):
 with log.open('a') as f:f.write(json.dumps(out)+'\n')
 print(out['mode'],out['widths'],out.get('reading',''),out['backend'],out['status'],round(out['seconds'],3),flush=True)
def run(p,c,ws,errors,ns,metadata,blocked=None):
 for backend,timeout in [('generic',20000),('eager',60000)]:
  out=solve(p,c,ws,timeout,errors,ns,backend=backend,blocked_keys=blocked);out.update(metadata);record(out)
  if out['status']!='unknown':return out
 return out
for w in range(17,23):
 rng=random.Random(6103642200+w);ns=[11]*3;ws=[w]*3;ks=[];ct=q+'r'
 for _ in range(3):
  k=rng.sample(range(1,w),w-1);k.insert(10,0);ks.append(k);ct=enc(ct,k)
 ctrl=run(q+'r',ct,ws,0,ns,{'mode':'independent_aligned_triple_control','alignments':ns,'planted_keys':ks,'plaintext':q+'r','ciphertext':ct})
 if ctrl['status']!='sat':continue
 if ctrl['keys']!=ks:
  # A second valid complete keyset is not recovery of unique original keys.
  print('Control alternative keys; full exact re-encryption checked',flush=True)
 for kind,errors in [('conditional-glyph-variant',0),('raw',3)]:
  g=gs[:]
  if errors==0:g[7]='tsnnd';g[9]='eloen';g[11]='ercuv'
  c=''.join(x for i,x in enumerate(g) if i!=2);metadata={'mode':'conditional_target','reading':kind,'alignments':ns,'alignment_is_hypothesis':True,'omitted_group':3,'source_quote_is_assumed':True}
  out=run(q+'?',c,ws,errors,ns,metadata)
  if out['status']=='sat':
   metadata=dict(metadata,mode='conditional_target_second_witness',blocked_first_keys=out['keys'])
   run(q+'?',c,ws,errors,ns,metadata,[out['keys']])
