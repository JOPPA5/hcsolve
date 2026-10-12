from pathlib import Path
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
import sys,json,random,hashlib
sys.path.insert(0,str(Path('batches/r364-equal16-corrected-sol61').resolve()))
from exact_cover_insert import solve
b=Path(__file__).resolve().parent;source=Path('batches/r364-review-collation-sol61/variants.json');v=json.loads(source.read_text());sentences=v['reply_sentence_templates'];raw=next(x['omit3']for x in v['variants']if x['name']=='EXCUU');positions=[i for i,ch in enumerate(raw)if ch=='u'];variants=[raw[:i]+'v'+raw[i+1:]for i in positions]
def prep(mask):
 s=''
 for j,word in enumerate(sentences):s+=word+('x'if j<3 and mask&(1<<j)else'')
 s+='x'*(5-mask.bit_count());return s
# Literal optional markers at all four sentence ends, followed by ordinary padding.
all_subsets=[];deduplicated={}
for subset in range(16):
 marked=''.join(word+('x'if subset&(1<<j)else'')for j,word in enumerate(sentences));padding=(-len(marked))%5;prepared=marked+'x'*padding
 all_subsets.append(dict(subset=subset,markers=[bool(subset&(1<<j))for j in range(4)],marked_length=len(marked),padding=padding,p=prepared))
 if len(prepared)==65:deduplicated.setdefault(prepared,[]).append(subset)
assert len(deduplicated)==8 and sum(len(z)for z in deduplicated.values())==15
preps={mask:prep(mask)for mask in range(7)};assert set(preps.values())==set(deduplicated)-{prep(7)};assert len(set(preps.values()))==7 and all(len(p)==65 and Counter(p)==Counter(variants[0])for p in preps.values());assert prep(7)==v['four_sentence_X_template64']+'x'
def encode(p,keys):
 for k in keys:p=''.join(p[i]for col in k for i in range(col,len(p),len(k)))
 return p
def inverse(c,keys):
 for k in keys[::-1]:
  a=['']*len(c);at=0
  for col in k:
   for i in range(col,len(c),len(k)):a[i]=c[at];at+=1
  c=''.join(a)
 return c
def verify(r,p,raw):
 if r['status']!='sat':return
 ct=r['selected_ciphertext_variant'];assert r['conditional_plaintext']==p and encode(p,r['keys'])==ct and inverse(ct,r['keys'])==p
 literal=inverse(raw,r['keys']);assert encode(literal,r['keys'])==raw;cd=[i for i,(a,c)in enumerate(zip(raw,ct))if a!=c];pd=[i for i,(a,c)in enumerate(zip(literal,p))if a!=c];assert len(cd)==len(pd)==1 and raw[cd[0]]=='u'and ct[cd[0]]=='v'and literal[pd[0]]=='u'and p[pd[0]]=='v';r.update(raw_literal_plaintext65=literal,raw_literal_reencode_exact=True,independent_selected_encoder_inverse=True,literal_ciphertext_mismatch_0based=cd,literal_plaintext_mismatch_0based=pd)
def alignment(family,n):return [n]*3 if family=='common'else[n,n+1,n+2]
def target(case):
 mask,family,n=case;f=b/f'target-{mask}-{family}-{n}.json'
 if f.exists():return json.loads(f.read_text())
 p=preps[mask];r=solve(p,variants[0],[16]*3,15000,alignments=alignment(family,n),backend='eager',cipher_variants=variants);verify(r,p,raw);r.update(mask=mask,mask_bits_first3=[bool(mask&(1<<j))for j in range(3)],tail_X=5-mask.bit_count(),family=family,n=n,plaintext=p,source_error_hypothesis=True);f.write_text(json.dumps(r,indent=2)+'\n');return r
if __name__=='__main__':
 (b/'input.json').write_text(json.dumps(dict(source=str(source),sha256=hashlib.sha256(source.read_bytes()).hexdigest(),raw=raw,changed_U_positions_0based=positions,cipher_variants=variants,preparations=preps,excluded_mask111_already_covered=prep(7),final_period_X_merged_with_tail=True,all16_optional_subsets=all_subsets,deduplicated_65_strings=deduplicated,all_tail_case_from_final_sentence_marker_and4_padding=True),indent=2)+'\n')
 controls=[]
 for j,(mask,family,plantedn)in enumerate([(0,'common',8),(5,'progressive',7)]):
  f=b/f'control{j}.json'
  if f.exists():result=json.loads(f.read_text())
  else:
   p=prep(mask);rng=random.Random(364716612+j);keys=[]
   for n in alignment(family,plantedn):k=rng.sample(range(1,16),15);k.insert(n-1,0);keys.append(k)
   ct=encode(p,keys);err=[i for i,ch in enumerate(ct)if ch=='v'][j];observed=ct[:err]+'u'+ct[err+1:];cv=[observed[:i]+'v'+observed[i+1:]for i,ch in enumerate(observed)if ch=='u'];(b/f'control{j}-input.json').write_text(json.dumps(dict(p=p,observed=observed,variants=cv,family=family,blind_n_search=True),indent=2)+'\n');(b/f'control{j}-truth.json').write_text(json.dumps(dict(keys=keys,ct=ct,error_0based=err,plantedn=plantedn,mask=mask,seed=364716612+j),indent=2)+'\n');trials=[];result=None
   for n in range(1,17 if family=='common' else 15):
    r=solve(p,cv[0],[16]*3,20000,alignments=alignment(family,n),backend='eager',cipher_variants=cv);verify(r,p,observed);r.update(n=n,known_key_seed=False,known_error_position=False);trials.append(r);(b/f'control{j}-trials.json').write_text(json.dumps(trials,indent=2)+'\n')
    if r['status']=='sat':result=r;break
   assert result is not None;result.update(full_plaintext_exact=result['conditional_plaintext']==p,selected_variant_is_planted=result['selected_ciphertext_variant']==ct,true_key_identity_not_required=True);f.write_text(json.dumps(result,indent=2)+'\n')
  assert result['status']=='sat'and result['full_plaintext_exact']and result['selected_variant_is_planted'];controls.append(result);print('control',j,result['status'],'foundn',result['n'],flush=True)
 (b/'controls.json').write_text(json.dumps(controls,indent=2)+'\n')
 cases=[(mask,fam,n)for mask in range(7)for fam,stop in [('common',17),('progressive',15)]for n in range(1,stop)];results=[]
 with ProcessPoolExecutor(max_workers=2)as pool:
  for r in pool.map(target,cases):
   results.append(r);(b/'targets.json').write_text(json.dumps(results,indent=2)+'\n');print('target',r['mask'],r['family'],r['n'],r['status'],flush=True)
 (b/'summary.json').write_text(json.dumps(dict(total=len(results),statuses=dict(Counter(r['status']for r in results)),cases_expected=210,controls=len(controls),workers=2),indent=2)+'\n')
