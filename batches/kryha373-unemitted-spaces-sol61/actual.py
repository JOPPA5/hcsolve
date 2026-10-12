from pathlib import Path
from itertools import product
from collections import Counter
import json,time,hashlib
from crt import solve
from schedule import prepare
from controls import check
b=Path(__file__).resolve().parent
src=Path('batches/kryha373-collation-sol61/ciphertext650.txt');base=src.read_text().strip();f=b/'actual-results.jsonl'
seen=set()
if f.exists():
 for line in f.read_text().splitlines():
  r=json.loads(line);seen.add(tuple(r['case_id']))
for unamended,ji,extra,policy,omit,g53,g90 in product([False,True],[False,True],[1,2],['lexical','whitespace'],[0,5],['l','i'],['e','a']):
 ca=prepare(unamended=unamended,ji=ji,extra=extra,policy=policy);p=ca['p'];ix=ca['press_indices'];cs=list(base);cs[52]=g53;cs[89]=g90;c=''.join(cs)[omit:omit+len(p)]
 for m in range(2,53):
  cid=[unamended,ji,extra,policy,omit,g53,g90,m]
  if tuple(cid)in seen:continue
  r=solve(p,c,m,2000,press_indices=ix);check(r,p,c,ix);r.update(case_id=cid,p=p,c=c,press_indices=ix,source_omit=omit)
  with f.open('a')as out:out.write(json.dumps(r)+'\n')
  if r['status']=='sat':print('SAT',cid,flush=True)
 print('finished variant',cid[:-1],flush=True)
rows=[json.loads(x)for x in f.read_text().splitlines()];(b/'actual-summary.json').write_text(json.dumps(dict(total=len(rows),statuses=dict(Counter(r['status']for r in rows)),sat_cases=[r['case_id']for r in rows if r['status']=='sat'],unknown_cases=[r['case_id']for r in rows if r['status']=='unknown'],timeout_ms=2000,source_sha256=hashlib.sha256(src.read_bytes()).hexdigest()),indent=2)+'\n')
