from pathlib import Path
import json,math,random,hashlib
p=Path(__file__).resolve().parent
# Manually read primary printedp185/PDFpage190, visually checked; indexh-1 is h -> h+1.
a=[4,3,4,3,3,3,4,3,4,4,3,3,3,3,4,4,3,3,4,3,3,4,3,3,4,3,3,4,4,4,3,3,4,3,3,3,4,3,4,3,3,4,5,3,3,3,3,4,3,3,4,5]
assert len(a)==52 and sum(a)==179
coordinates=[0]
for d in a[:-1]:coordinates.append(coordinates[-1]+d)
def distance_iter(h,k):
 d=0
 while True:
  d+=a[h-1];h=h%52+1
  if h==k:return d
# Independent calculation from cumulative wheel coordinates plus179 wrap.
def distance_coords(h,k):return (coordinates[k-1]-coordinates[h-1])%179 or 179
fragments=[(48,8,[4,3,3,4,5,4,3,4,3,3,3,4]),(43,1,[5,3,3,3,3,4,3,3,4,5])]
for h,k,expected in fragments:
 got=[];at=h
 while at!=k:got.append(a[at-1]);at=at%52+1
 assert got==expected
checks=[(8,9,3),(8,10,7),(8,11,11),(8,12,14),(8,13,17),(1,2,4),(1,3,7),(1,4,11),(1,5,14),(2,3,3),(2,4,7),(2,5,10),(2,6,13),(3,4,4),(3,5,7),(3,6,10),(3,7,13),(10,15,16),(15,17,8),(10,17,24),(48,49,4),(49,2,19),(2,5,10),(5,7,6),(7,8,4)]
for h,k,want in checks:assert distance_iter(h,k)==want==distance_coords(h,k)
rng=random.Random(52179);random_checks=0
for _ in range(1000):
 stops=sorted(rng.sample(range(1,53),rng.randint(20,30)))
 jumps=[distance_iter(h,stops[(i+1)%len(stops)])for i,h in enumerate(stops)]
 assert jumps==[distance_coords(h,stops[(i+1)%len(stops)])for i,h in enumerate(stops)]
 assert sum(jumps)==179
 # Independently follow state (active-stop index, cipher-relative offset) until return.
 state=(0,0);n=0
 while True:
  state=((state[0]+1)%len(stops),(state[1]+jumps[state[0]])%26);n+=1
  if state==(0,0):break
  assert n<=26*len(stops)
 assert n==26*len(stops);random_checks+=1
# Primary example active-stop masks (publishedGerman exercises, not targetkeys).
masks={'NR2417_page9':[48,49,51,52,2,5,7,8,10,12,15,17,20,22,24,29,30,32,33,37,38,40,41,44,45,47],'NR2417_page15':[43,44,45,47,49,51,52,1,3,4,7,8,10,11,12,16,17,19,22,23,24,27,31,33,36,39,40,42]}
examples={name:dict(active_count=len(stops),cycle_jumps=[distance_iter(h,stops[(i+1)%len(stops)])for i,h in enumerate(stops)],cycle_sum=179,press_state_period=26*len(stops))for name,stops in masks.items()}
for ex in examples.values():assert sum(ex['cycle_jumps'])==179
geometry=dict(model='later programmable52stop Kryha; effective letter displacement',adjacent_distances=a,index_convention='array[h-1] is holeh -> hole(h%52+1), hole1 coordinate0',unwrapped_effective_coordinates=coordinates,cycle_total=179,cycle_mod26=23,physical_angles_not_measured=True,allowed_step_family='cyclic sums of consecutiveadjacentdistances between activeholes; cannot choose eachstep independently',orientation='positive increasinghole direction; physicalring handedness separate and model-dependent',holes1to52_all_transcribed=True)
(p/'wheel52.json').write_text(json.dumps(geometry,indent=2));(p/'wheel52.csv').write_text('from_hole,to_hole,effective_letter_distance,unwrapped_coordinate\n'+''.join(f'{h},{h%52+1},{a[h-1]},{coordinates[h-1]}\n'for h in range(1,53)))
result=dict(adjacent_count=52,cycle_sum=179,gcd_cycle26=math.gcd(179,26),SSA_fragment_and_sum_checks=len(checks)+len(fragments),independent_random_masks=random_checks,example_masks=examples,source_conflict=dict(reference='NR2417page7 provisionalhole17to19 jump16',actual_17to19=distance_iter(17,19),hypothetical_17to22=distance_iter(17,22),correction_not_assumed=True),source_sha256={f.name:hashlib.sha256(f.read_bytes()).hexdigest()for f in (p/'source').glob('*.pdf')})
(p/'verification.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
