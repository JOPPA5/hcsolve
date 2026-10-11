from pathlib import Path
import json, math, collections, random
b=Path(__file__).resolve().parent;r=b.parents[1];truth=json.load(open(b/'control.json'));geometry=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'));a=geometry['adjacent_distances'];cts=(b/'ciphertexts.txt').read_text().split();plains=[m['plaintext'] for m in truth['messages']]
models={}
for n in range(2,6):
 p=r/f'batches/kryha-mask-sol61/model{n}.tsv' if n<4 else r/f'ciphers/hcp-350/work/ring-{n}grams.tsv'
 models[n]={s:float(v) for s,v in (line.split() for line in p.read_text().splitlines())}
def score(texts):return sum(w*sum(models[n].get(t[i:i+n],-n) for i in range(len(t)-n+1)) for t in texts for n,w in [(2,.1),(3,.15),(4,.4),(5,.8)])
def jumps(holes):
 assert len(holes)==26 and len(set(holes))==26
 z=[]
 for j,h in enumerate(holes):
  d=0;x=h
  while True:
   d+=a[x];x=(x+1)%52
   if x==holes[(j+1)%26]:break
  z.append(d)
 assert sum(z)==179;return z
checked=0;maxerr=0;bestmatch=0

def check(row):
 global checked,maxerr,bestmatch
 P=row['input_slots'];O=row['output_positions'];holes=row['holes'];texts=row['plaintexts'];assert sorted(P)==sorted(O)==list(range(26));steps=jumps(holes);pi={chr(97+p):i for i,p in enumerate(P)};oi={p:chr(97+i) for i,p in enumerate(O)}
 for ct,pt in zip(cts,texts):
  d=0;enc='';dec=''
  for i,(c,p) in enumerate(zip(ct,pt)):
   enc+=oi[(pi[p]+d)%26];dec+=chr(97+P[(O[ord(c)-97]-d)%26]);d=(d+steps[i%26])%26
  assert len(pt)==len(ct) and enc==ct and dec==pt
 err=abs(score(texts)-row['score']);maxerr=max(maxerr,err);assert err<.13,(err,row['score']);checked+=1;bestmatch=0

folder=b/'framing355-control';truth=json.load(open(folder/'control.json'));plains=[m['plaintext'] for m in truth['messages']];cts=(folder/'ciphertexts.txt').read_text().split();rows=[]
for seed in range(4):
 for it in range(2):
  stage=folder/f'local-seed{seed}'/f'pass{it}'
  for file in ('local.json','result.json'):
   z=json.load(open(stage/file));check(z);rows.append(z)
exact=[z for z in rows if z['plaintexts']==plains];bestmatch=max(sum(c==p for a,d in zip(z['plaintexts'],plains) for c,p in zip(a,d)) for z in rows)
report=dict(status='PASS exact355pair' if exact else 'FAIL local rotation355pair; no cropped target allowed',paired_rows_checked=checked,message_reencryptions=checked*2,max_score_error=maxerr,best_letter_matches_out_of710=bestmatch,true_language_score=score(plains),exact_rows=len(exact),final_scores=[z['score'] for z in json.load(open(folder/'local-results.json'))])
if exact:report['exact_candidate']=exact[0]
(folder/'local-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='exact_candidate'},indent=2))
