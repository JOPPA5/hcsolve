from pathlib import Path
from exact_cover import solve,enc
import random,json,concurrent.futures,hashlib
B=Path(__file__).resolve().parent;S=Path('batches/repeat396-387-sol61');p=(S/'preferred-prepared-plaintext50.txt').read_text().strip();g=(S/'ciphertext387.txt').read_text().split()[1:];body=''.join(g[:7]+g[8:]);assert len(body)==len(p)==50
variants=[]
for i,ch in enumerate(body):
 if ch=='p':variants.append({'changed_position1':i+1,'ciphertext':body[:i]+'f'+body[i+1:],'hypothesis':'printed P changed to F; not source-supported glyph correction'})
(B/'conditional-pair.json').write_text(json.dumps({'published_plaintext':p,'omit_group1':8,'literal_body':body,'variants':variants},indent=2)+'\n')
rng=random.Random(3963871011);controls=[]
for label in ['shuffled-matched-inventory','known-plaintext-order']:
 plain=''.join(rng.sample(p,len(p)))if label.startswith('shuffled')else p;ks=[rng.sample(range(w),w)for w in [21,19,20]];c=plain
 for k in ks:c=enc(c,k)
 controls.append(dict(label=label,plaintext=plain,ciphertext=c,planted_keys=ks))
(B/'fresh-controls.json').write_text(json.dumps(controls,indent=2)+'\n')
def run(c):
 r=solve(c['plaintext'],c['ciphertext'],[21,19,20],30000,backend='eager');r.update(control=c,blind=True);(B/f"control-{c['label']}.json").write_text(json.dumps(r,indent=2)+'\n');return r
if __name__=='__main__':
 k=controls[0];r=solve(k['plaintext'],k['ciphertext'],[21,19,20],5000,known_keys=k['planted_keys'],backend='eager');assert r['status']=='sat';(B/'known-key-encoding.json').write_text(json.dumps(r,indent=2)+'\n');print('known-key',r['status'],flush=True)
 with concurrent.futures.ProcessPoolExecutor(max_workers=2)as pool:results=list(pool.map(run,controls))
 for r in results:print(r['control']['label'],r['status'],r['seconds'],flush=True)
 if not all(r['status']=='sat'for r in results):print('Control recovery failed; no actual search executed',flush=True)
 else:
  for v in variants:
   r=solve(p,v['ciphertext'],[21,19,20],30000,backend='eager');r['hypothetical_correction']=v;(B/f"target-P{v['changed_position1']}-F.json").write_text(json.dumps(r,indent=2)+'\n');print(v['changed_position1'],r['status'],flush=True)
