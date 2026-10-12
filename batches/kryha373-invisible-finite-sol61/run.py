from pathlib import Path
import sys,json,hashlib
sys.path.insert(0,str(Path('batches/kryha373-unemitted-spaces-sol61').resolve()))
from crt import expressions
from vector import enumerate_observed
b=Path(__file__).resolve().parent;old=Path('batches/kryha373-unemitted-spaces-sol61')
def fit(p,c,ix,m):
 n=52+m;rows=[]
 for a,cc,t in zip(p,c,ix):
  r=[0]*(n+1);r[26+ord(cc)-97]+=1;r[ord(a)-97]-=1;r[52+t%m]-=1;r[-1]=179*(t//m);rows.append(r)
 for j in [0,26]:r=[0]*(n+1);r[j]=1;rows.append(r)
 e2,v2=expressions(rows,n,2);e13,v13=expressions(rows,n,13)
 if e2 is None or e13 is None:return dict(status='unsat',reason='linear CRT inconsistency')
 obs=[sorted({ord(ch)-97 for ch in s}|{0})for s in [p,c]];r=enumerate_observed(e2,v2,e13,v13,obs[0]+[26+i for i in obs[1]])
 if r['status']=='sat':
  vals=r.pop('values');P,O,K=vals[:26],vals[26:52],vals[52:]
  for ring,known in zip([P,O],obs):
   rest=iter(sorted(set(range(26))-{ring[i]for i in known}))
   for i in range(26):
    if i not in known:ring[i]=next(rest)
  assert sorted(P)==sorted(O)==list(range(26));ip={v:chr(97+i)for i,v in enumerate(P)};io={v:chr(97+i)for i,v in enumerate(O)}
  enc=''.join(io[(P[ord(a)-97]+K[t%m]+179*(t//m))%26]for a,t in zip(p,ix));dec=''.join(ip[(O[ord(a)-97]-K[t%m]-179*(t//m))%26]for a,t in zip(c,ix));assert enc==c and dec==p
  r.update(P=P,O=O,K=K,independent_full_prefix_encoder_inverse=True)
 return r
# Run existing independent676-pair audit with vector backend, writing exclusively this new batch.
s=(old/'audit-finite.py').read_text().replace('from finite import enumerate_observed','from vector import enumerate_observed').replace("'finite-independent-audit.json'","'vector-independent-audit.json'")
exec(compile(s,str(b/'audit-vector.py'),'exec'),{'__file__':str(b/'audit-vector.py')})
control=[]
for j,summary in enumerate(json.loads((old/'controls-summary.json').read_text())):
 inp=json.loads((old/f'control{j}-input.json').read_text());case=inp['case'];m=summary['sat_periods'][0];r=fit(case['p'],inp['ciphertext'],case['press_indices'],m);assert r['status']=='sat';control.append(dict(control=j,m=m,result=r))
(b/'control-validation.json').write_text(json.dumps(control,indent=2)+'\n');print('All8savedpositivecontrols accepted without truthkeys',flush=True)
unknown=[r for r in map(json.loads,(old/'actual-results.jsonl').read_text().splitlines())if r['status']=='unknown'];out=[]
for row in unknown:
 r=fit(row['p'],row['c'],row['press_indices'],row['m']);r.update(case_id=row['case_id'],original_status='unknown',original_timeout_ms=row['timeout_ms']);out.append(r);(b/'exact-results.json').write_text(json.dumps(out,indent=2)+'\n');print('actual',r['case_id'],r['status'],r.get('total'),flush=True)
(b/'provenance.json').write_text(json.dumps(dict(inputs={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in [old/'actual-results.jsonl',old/'audit-finite.py',old/'controls-summary.json']},source_batch_preserved=True,read_truth_keys=False),indent=2)+'\n')
