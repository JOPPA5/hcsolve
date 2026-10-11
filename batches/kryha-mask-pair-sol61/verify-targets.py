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

cases=json.load(open(b/'targets.json'));summaries=[]
logs=sorted(float(line.split()[1]) for line in (r/'ciphers/hcp-350/work/ring-unigrams.tsv').read_text().splitlines())
for case in cases:
 folder=Path(case['folder']);cts=case['ciphertexts'];startcount=checked
 for row in json.load(open(folder/'bridge-ranked.json')):check(row)
 for seed in range(4):
  for it in range(4):
   stage=folder/f'bridge-seed{seed}'/f'iteration{it}';keys=list(map(int,(stage/'rings-before.txt').read_text().split()));P,O=keys[:26],keys[26:]
   for line in (stage/'beam.tsv').read_text().splitlines():
    anchor,rank,sc,h,p0,p1=line.split('\t');check(dict(score=float(sc),holes=list(map(int,h.split(','))),input_slots=P,output_positions=O,plaintexts=[p0,p1]))
   check(json.load(open(stage/'result.json')))
 # Independent physical profile check and pooled-cycle recomputation.
 for line in (folder/'mask-profiles.tsv').read_text().splitlines():
  ix,restart,sc,h,key=line.split('\t');O=list(map(int,key.rstrip(',').split(',')));steps=jumps(list(map(int,h.rstrip(',').split(','))));N=collections.Counter()
  for ct in cts:
   d=0
   for i,c in enumerate(ct):N[(O[ord(c)-97]-d)%26]+=1;d=(d+steps[i%26])%26
  counts=sorted(N[i] for i in range(26));v=sum(n*l-math.lgamma(n+1) for n,l in zip(counts,logs));assert abs(v-float(sc))<.012
 for line in (folder/'pair-cycle.tsv').read_text().splitlines():
  ix,sc,key=line.split('\t');O=list(map(int,key.split(',')));H=[collections.Counter() for _ in range(26)]
  for ct in cts:
   for i,c in enumerate(ct):H[i%26][(O[ord(c)-97]-23*(i//26))%26]+=1
  assert sum(n*(n-1)//2 for row in H for n in row.values())==int(sc)
 winners=json.load(open(folder/'bridge-results.json'));winners.sort(key=lambda z:z['score'],reverse=True);summaries.append(dict(case=folder.name,rows_checked=checked-startcount,best_complete_candidate=winners[0],reading=case['reading'],direction=case['direction'],assumptions=case['assumptions']))
report=dict(status='Exploratory restricted shared26 physical Kryha pair scout; whole plaintexts require semantic review',paired_rows_checked=checked,message_reencryptions=checked*2,physical_profiles_checked=4*256,cycle_keys_checked=4*32,max_score_error=maxerr,cases=summaries)
(b/'target-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='cases'},indent=2));print([(z['case'],z['best_complete_candidate']['score']) for z in summaries])
