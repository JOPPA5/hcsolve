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
 err=abs(score(texts)-row['score']);maxerr=max(maxerr,err);assert err<.13,(err,row['score']);checked+=1;bestmatch=max(bestmatch,sum(x==y for t,u in zip(texts,plains) for x,y in zip(t,u)))
logs=sorted(float(line.split()[1]) for line in (r/'ciphers/hcp-350/work/ring-unigrams.tsv').read_text().splitlines());profilechecks=0;profileerr=0
for g in range(6):
 folder=b/f'guess{g}';initial=json.load(open(folder/'initial-mask.json'))['ordered_holes'];steps=jumps(initial)
 for line in (folder/'profiles.txt').read_text().splitlines():
  sc,keys=line.split();O=list(map(int,keys.rstrip(',').split(',')));N=collections.Counter()
  for ct in cts:
   d=0
   for i,c in enumerate(ct):N[(O[ord(c)-97]-d)%26]+=1;d=(d+steps[i%26])%26
  counts=sorted(N[i] for i in range(26));v=sum(n*l-math.lgamma(n+1) for n,l in zip(counts,logs));err=abs(v-float(sc));profileerr=max(err,profileerr);assert err<.012;profilechecks+=1
 for row in json.load(open(folder/'ranked.json')):check(row)
 for it in range(4):
  stage=folder/f'iteration{it}';keys=list(map(int,(stage/'rings-before.txt').read_text().split()));P,O=keys[:26],keys[26:]
  for line in (stage/'beam.tsv').read_text().splitlines():
   anchor,rank,sc,h,p0,p1=line.split('\t');check(dict(score=float(sc),holes=list(map(int,h.split(','))),input_slots=P,output_positions=O,plaintexts=[p0,p1]))
  check(json.load(open(stage/'result.json')))
cycle_initialization_checks=0
for g in range(6):
 folder=b/f'cycle-guess{g}'
 for row in json.load(open(folder/'ranked.json')):check(row);cycle_initialization_checks+=1
 for it in range(4):
  stage=folder/f'iteration{it}';keys=list(map(int,(stage/'rings-before.txt').read_text().split()));P,O=keys[:26],keys[26:]
  for line in (stage/'beam.tsv').read_text().splitlines():
   anchor,rank,sc,h,p0,p1=line.split('\t');check(dict(score=float(sc),holes=list(map(int,h.split(','))),input_slots=P,output_positions=O,plaintexts=[p0,p1]));cycle_initialization_checks+=1
  check(json.load(open(stage/'result.json')));cycle_initialization_checks+=1
bridge_checks=0
for row in json.load(open(b/'bridge-ranked.json')):check(row);bridge_checks+=1
for g in range(4):
 folder=b/f'bridge-seed{g}'
 for it in range(4):
  stage=folder/f'iteration{it}';keys=list(map(int,(stage/'rings-before.txt').read_text().split()));P,O=keys[:26],keys[26:]
  for line in (stage/'beam.tsv').read_text().splitlines():
   anchor,rank,sc,h,p0,p1=line.split('\t');check(dict(score=float(sc),holes=list(map(int,h.split(','))),input_slots=P,output_positions=O,plaintexts=[p0,p1]));bridge_checks+=1
  check(json.load(open(stage/'result.json')));bridge_checks+=1
# Histogram profile independently reconstructed by physical walking, not ordinal arithmetic.
def physical_profile(O,holes):
 N=collections.Counter();steps=jumps(holes)
 for ct in cts:
  d=0
  for i,c in enumerate(ct):N[(O[ord(c)-97]-d)%26]+=1;d=(d+steps[i%26])%26
 counts=sorted(N[i] for i in range(26));return sum(n*l-math.lgamma(n+1) for n,l in zip(counts,logs))
mask_profile_scores=[];mask_profile_maxerr=0
for line in (b/'mask-profiles.tsv').read_text().splitlines():
 ix,restart,sc,h,key=line.split('\t');O=list(map(int,key.rstrip(',').split(',')));holes=list(map(int,h.rstrip(',').split(',')));v=physical_profile(O,holes);err=abs(v-float(sc));mask_profile_maxerr=max(mask_profile_maxerr,err);assert err<.012;mask_profile_scores.append(v)
trueholes=truth['active_holes_zero_based'];phase=truth['phase'];trueholes=trueholes[phase:]+trueholes[:phase];true_mask_profile=physical_profile(truth['output_positions'],trueholes)
# Diagnostic only: saved blind cyclic candidates, then planted truth and independent nulls.
def cyc(O):
 H=[collections.Counter() for _ in range(26)]
 for ct in cts:
  for i,c in enumerate(ct):H[i%26][(O[ord(c)-97]-23*(i//26))%26]+=1
 return sum(n*(n-1)//2 for row in H for n in row.values())
trueO=truth['output_positions'];cycle=[]
for line in (b/'pair-cycle.tsv').read_text().splitlines():
 ix,sc,key=line.split('\t');O=list(map(int,key.split(',')));assert sorted(O)==list(range(26));assert cyc(O)==int(sc);overlap=max(sum(o==(t+k)%26 for o,t in zip(O,trueO)) for k in range(26));cycle.append(dict(index=int(ix),score=int(sc),output_overlap_up_to_rotation=overlap,output_positions=O))
rng=random.Random(52770333);null=[]
for _ in range(1000):O=list(range(26));rng.shuffle(O);null.append(cyc(O))
results=json.load(open(b/'blind-results.json'));report=dict(status='PASS: blind physical-profile bridge recovers both full control texts; target not yet attempted',full_pair_rows_checked=checked,message_reencryptions=2*checked,profiles_checked=profilechecks,score_max_error=maxerr,profile_max_error=profileerr,true_language_score=score(plains),best_diagnostic_letter_matches_out_of_770=bestmatch,final_scores=[z['score'] for z in results],bridge_pair_rows=bridge_checks,bridge_final_scores=[z['score'] for z in json.load(open(b/'bridge-results.json'))],mask_profile=dict(rows=len(mask_profile_scores),max_error=mask_profile_maxerr,true_score=true_mask_profile,blind_min=min(mask_profile_scores),blind_max=max(mask_profile_scores)),cycle_initialization_pair_rows=cycle_initialization_checks,cycle_initialized_final_scores=[z['score'] for z in json.load(open(b/'cycle-blind-results.json'))],cycle=dict(true_score=cyc(trueO),random_null_max=max(null),blind_min=min(z['score'] for z in cycle),blind_max=max(z['score'] for z in cycle),max_output_overlap=max(z['output_overlap_up_to_rotation'] for z in cycle),all_false_outrank_truth=all(z['score']>cyc(trueO) for z in cycle),rows=cycle))
winner=json.load(open(b/'bridge-seed1/iteration3/result.json'))
rot=[k for k in range(26) if all(o==(v+k)%26 for o,v in zip(winner['output_positions'],truth['output_positions']))]
report['control_positive_key']=dict(both_full_plaintexts_exact=winner['plaintexts']==plains,output_gauge_offsets=rot,input_ring_gauge_equivalent=any(all(winner['input_slots'][(i+k)%26]==truth['input_slots'][i] for i in range(26)) for k in rot),physical_mask_exact=set(winner['holes'])==set(truth['active_holes_zero_based']),physical_start_exact=winner['holes'][0]==truth['starting_hole'])
assert all(report['control_positive_key'][k] for k in ['both_full_plaintexts_exact','input_ring_gauge_equivalent','physical_mask_exact','physical_start_exact'])
(b/'verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='cycle'},indent=2));print('cycle', {k:v for k,v in report['cycle'].items() if k!='rows'})
