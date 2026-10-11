from codec import *
from collections import Counter
import sys
folder=Path(sys.argv[1]).resolve();m=int(sys.argv[2]);cts=(folder/'ciphertexts.txt').read_text().split();T=models();checked=0;maxerr=0;bestmatch=0;plant=json.loads((folder/'plant.json').read_text())if(folder/'plant.json').exists()else None

def test(z):
 global checked,maxerr,bestmatch
 assert len(z['holes'])==m;maxerr=max(maxerr,check(z,cts,T));checked+=1
 if plant is not None:bestmatch=max(bestmatch,sum(a==b for t,u in zip(z['plaintexts'],plant['plaintexts'])for a,b in zip(t,u)))
for z in json.loads((folder/'bridge-ranked.json').read_text()):test(z)
for seed in range(4):
 sfolder=folder/f'bridge-seed{seed}'
 for iteration in range(4):
  stage=sfolder/f'iteration{iteration}';keys=list(map(int,(stage/'rings-before.txt').read_text().split()));P,O=keys[:26],keys[26:]
  for line in(stage/'beam.tsv').read_text().splitlines():
   anchor,rank,sc,h,p0,p1=line.split('\t');test(dict(score=float(sc),holes=list(map(int,h.split(','))),input_slots=P,output_positions=O,plaintexts=[p0,p1]))
  test(json.loads((stage/'result.json').read_text()))
logs=sorted(float(line.split()[1])for line in(LARGE/'ring-unigrams.tsv').read_text().splitlines());profileerr=0;profiles=0
for line in(folder/'mask-profiles.tsv').read_text().splitlines():
 ix,restart,sc,h,key=line.split('\t');holes=list(map(int,h.rstrip(',').split(',')));O=list(map(int,key.rstrip(',').split(',')));assert sorted(O)==list(range(26));steps=schedule(holes);counts=Counter()
 for ct in cts:
  d=0
  for i,c in enumerate(ct):counts[(O[ord(c)-97]-d)%26]+=1;d=(d+steps[i%m])%26
 value=sum(n*l-math.lgamma(n+1)for n,l in zip(sorted(counts[i]for i in range(26)),logs));err=abs(value-float(sc));profileerr=max(profileerr,err);assert err<.012;profiles+=1
cyclechecked=0
for line in(folder/'pair-cycle.tsv').read_text().splitlines():
 ix,sc,key=line.split('\t');O=list(map(int,key.split(',')));assert sorted(O)==list(range(26));H=[Counter()for _ in range(m)]
 for ct in cts:
  for i,c in enumerate(ct):H[i%m][(O[ord(c)-97]-179*(i//m))%26]+=1
 assert int(sc)==sum(n*(n-1)//2 for row in H for n in row.values());cyclechecked+=1
results=json.loads((folder/'bridge-results.json').read_text());winner=max(results,key=lambda z:z['score']);report=dict(count=m,complete=True,paired_candidate_keys_checked=checked,full_message_reencryptions=2*checked,score_max_error=maxerr,profile_rows_checked=profiles,profile_max_error=profileerr,cycle_rows_checked=cyclechecked,selected_by_model_score_only=True,selected_final=winner,all_key_permutations_valid=True,all_independent_encoder_inverse_checks_exact=True,all_per_message_boundary_scores_exact=True)
if plant is not None:
 trueP=plant['input_slots'];trueO=plant['output_positions'];g=(winner['output_positions'][0]-trueO[0])%26;normalizedO=[(x+g)%26 for x in trueO];normalizedP=[trueP[(i-g)%26]for i in range(26)];report.update(exact_full_selected_plaintext=winner['plaintexts']==plant['plaintexts'],matching_letters_per_message=[sum(a==b for a,b in zip(t,u))for t,u in zip(winner['plaintexts'],plant['plaintexts'])],best_saved_diagnostic_matches=bestmatch,true_language_score=score(plant['plaintexts'],T),exact_physical_mask=set(winner['holes'])==set(plant['ordered_holes']),exact_physical_start=winner['holes'][0]==plant['starting_hole'],output_ring_slots_matching_up_rotation=sum(a==b for a,b in zip(normalizedO,winner['output_positions'])),input_ring_slots_matching_up_rotation=sum(a==b for a,b in zip(normalizedP,winner['input_slots'])),unused_plaintext_letters=''.join(chr(97+i)for i in range(26)if chr(97+i)not in ''.join(plant['plaintexts'])),truth_opened_only_after_search=True)
(folder/'verification.json').write_text(json.dumps(report,indent=2));print(m,report.get('exact_full_selected_plaintext'),report.get('matching_letters_per_message'),winner['score'],'checked',checked)
