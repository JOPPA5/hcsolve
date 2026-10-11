from pathlib import Path
from crt import solve
import json,re,unicodedata,concurrent.futures
B=Path(__file__).resolve().parent;src=Path('batches/kryha373-collation-sol61/plaintext-typed.txt').read_text();raw=src.split('6.000')[0]
def norm(t):return ''.join(c for c in unicodedata.normalize('NFD',t.lower())if'a'<=c<='z')
words=[norm(w)for w in re.findall(r'[^\W\d_]+',raw,re.UNICODE)];cipher=Path('batches/kryha373-collation-sol61/ciphertext650.txt').read_text().strip().lower();assert len(cipher)==650
cases=[]
for sep in ['', 'x','j']:
 for ji in [False,True]:
  p=sep.join(w.replace('j','i')if ji else w for w in words)
  label=f"sep-{sep or 'none'}-naturalJ-{'I'if ji else'J'}"
  for omit in [0,5]:
   for m in range(2,53):cases.append(dict(label=label,separator=sep,natural_j_to_i=ji,omitprefix=omit,m=m,p=p,c=cipher[omit:omit+len(p)]))
(B/'preparation-cases.json').write_text(json.dumps({'published_raw_prefix':raw,'normalized_words':words,'hypotheses':[{k:v for k,v in c.items()if k not in ['m','c']}for c in cases if c['m']==2]},indent=2,ensure_ascii=False)+'\n')
def target(case):
 r=solve(case['p'],case['c'],case['m'],2000);r['case']=case
 if r['status']=='sat':
  r['second_witness']=solve(case['p'],case['c'],case['m'],1000,blocked=r)
  r['heldout']=solve(case['p'][:-20],case['c'][:-20],case['m'],1000,heldout=(case['p'],case['c']))
 return r
if __name__=='__main__':
 truth=json.loads((B/'control-truth.json').read_text());control=[]
 for m in range(2,53):
  r=solve(truth['p'],truth['c'],m,1000);control.append(r)
 (B/'control-unknown-period.json').write_text(json.dumps(control,indent=2)+'\n');assert any(r['m']==truth['m']and r['status']=='sat'for r in control);print('periodcontrol',[(r['m'],r['status'])for r in control if r['status']!='unsat'],flush=True)
 out=[]
 with concurrent.futures.ProcessPoolExecutor(max_workers=3)as pool:
  for r in pool.map(target,cases):
   out.append(r)
   if len(out)%51==0 or r['status']=='sat':
    (B/'results.json').write_text(json.dumps(out,indent=2)+'\n');print(len(out),r['case']['label'],r['case']['omitprefix'],r['m'],r['status'],r.get('heldout',{}).get('heldout_matches'),flush=True)
 (B/'results.json').write_text(json.dumps(out,indent=2)+'\n')
