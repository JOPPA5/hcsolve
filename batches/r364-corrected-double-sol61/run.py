from exact_cover_insert import solve,enc
from pathlib import Path
import json,random,hashlib,concurrent.futures,time
B=Path(__file__).resolve().parent
V=Path('batches/r364-review-collation-sol61/variants.json')
v=json.loads(V.read_text());base=v['four_sentence_X_template64'];cs=[r['omit3']for r in v['variants']if r['name']in['EXCUV','EXCVU']]
def verify(r):
 if r['status']!='sat':return
 p=r['conditional_plaintext'];c=r['selected_ciphertext_variant'];x=p
 for k in r['keys']:
  x=''.join(x[i]for col in k for i in range(col,len(x),len(k)))
 assert x==c
 for k in r['keys'][::-1]:
  a=['']*len(x);at=0
  for col in k:
   for pos in range(col,len(a),len(k)):a[pos]=x[at];at+=1
  x=''.join(a)
 assert x==p
 r['wrapper_independent_full65_verified']=True

def case(ws):
 r=solve('?'*65,cs[0],list(ws),15000,backend='eager',insert_x_template=base,cipher_variants=cs);verify(r)
 (B/f'target-{ws[0]}-{ws[1]}.json').write_text(json.dumps(r,indent=2)+'\n');return r
if __name__=='__main__':
 rng=random.Random(364101124);controls=[]
 for j,ws in enumerate([(16,22),(19,19),(22,16)]):
  t=base if j else ''.join(rng.sample('abcdefghijklmnopqrstuvwxyz',26))+''.join(rng.choice('abcdefghijklmnopqrstuvwxyz')for _ in range(38))
  at=[0,37,64][j];p=t[:at]+'x'+t[at:];keys=[rng.sample(range(w),w)for w in ws];c=p
  for k in keys:c=enc(c,k)
  u=c.index('u');vv=c.index('v');alt=list(c);alt[u],alt[vv]=alt[vv],alt[u];alt=''.join(alt)
  r=solve('?'*65,c,list(ws),20000,backend='eager',insert_x_template=t,cipher_variants=[c,alt]);verify(r);r.update(planted_plaintext=p,planted_keys=keys,extra_x=at,blind=True,matched_quote_template=j>0)
  controls.append(r);(B/'controls.json').write_text(json.dumps(controls,indent=2)+'\n');print('control',ws,r['status'],r['seconds'],flush=True)
  assert r['status']=='sat'
 rows=[]
 with concurrent.futures.ProcessPoolExecutor(max_workers=3)as pool:
  for r in pool.map(case,[(a,b)for a in range(16,23)for b in range(16,23)]):
   rows.append(r);(B/'results.json').write_text(json.dumps(rows,indent=2)+'\n');print('target',r['widths'],r['status'],round(r['seconds'],2),flush=True)
 (B/'provenance.json').write_text(json.dumps({'source_variants':str(V),'sha256':hashlib.sha256(V.read_bytes()).hexdigest(),'solver_copy_source':'batches/r364-review-collation-sol61/exact_cover_insert.py','model':'two ordinary irregular columnar permutations; widths 16..22 ordered; insert fifth X anywhere; exact EXCUV/EXCVU alternatives; no alignment imposed','timeout_ms':15000},indent=2)+'\n')
