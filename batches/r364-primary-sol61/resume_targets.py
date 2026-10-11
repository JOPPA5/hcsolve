from pathlib import Path
import json,concurrent.futures
from exact_cover import solve
p=Path(__file__).resolve().parent;repo=p.parents[1]
def worker(job):
 mode,n,reading,omit,c,errors,template=job;align=[n]*3 if mode=='constant'else[n,n+1,n+2]
 r=solve(template,c,[21,19,20],60000,errors=errors,alignments=align,backend='eager');r.update(stage='conditional-target',mode=mode,n=n,alignment=align,reading=reading,omitted_group=omit,assumptions='unproved cover quote, fixed four sentence X, unknown final filler, omit group 3; arbitrary key permutations constrained only by daily column0 ranks');rows=[r]
 if r['status']=='sat':
  other=solve(template,c,[21,19,20],60000,errors=errors,alignments=align,backend='eager',blocked_keys=[r['keys']]);other.update(stage='blocked-first-keyset-alternative',mode=mode,n=n,reading=reading);rows.append(other)
 return rows
if __name__=='__main__':
 out=p/'results.jsonl';past=[json.loads(x)for x in out.read_text().splitlines()];done={(r['mode'],r['n'],r['reading'])for r in past if r['stage']=='conditional-target'};data=json.loads((repo/'batches/constraint-sol61/target-cases.json').read_text());jobs=[]
 for mode,ns in [('constant',range(1,20)),('progressive',range(1,19))]:
  for n in ns:
   for reading,omit,c,errors in data['cases']:
    if(mode,n,reading)not in done:jobs.append((mode,n,reading,omit,c,errors,data['template']))
 print('Resuming',len(jobs),'unfinished cases; completed records retained',len(done),flush=True)
 with concurrent.futures.ProcessPoolExecutor(max_workers=4)as pool:
  futures=[pool.submit(worker,j)for j in jobs]
  for future in concurrent.futures.as_completed(futures):
   rows=future.result()
   for r in rows:
    with out.open('a')as f:f.write(json.dumps(r)+'\n')
    print(json.dumps({k:r[k]for k in ['stage','mode','n','reading','status','seconds']}),flush=True)
