from pathlib import Path
import random,json,os,hashlib
from engine import solve
B=Path(__file__).resolve().parent;(B/'owned-pid.txt').write_text(str(os.getpid())+'\n')
source=Path('batches/r364-review-collation-sol61/variants.json');v=json.loads(source.read_text());base=v['four_sentence_X_template64'];cts=[r['omit3']for r in v['variants']if r['name']in['EXCUV','EXCVU']];widths=[16,17,18];align=[11]*3
def save(name,obj):(B/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n')
def independent_enc(s,key):return ''.join(s[row*len(key)+col]for col in key for row in range((len(s)+len(key)-1)//len(key))if row*len(key)+col<len(s))
def independent_verify(result):
 if result['status']!='sat':return
 p=result['conditional_plaintext'];c=result['selected_ciphertext_variant'];pred=p
 for key in result['keys']:pred=independent_enc(pred,key)
 assert pred==c
 for key in reversed(result['keys']):
  out=['']*len(pred);at=0
  for col in key:
   for i in range(col,len(pred),len(key)):out[i]=pred[at];at+=1
  pred=''.join(out)
 assert pred==p and all(k.index(0)+1==11 for k in result['keys']);result['independent_full65_encoder_inverse']=True
save('source-inputs',dict(variant_source=str(source),variant_source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),cipher_variants=cts,template64=base,widths=widths,alignments=align,quote_is_conditional=True,n11_is_declared_hypothesis_not_header_inference=True))
for mode,seed,at in [('free-X',364617181201,37),('fixed-end-X',364617181202,64)]:
 rng=random.Random(seed);p=base[:at]+'x'+base[at:];keys=[];c=p
 for w in widths:
  key=rng.sample(range(1,w),w-1);key.insert(10,0);keys.append(key);c=independent_enc(c,key)
 a=list(c);u=c.index('u');vv=c.index('v');a[u],a[vv]=a[vv],a[u];alternative=''.join(a);variants=[alternative,c]
 save(mode+'-control-truth',dict(plaintext=p,keys=keys,insertion=at,ciphertext=c,seed=seed,variants=variants,alignment=11,truekeys_not_supplied=True,true_insertion_not_supplied=True,true_variant_not_supplied=True))
 if mode=='free-X':result=solve('?'*65,variants[0],widths,120000,alignments=align,backend='eager',insert_x_template=base,cipher_variants=variants)
 else:result=solve(p,variants[0],widths,120000,alignments=align,backend='eager',cipher_variants=variants)
 independent_verify(result);result.update(exact_planted_plaintext=result.get('conditional_plaintext')==p,selected_variant_is_planted=result.get('selected_ciphertext_variant')==c,all_planted_keys_recovered=result.get('keys')==keys,mode=mode,n11_declared=True)
 save(mode+'-control',result);print(mode,'control',result['status'],result['seconds'],flush=True)
 positive=result['status']=='sat'and result['exact_planted_plaintext']and result['selected_variant_is_planted']
 if not positive:continue
 if mode=='free-X':target=solve('?'*65,cts[0],widths,180000,alignments=align,backend='eager',insert_x_template=base,cipher_variants=cts)
 else:target=solve(base+'x',cts[0],widths,180000,alignments=align,backend='eager',cipher_variants=cts)
 independent_verify(target);target.update(mode=mode,corrected_source_union=['EXCUV','EXCVU'],omitted_group='ITPKA',n11_declared_not_inferred=True,conditional_quote=True);save(mode+'-target',target);print(mode,'target',target['status'],target['seconds'],flush=True)
 if target['status']=='sat':
  if mode=='free-X':second=solve('?'*65,cts[0],widths,60000,alignments=align,backend='eager',insert_x_template=base,cipher_variants=cts,blocked_keys=[target['keys']])
  else:second=solve(base+'x',cts[0],widths,60000,alignments=align,backend='eager',cipher_variants=cts,blocked_keys=[target['keys']])
  independent_verify(second);save(mode+'-second-witness',second)
 # A passed complete free-X branch already includes the fixed-end subset.
 if mode=='free-X':break
save('hashes',{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in[Path('ciphers/hcp-364/source/cryptogram.jpg'),source,B/'engine.py']})
