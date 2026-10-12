from pathlib import Path
import json,random,os,hashlib
from engine import solve
B=Path(__file__).resolve().parent;(B/'owned-pid.txt').write_text(str(os.getpid())+'\n')
source=Path('batches/r364-review-collation-sol61/variants.json');v=json.loads(source.read_text());p=v['four_sentence_X_template64']+'x';cts=[r['omit3']for r in v['variants']if r['name']in['EXCUV','EXCVU']];widths=(16,16,17)
def save(name,obj):(B/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n')
def independent(p,key):return ''.join(p[row*len(key)+col]for col in key for row in range((len(p)+len(key)-1)//len(key))if row*len(key)+col<len(p))
def verify(result):
 if result['status']!='sat':return
 pred=result['conditional_plaintext']
 for key in result['keys']:pred=independent(pred,key)
 assert pred==result['selected_ciphertext']
 for key in reversed(result['keys']):
  out=['']*65;at=0
  for col in key:
   for i in range(col,65,len(key)):out[i]=pred[at];at+=1
  pred=''.join(out)
 assert pred==p;result['independent_full65_encoder_inverse']=True
seed=3641616171201;rng=random.Random(seed);n=rng.randrange(1,17);keys=[];c=p
for w in widths:
 key=rng.sample(range(1,w),w-1);key.insert(n-1,0);keys.append(key);c=independent(c,key)
a=list(c);u=c.index('u');vv=c.index('v');a[u],a[vv]=a[vv],a[u];variants=[''.join(a),c]
save('control-truth',dict(plaintext=p,keys=keys,ciphertext=c,variants=variants,n=n,seed=seed,truth_keys_n_not_supplied=True))
control=solve(p,variants,widths=widths,seconds=120);verify(control)
if control['status']=='sat':control.update(all_planted_keys_recovered=control['keys']==keys,recovered_true_n=control['recovered_n']==n,selected_true_variant=control['selected_ciphertext']==c)
save('control',control);print('control',control['status'],control['seconds'],flush=True)
if control['status']!='sat':
 control=solve(p,variants,widths=widths,rank_partition=True,rank_cap=8);verify(control)
 if control['status']=='sat':control.update(all_planted_keys_recovered=control['keys']==keys,recovered_true_n=control['recovered_n']==n,selected_true_variant=control['selected_ciphertext']==c)
 save('partition-control',control);print('partition control',control['status'],flush=True)
if control['status']=='sat':
 target=solve(p,cts,widths=widths,rank_partition=True,rank_cap=15);verify(target);target.update(conditional_quote=True,fixed_end_X=True,source_union=['EXCUV','EXCVU'],omitted_group='ITPKA');save('target',target);print('target',target['status'],flush=True)
 if target['status']=='sat':
  second=solve(p,cts,widths=widths,rank_partition=True,rank_cap=8,blocked_keys=target['keys']);verify(second);save('second-witness',second)
else:print('No actual: blind calibration gate failed.',flush=True)
save('hashes',{str(f):hashlib.sha256(f.read_bytes()).hexdigest()for f in[source,Path('ciphers/hcp-364/source/cryptogram.jpg'),B/'engine.py']})
