from pathlib import Path
import json,math
b=Path(__file__).resolve().parent;r=b.parents[2];a=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'))['adjacent_distances'];logs=sorted(float(line.split()[1]) for line in (r/'ciphers/hcp-350/work/ring-unigrams.tsv').read_text().splitlines());counts={'physical_full_reencryptions':0,'independent_profile_rescores':0};results=[]
def verify(z,c,jumps):
 P=z['input_slots'];O=z['output_positions'];assert sorted(P)==sorted(O)==list(range(26));ip={v:i for i,v in enumerate(P)};op={v:i for i,v in enumerate(O)};d=0;dec='';enc=''
 for i,(pc,cc) in enumerate(zip(z['plaintext'],c['ciphertext'])):enc+=chr(97+op[(ip[ord(pc)-97]+d)%26]);dec+=chr(97+P[(O[ord(cc)-97]-d)%26]);d=(d+jumps[i%c['m']])%26
 assert len(z['plaintext'])==385 and enc==c['ciphertext'] and dec==z['plaintext'];counts['physical_full_reencryptions']+=1
for c in json.load(open(b/'controls.json')):
 holes=c['active_holes_zero_based'];holes=holes[c['phase']:]+holes[:c['phase']];jumps=[]
 for j,h in enumerate(holes):
  dist=0;x=h
  while True:
   dist+=a[x];x=(x+1)%52
   if x==holes[(j+1)%len(holes)]:break
  jumps.append(dist)
 assert sum(jumps)==179 and jumps==c['supplied_schedule'];folder=b/c['label'];ranked=json.load(open(folder/'ranked.json'))
 for z in ranked:verify(z,c,jumps)
 for line in (folder/'profile.txt').read_text().splitlines():
  sc,key=line.split();O=list(map(int,key.rstrip(',').split(',')));assert sorted(O)==list(range(26));N=[0]*26;d=0
  for i,cc in enumerate(c['ciphertext']):N[(O[ord(cc)-97]-d)%26]+=1;d=(d+jumps[i%c['m']])%26
  score=sum(n*p-math.lgamma(n+1) for n,p in zip(sorted(N),logs));assert abs(score-float(sc))<.02;counts['independent_profile_rescores']+=1
 for stage in (4,5):
  z=json.load(open(folder/f'result{stage}.json'));verify(z,c,jumps);coverage=json.load(open(folder/f'result{stage}-coverage.json'));assert len(coverage)==326
  for row in coverage:verify(row,c,jumps)
  shift=(z['output_positions'][0]-c['output_positions'][0])%26;record={'label':c['label'],'stage':stage,'known_mask_and_phase':True,'unknown_rings':True,'exact_plaintext':z['plaintext']==c['plaintext'],'matching_letters':sum(a==v for a,v in zip(z['plaintext'],c['plaintext'])),'output_positions_matching_up_rotation':sum((a+shift)%26==v for a,v in zip(c['output_positions'],z['output_positions'])),'exact_neighbor_ranks5':[i for i,row in enumerate(coverage) if row['plaintext']==c['plaintext']],'absent_plaintext_letters':''.join(chr(97+i) for i in range(26) if chr(97+i) not in c['plaintext']),'plaintext':z['plaintext'],'input_slots':z['input_slots'],'output_positions':z['output_positions']};results.append(record)
(b/'checks.json').write_text(json.dumps({'counts':counts,'results':results,'actual_targets_attempted':0},indent=2)+'\n');print(counts);print([(x['label'],x['stage'],x['matching_letters'],x['output_positions_matching_up_rotation'],x['exact_neighbor_ranks5']) for x in results])
