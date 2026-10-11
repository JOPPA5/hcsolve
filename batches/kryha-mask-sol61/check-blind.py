from pathlib import Path
import json
b=Path(__file__).resolve().parent;r=b.parents[1];geometry=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'));a=geometry['adjacent_distances'];weights={2:.1,3:.15,4:.4,5:.8};models={n:{s:float(v) for s,v in (line.split() for line in (b/f'model{n}.tsv' if n<4 else r/f'ciphers/hcp-350/work/ring-{n}grams.tsv').read_text().splitlines())} for n in range(2,6)}
control=next(c for c in json.load(open(b/'controls.json')) if c['m']==26);ct=control['ciphertext'];count=0;results=[]
def verify(P,O,holes,plain,score):
 global count
 assert sorted(P)==sorted(O)==list(range(26));assert len(set(holes))==len(holes)==26;assert all((holes[i+1]-holes[0])%52>(holes[i]-holes[0])%52 for i in range(25));jumps=[]
 for j,h in enumerate(holes):
  x=h;dist=0
  while True:
   dist+=a[x];x=(x+1)%52
   if x==holes[(j+1)%26]:break
  jumps.append(dist)
 assert sum(jumps)==179;ip={c:i for i,c in enumerate(P)};op={v:c for c,v in enumerate(O)};d=0;enc='';dec=''
 for i,(pc,cc) in enumerate(zip(plain,ct)):
  enc+=chr(97+op[(ip[ord(pc)-97]+d)%26]);dec+=chr(97+P[(O[ord(cc)-97]-d)%26]);d=(d+jumps[i%26])%26
 assert len(plain)==len(ct) and enc==ct and dec==plain
 independent=sum(weights[n]*sum(models[n].get(plain[i:i+n],-n) for i in range(len(plain)-n+1)) for n in range(2,6));assert abs(independent-score)<.04;count+=1
for folder in sorted(b.glob('blind26-start*')):
 for stage in sorted(folder.glob('iteration*')):
  keys=list(map(int,(stage/'rings-before.txt').read_text().split()));P=keys[:26];O=keys[26:]
  for line in (stage/'beam.tsv').read_text().splitlines():anchor,rank,score,holes,plain=line.split('\t');verify(P,O,list(map(int,holes.split(','))),plain,float(score))
  z=json.load(open(stage/'result.json'));verify(z['input_slots'],z['output_positions'],z['holes'],z['plaintext'],z['score']);z['exact_plaintext_diagnostic']=z['plaintext']==control['plaintext'];z['matching_letters_diagnostic']=sum(a==v for a,v in zip(z['plaintext'],control['plaintext']));off=(z['output_positions'][0]-control['output_positions'][0])%26;z['output_ring_positions_up_rotation_diagnostic']=sum((a+off)%26==v for a,v in zip(control['output_positions'],z['output_positions']));z['physical_hole_overlap_diagnostic']=len(set(z['holes'])&set(control['active_holes_zero_based']));results.append(z)
summary={'independent_blind_full_reencryptions_and_rescores':count,'iterations':len(results),'exact_blind_plaintext_found':any(z['exact_plaintext_diagnostic'] for z in results),'best_matching_letters_diagnostic_only':max(z['matching_letters_diagnostic'] for z in results),'best_whole_score':max(z['score'] for z in results),'m_supplied':26,'known_ring_calibration_does_not_validate_blind_search':True,'results':results};(b/'blind-checks.json').write_text(json.dumps(summary,indent=2)+'\n');print({k:v for k,v in summary.items() if k!='results'})
