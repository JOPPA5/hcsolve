from pathlib import Path
from exact_cover_insert import solve
import json,time,concurrent.futures
B=Path(__file__).resolve().parent;data=json.loads((B/'variants.json').read_text());template=data['four_sentence_X_template64'];variants=[v['omit3']for v in data['variants']if v['name']in['EXCUV','EXCVU']];assert len(variants)==2
cases=[dict(mode=mode,n=n,alignment=[n]*3 if mode=='constant'else[n,n+1,n+2])for mode,ns in [('constant',range(1,20)),('progressive',range(1,19))]for n in ns]
def work(case):
 folder=B/f"target-{case['mode']}-{case['n']}";folder.mkdir(exist_ok=True);resultfile=folder/'result.json'
 if resultfile.exists():return json.loads(resultfile.read_text())
 r=solve('?'*65,variants[0],[21,19,20],60000,alignments=case['alignment'],backend='eager',insert_x_template=template,cipher_variants=variants);r.update(case,widths=[21,19,20],errors=0,omitted_group=3,source_endings=['EXCUV','EXCVU'],fifth_x_any_boundary=True,no_known_key_seed=True,assumptions='printed reply might be cover response; sentence X and fifth extraX preparation; group3 omitted; primary-example widths; daily column0 ranks and common orientation all conditional')
 resultfile.write_text(json.dumps(r,indent=2));return r
if __name__=='__main__':
 out=[]
 with concurrent.futures.ProcessPoolExecutor(max_workers=3)as pool:
  futures={pool.submit(work,c):c for c in cases}
  for f in concurrent.futures.as_completed(futures):
   r=f.result();out.append(r);(B/'target-results.json').write_text(json.dumps(out,indent=2));print(r['mode'],r['n'],r['status'],r['seconds'],flush=True)
 (B/'target-run-completion.json').write_text(json.dumps(dict(complete=True,cases=len(out),statuses={s:sum(r['status']==s for r in out)for s in set(r['status']for r in out)}),indent=2))
