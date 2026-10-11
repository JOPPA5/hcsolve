from pathlib import Path
import json,concurrent.futures
b=Path(__file__).resolve().parent;r=b.parents[1];records=[]
for n in (350,351,369):
 path=r/f'ciphers/hcp-{n}/work/transcription.txt';ct=''.join(path.read_text().lower().split());assert all('a'<=c<='z' for c in ct)
 for direction,body in [('forward',ct),('reverse',ct[::-1])]:
  rec={'label':f'target{n}-{direction}','cipher':n,'direction':direction,'length':len(body),'ciphertext':body,'source':str(path.relative_to(r)),'removed_symbols':None,'short_branch_control_failed':n==369,'model_is_conditional':'unknown26bijective rings and d_i=i; no historical machine attribution'};records.append(rec);folder=b/rec['label'];folder.mkdir(exist_ok=True);(folder/'cipher.txt').write_text(body+'\n')
(b/'targets.json').write_text(json.dumps(records,indent=2)+'\n')
ns={'__file__':str(b/'run.py')};source=(b/'run.py').read_text();exec(source[:source.index('with concurrent.futures')],ns)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(ns['work'],records))
(b/'target-results.json').write_text(json.dumps(results,indent=2)+'\n')
