from pathlib import Path
import json,hashlib,concurrent.futures
from exact_cover_insert import solve
b=Path(__file__).resolve().parent;source=Path('batches/r364-review-collation-sol61/variants.json');v=json.loads(source.read_text());base=v['four_sentence_X_template64'];variants=[a['omit3']for a in v['variants']if a['name']in ['EXCUV','EXCVU']]
def verify(r):
 if r['status']!='sat':return
 p=r['conditional_plaintext'];c=r['selected_ciphertext_variant'];x=p
 for k in r['keys']:x=''.join(x[i]for col in k for i in range(col,len(x),len(k)))
 assert x==c
 for k in r['keys'][::-1]:
  a=['']*len(x);at=0
  for col in k:
   for pos in range(col,len(x),len(k)):a[pos]=x[at];at+=1
  x=''.join(a)
 assert x==p and all(k.index(0)+1==n for k,n in zip(r['keys'],r['alignments']));r['independent_complete_encoder_inverse']=True

def attempt(template,ct,n):
 r=solve('?'*65,ct[0],[16]*3,20000,alignments=[n,n+1,n+2],backend='eager',insert_x_template=template,cipher_variants=ct);r.update(n=n,alignments=[n,n+1,n+2],planted_n_or_key_supplied=False,free_fifth_x=True);verify(r);return r

def target(n):
 f=b/f'target-{n}.json'
 if f.exists():return json.loads(f.read_text())
 r=attempt(base,variants,n);r.update(omitted_group=3,source_readings=['EXCUV','EXCVU'],conditional_visible_reply=True,no_wrap=True);f.write_text(json.dumps(r,indent=2)+'\n');return r
if __name__=='__main__':
 outcomes=[]
 for j in range(3):
  inp=json.loads((b/f'control{j}-input.json').read_text());blind=b/f'control{j}-blind.json'
  if blind.exists():r=json.loads(blind.read_text())
  else:
   checks=[];r=None
   for n in range(1,15):
    f=b/f'control{j}-n{n}.json'
    if f.exists():trial=json.loads(f.read_text())
    else:trial=attempt(inp['template'],inp['cipher_variants'],n);f.write_text(json.dumps(trial,indent=2)+'\n')
    checks.append(dict(n=n,status=trial['status'],seconds=trial['seconds']));print('control',j,'n',n,trial['status'],round(trial['seconds'],3),flush=True)
    if trial['status']=='sat':r=trial;break
   if r is None:r=dict(status='unknown'if any(z['status']=='unknown'for z in checks)else'unsat')
   r=dict(r,blind_checks=checks,n_not_in_input=True);blind.write_text(json.dumps(r,indent=2)+'\n')
  # Truth is used only after the complete blind-selected witness is frozen.
  truth=json.loads((b/f'control{j}-truth.json').read_text());audit=dict(blind_sha256=hashlib.sha256(blind.read_bytes()).hexdigest(),truth_read_after_blind_saved=True,exact_plaintext=r.get('conditional_plaintext')==truth['plaintext'],exact_ciphertext_variant=r.get('selected_ciphertext_variant')==truth['ciphertext'],recovered_n=r.get('n'),planted_n=truth['alignment'],status=r['status']);(b/f'control{j}-audit.json').write_text(json.dumps(audit,indent=2)+'\n');outcomes.append(audit)
 (b/'controls-summary.json').write_text(json.dumps(outcomes,indent=2)+'\n')
 if not all(z['status']=='sat'and z['exact_plaintext']for z in outcomes):print('No target: control gate failed.',flush=True);raise SystemExit()
 out=[]
 with concurrent.futures.ProcessPoolExecutor(max_workers=3)as pool:
  for r in pool.map(target,range(1,15)):
   out.append(r);(b/'targets.json').write_text(json.dumps(out,indent=2)+'\n');print('target',r['n'],r['status'],round(r['seconds'],3),flush=True)
 (b/'summary.json').write_text(json.dumps(dict(controls=outcomes,target_cases=len(out),target_statuses={s:sum(r['status']==s for r in out)for s in set(r['status']for r in out)},source_sha256=hashlib.sha256(source.read_bytes()).hexdigest()),indent=2)+'\n')
