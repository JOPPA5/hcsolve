from pathlib import Path
import importlib.util,json,random,os,hashlib
B=Path(__file__).resolve().parent;(B/'owned-pid.txt').write_text(str(os.getpid())+'\n')
original=B.parent/'engine.py';copy=original.read_text().replace('q0=N//w0;t=','q0=N//w0;assert q0>=2 and N>=max(widths);t=');(B/'engine.py').write_text(copy);sp=importlib.util.spec_from_file_location('extension',B/'engine.py');e=importlib.util.module_from_spec(sp);sp.loader.exec_module(e)
source=Path('batches/r364-review-collation-sol61/variants.json');data=json.loads(source.read_text());p=data['four_sentence_X_template64']+'x';cts=[v['omit3']for v in data['variants']if v['name']in['EXCUV','EXCVU']]
def save(name,obj):(B/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n')
def enc(s,key):return ''.join(s[row*len(key)+col]for col in key for row in range((len(s)+len(key)-1)//len(key))if row*len(key)+col<len(s))
def verify(result):
 if result['status']!='sat':return
 pred=p
 for key in result['keys']:pred=enc(pred,key)
 assert pred==result['selected_ciphertext']
 for key in reversed(result['keys']):
  out=['']*65;at=0
  for col in key:
   for row in range((65+len(key)-1)//len(key)):
    i=row*len(key)+col
    if i<65:out[i]=pred[at];at+=1
  pred=''.join(out)
 assert pred==p and all(k.index(0)+1==result['recovered_n']for k in result['keys']);result['independent_full65_encoder_inverse']=True
summary=[]
for w in range(18,23):
 widths=(16,16,w);seed=364161600000+w;rng=random.Random(seed);n=rng.randrange(1,17);keys=[];c=p
 for width in widths:
  key=rng.sample(range(1,width),width-1);key.insert(n-1,0);keys.append(key);c=enc(c,key)
 a=list(c);u=c.index('u');v=c.index('v');a[u],a[v]=a[v],a[u];variants=[''.join(a),c]
 save(f'width{w}-control-truth',dict(plaintext=p,ciphertext=c,variants=variants,keys=keys,n=n,seed=seed,widths=widths,truth_keys_n_not_supplied=True))
 control=e.solve(p,variants,widths=widths,seconds=30);verify(control)
 if control['status']=='sat':control.update(all_planted_keys_equal=control['keys']==keys,true_n_recovered=control['recovered_n']==n,true_variant_recovered=control['selected_ciphertext']==c)
 save(f'width{w}-control',control);print('width',w,'control',control['status'],round(control['seconds'],2),flush=True)
 row=dict(widths=widths,control_status=control['status'],control_seconds=control['seconds'])
 if control['status']=='sat':
  target=e.solve(p,cts,widths=widths,rank_partition=True,rank_cap=15);verify(target);target.update(conditional_quote=True,fixed_end_X=True,source_union=['EXCUV','EXCVU'],omitted_group='ITPKA');save(f'width{w}-target',target);print('width',w,'target',target['status'],round(target['seconds'],2),flush=True);row.update(target_status=target['status'],target_seconds=target['seconds'])
  if target['status']=='sat':
   save(f'width{w}-second-witness',e.solve(p,cts,widths=widths,rank_partition=True,rank_cap=8,blocked_keys=target['keys']))
 else:row['target_status']='NOT_RUN_failed_calibration'
 summary.append(row);save('summary',summary)
save('hashes',{str(f):hashlib.sha256(f.read_bytes()).hexdigest()for f in[source,Path('ciphers/hcp-364/source/cryptogram.jpg'),B/'engine.py']})
