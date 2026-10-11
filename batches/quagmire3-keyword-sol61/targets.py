from pathlib import Path
import json,subprocess,time,concurrent.futures,threading,hashlib
# Reuse batch-only independent codecs/model-score checks without triggering controls.
exec((Path(__file__).parent/'run_controls.py').read_text().split('results=[]')[0])
source=R/'ciphers/hcp-334/work/transcription.txt';groups=source.read_text().split();assert len(groups)==30 and groups[18]=='FWXX?' and groups[14]=='?DZQR';source_initial=hashlib.sha256(source.read_bytes()).hexdigest();lock=threading.Lock()
def job(item):
 gap,T=item;g=groups.copy();g[18]='FWXX'[:gap]+'?'+'FWXX'[gap:];ct=''.join(g).lower();assert len(ct)==150 and ct.count('?')==2 and ct.count('w')==1;folder=P/'targets'/f'gap{gap}-T{T}';folder.mkdir(parents=True,exist_ok=True);cipher=folder/'cipher.txt';cipher.write_text(ct+'\n');prefix=folder/'candidates';started=time.monotonic()
 if not (folder/'candidates-five.txt').exists():
  with (folder/'progress.txt').open('w') as log:subprocess.run([str(P/'search'),str(M),str(cipher),str(T),str(P/'alphabets.tsv'),str(prefix)],stdout=log,stderr=log,check=True)
 stages={label:parse(folder/f'candidates-{label}.txt',ct,n) for label,n in [('screen',4),('four',4),('five',5)]};chosen=stages['five'][0];r=dict(**chosen,period=T,FWXX_unknown_slot0=gap,erasure_positions0=[70,90+gap],ciphertext=ct,seconds=time.monotonic()-started,selection='samefixedcontrolpipeline, highestgeneric5gramscore',framing_and_keyword_model_conditional=True,source_glyphs_unchanged=True,missing_plaintext_not_inferred=True,stages=stages);(folder/'result.json').write_text(json.dumps(r,indent=2)+'\n')
 with lock:
  with (P/'target-results.jsonl').open('a') as f:f.write(json.dumps(r)+'\n')
  print(gap,T,chosen['score'],chosen['keyword'],chosen['plaintext'],flush=True)
 return r
prior={(r['FWXX_unknown_slot0'],r['period']) for r in (json.loads(x) for x in (P/'target-results.jsonl').read_text().splitlines())} if (P/'target-results.jsonl').exists() else set()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:list(pool.map(job,[(gap,T) for gap in range(5) for T in [3,9] if (gap,T) not in prior]))
assert hashlib.sha256(source.read_bytes()).hexdigest()==source_initial
rows=[json.loads(x) for x in (P/'target-results.jsonl').read_text().splitlines()];summary=dict(branches=len(rows),top_by_period={str(T):sorted([r for r in rows if r['period']==T],key=lambda r:r['score'],reverse=True)[:3] for T in [3,9]},pipeline='samefixedcontrolmanifest',source_working_sha256=source_initial,source_working_unchanged=True,source_image_unchanged=hashlib.sha256((R/'ciphers/hcp-334/source/cryptogram.jpg').read_bytes()).hexdigest()==json.loads((P/'manifest.json').read_text())['source_sha256'],coherent_solution_claim=False,heuristic_failure_not_exclusion=True)
(P/'target-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
