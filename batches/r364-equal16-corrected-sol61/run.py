from pathlib import Path
import json,random,hashlib,concurrent.futures
from exact_cover_insert import solve
b=Path(__file__).resolve().parent;source=Path('batches/r364-review-collation-sol61/variants.json');v=json.loads(source.read_text());base=v['four_sentence_X_template64'];cs=[a['omit3']for a in v['variants']if a['name']in ['EXCUV','EXCVU']]
def verify(r):
 if r['status']!='sat':return
 p=r['conditional_plaintext'];c=r['selected_ciphertext_variant'];x=p
 for k in r['keys']:x=''.join(x[i]for col in k for i in range(col,len(x),len(k)))
 assert x==c
 for k in r['keys'][::-1]:
  arr=['']*len(x);at=0
  for col in k:
   for pos in range(col,len(x),len(k)):arr[pos]=x[at];at+=1
  x=''.join(arr)
 assert x==p;assert all(k.index(0)+1==r['alignment']for k in r['keys']);r['independent_full65_encoder_inverse']=True

def target(n):
 f=b/f'target-{n}.json'
 if f.exists():return json.loads(f.read_text())
 r=solve('?'*65,cs[0],[16]*3,20000,alignments=[n]*3,backend='eager',insert_x_template=base,cipher_variants=cs);r.update(alignment=n,omitted_group=3,source_readings=['EXCUV','EXCVU'],free_fifth_x=True,conditional_visible_reply=True,known_key_seed=False);verify(r);f.write_text(json.dumps(r,indent=2)+'\n');return r
if __name__=='__main__':
 rows=[]
 for j,n in enumerate([1,8,16]):
  f=b/f'control-{n}.json'
  if f.exists():r=json.loads(f.read_text())
  else:
   rng=random.Random(6173641612+j);template=base if j else ''.join(rng.sample('abcdefghijklmnopqrstuvwxyz',26))+''.join(rng.choice('abcdefghijklmnopqrstuvwxyz')for _ in range(38));at=[0,37,64][j];p=template[:at]+'x'+template[at:];keys=[];c=p
   for _ in range(3):
    k=rng.sample(range(1,16),15);k.insert(n-1,0);keys.append(k);c=''.join(c[i]for col in k for i in range(col,len(c),16))
   a=list(c);u=c.index('u');vv=c.index('v');a[u],a[vv]=a[vv],a[u];alt=''.join(a);variants=[alt,c]if j%2 else[c,alt]
   (b/f'control-{n}-input.json').write_text(json.dumps(dict(template=template,cipher_variants=variants,alignment=n,widths=[16]*3),indent=2)+'\n');(b/f'control-{n}-truth.json').write_text(json.dumps(dict(plaintext=p,keys=keys,insertion=at,ciphertext=c),indent=2)+'\n')
   r=solve('?'*65,variants[0],[16]*3,20000,alignments=[n]*3,backend='eager',insert_x_template=template,cipher_variants=variants);r.update(alignment=n,known_key_seed=False);verify(r);r.update(exact_planted_plaintext=r.get('conditional_plaintext')==p,chosen_variant_is_planted=r.get('selected_ciphertext_variant')==c);f.write_text(json.dumps(r,indent=2)+'\n')
  rows.append(r);print('control',n,r['status'],r['seconds'],r.get('exact_planted_plaintext'),flush=True)
 (b/'controls.json').write_text(json.dumps(rows,indent=2)+'\n')
 if not all(r['status']=='sat'and r['exact_planted_plaintext']for r in rows):print('No target: full control gate failed.',flush=True);raise SystemExit()
 out=[]
 with concurrent.futures.ProcessPoolExecutor(max_workers=3)as pool:
  for r in pool.map(target,range(1,17)):
   out.append(r);(b/'targets.json').write_text(json.dumps(out,indent=2)+'\n');print('target',r['alignment'],r['status'],r['seconds'],flush=True)
 (b/'provenance.json').write_text(json.dumps(dict(source_variants=str(source),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),copied_solver='batches/r364-corrected-double-sol61/exact_cover_insert.py',structural_pruning='N65 width16: unique long physicalcol0, fixed shared rank fixes every length pattern; only actual boundaries retained',old_gap='sweep_aligned_equal.py used ERCUV and fixed suffix filler, not correctedEXC/freefifthX'),indent=2)+'\n')
