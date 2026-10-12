from pathlib import Path
from collections import Counter
import sys,json,random,hashlib
sys.path.insert(0,str(Path('batches/r364-equal16-corrected-sol61').resolve()))
from exact_cover_insert import solve
b=Path(__file__).resolve().parent;source=Path('batches/r364-review-collation-sol61/variants.json');v=json.loads(source.read_text());base=v['four_sentence_X_template64'];raw=next(x['omit3']for x in v['variants']if x['name']=='EXCUU');assert len(raw)==65
# Original group12 becomes body group11 after omission of original group3.
excluded=[53,54];assert raw[50:55]=='excuu';positions=[i for i,ch in enumerate(raw)if ch=='u'and i not in excluded];variants=[raw[:i]+'v'+raw[i+1:]for i in positions];assert all(Counter(c)==Counter(base)+Counter({'x':1})for c in variants)
(b/'input.json').write_text(json.dumps(dict(source=str(source),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),raw_ciphertext=raw,base_template=base,excluded_0based=excluded,change_positions_0based=positions,variants=variants,inventory_exact=True),indent=2)+'\n')
def encode(p,keys):
 for k in keys:p=''.join(p[i]for col in k for i in range(col,len(p),len(k)))
 return p
def inverse(c,keys):
 for k in keys[::-1]:
  arr=['']*len(c);at=0
  for col in k:
   for i in range(col,len(c),len(k)):arr[i]=c[at];at+=1
  c=''.join(arr)
 return c
def verify(r,raw):
 if r['status']!='sat':return
 selected=r['selected_ciphertext_variant'];pt=r['conditional_plaintext'];assert encode(pt,r['keys'])==selected and inverse(selected,r['keys'])==pt
 literal=inverse(raw,r['keys']);assert encode(literal,r['keys'])==raw;ctdiff=[i for i,(a,c)in enumerate(zip(raw,selected))if a!=c];ptdiff=[i for i,(a,c)in enumerate(zip(literal,pt))if a!=c];assert len(ctdiff)==len(ptdiff)==1 and raw[ctdiff[0]]=='u'and selected[ctdiff[0]]=='v'and literal[ptdiff[0]]=='u'and pt[ptdiff[0]]=='v'
 r.update(raw_literal_plaintext65=literal,raw_literal_reencode_exact=True,independent_selected_encoder_inverse=True,literal_ciphertext_mismatch_positions_0based=ctdiff,literal_plaintext_mismatch_positions_0based=ptdiff)
controls=[]
for j,align in enumerate([[8]*3,[16]*3,[8,9,10]]):
 f=b/f'control{j}.json'
 if f.exists():r=json.loads(f.read_text())
 else:
  rng=random.Random(364865261+j);insertion=[21,47,9][j];p=base[:insertion]+'x'+base[insertion:];keys=[]
  for n in align:k=rng.sample(range(1,16),15);k.insert(n-1,0);keys.append(k)
  c=encode(p,keys);error=[i for i,ch in enumerate(c)if ch=='v'][j%3];observed=c[:error]+'u'+c[error+1:];cv=[observed[:i]+'v'+observed[i+1:]for i,ch in enumerate(observed)if ch=='u'];(b/f'control{j}-input.json').write_text(json.dumps(dict(observed=observed,alignments=align,variants=cv,all_U_positions_searched=True,template=base),indent=2)+'\n');(b/f'control{j}-truth.json').write_text(json.dumps(dict(p=p,keys=keys,ciphertext=c,injected_V_to_U_0based=error,seed=364865261+j),indent=2)+'\n')
  r=solve('?'*65,cv[0],[16]*3,60000,alignments=align,backend='eager',insert_x_template=base,cipher_variants=cv);verify(r,observed);r.update(exact_planted_plaintext=r.get('conditional_plaintext')==p,selected_variant_is_planted=r.get('selected_ciphertext_variant')==c,true_key_identity_not_required=True);f.write_text(json.dumps(r,indent=2)+'\n')
 controls.append(r);print('control',j,r['status'],r.get('exact_planted_plaintext'),flush=True)
(b/'controls.json').write_text(json.dumps(controls,indent=2)+'\n');assert all(r['status']=='sat'and r['exact_planted_plaintext']and r['selected_variant_is_planted']for r in controls)
cases=[('common',n,[n]*3)for n in range(1,17)]+[('progressive',n,[n,n+1,n+2])for n in range(1,15)]
results=[]
for family,n,align in cases:
 f=b/f'target-{family}-{n}.json'
 if f.exists():r=json.loads(f.read_text())
 else:
  r=solve('?'*65,variants[0],[16]*3,15000,alignments=align,backend='eager',insert_x_template=base,cipher_variants=variants);verify(r,raw);r.update(family=family,n=n,alignments=align,source_error_hypothesis=True,actual_source_modified=False);f.write_text(json.dumps(r,indent=2)+'\n')
 results.append(r);(b/'targets.json').write_text(json.dumps(results,indent=2)+'\n');print('target',family,n,r['status'],flush=True)
(b/'summary.json').write_text(json.dumps(dict(total=len(results),statuses=dict(Counter(r['status']for r in results)),control_statuses=[r['status']for r in controls],variant_count=len(variants)),indent=2)+'\n')
