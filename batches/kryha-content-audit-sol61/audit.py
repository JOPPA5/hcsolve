from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parent;R=B.parents[1];kp=R/'batches/kryha-content-main/proposed-keys.json';keys=json.loads(kp.read_text());wp=R/'batches/kryha-wheel-sol61/wheel52.json';wheel=json.loads(wp.read_text());adj=wheel['adjacent_distances'];assert len(adj)==52 and sum(adj)==179
oldp=R/'batches/kryha-two-mask-refine-sol61/actual-row5-pure6-r7-full.json';old=next(x for x in json.loads(oldp.read_text())if x['n']==6);mapping={6:23,16:6,23:9,9:16};out=[]
def rotate(xs,n):return xs[n:]+xs[:n]
for side,key in enumerate(keys):
 number=key['number'];cp=R/f'batches/kryha-shift23-sol61/{number}-pixel-strong.txt';ct=cp.read_text().strip();P=key['P'];O=key['O'];holes=key['holes'];assert len(ct)==385;assert sorted(P)==list(range(26)) and sorted(O)==list(range(26));assert key['adjacent_distances']==adj;assert len(holes)==23 and len(set(holes))==23
 # A physical walker, not the inherited unwrapped-coordinate formula.
 jumps=[];walks=[]
 for a,b in zip(holes,holes[1:]+holes[:1]):
  h=a;dist=0;visited=[]
  while True:
   visited.append(h);dist+=adj[h];h=(h+1)%52
   if h==b:break
   assert len(visited)<53
  jumps.append(dist);walks.append(visited)
 assert sum(jumps)==179 and sum(map(len,walks))==52
 displacement=key['initial_displacement'];pt='';ds=[]
 for i,ch in enumerate(ct):
  ds.append(displacement);slot=(O[ord(ch)-97]-displacement)%26;pt+=chr(97+P[slot]);displacement=(displacement+jumps[i%23])%26
 assert pt==key['plaintext']
 ip={letter:slot for slot,letter in enumerate(P)};io={pos:letter for letter,pos in enumerate(O)};d=key['initial_displacement'];reen=''
 for i,ch in enumerate(pt):reen+=chr(97+io[(ip[ord(ch)-97]+d)%26]);d=(d+jumps[i%23])%26
 assert reen==ct
 expected_holes=rotate(old['masks'][side],3);assert expected_holes==holes and holes[0]==47
 # Walk from full start to old crop origin after twenty presses.
 anchor_advance=sum(jumps[:20]);assert anchor_advance==162 and anchor_advance%26==6
 expected_P=[mapping.get(old['P'][(i+anchor_advance)%26],old['P'][(i+anchor_advance)%26])for i in range(26)]
 assert expected_P==P and O==old['O']
 # Independent signed crop-coordinate crosscheck plus explicit relabeling.
 crop=old['masks'][side];co=wheel['unwrapped_effective_coordinates'];cross='';oldlabels=[]
 for i,ch in enumerate(ct):
  t=i-20;shift=co[crop[t%23]]-co[crop[0]]+(179 if crop[t%23]<crop[0]else 0)+179*(t//23)+ (old['beta']if side else 0)
  label=old['P'][(O[ord(ch)-97]-shift)%26];oldlabels.append(label);cross+=chr(97+mapping.get(label,label))
 assert cross==pt and 9 not in oldlabels
 (B/f'{number}-raw-prepared.txt').write_text(pt+'\n');(B/f'{number}-reencrypted.txt').write_text(reen+'\n')
 out.append(dict(number=number,ciphertext_length=len(ct),prepared_length=len(pt),exact_proposed_plaintext=True,exact_full385_inverse=True,exact_full385_adjacent_encoder=True,all_holes_walked_once=True,circumference=sum(jumps),active_stop_count=23,full_start_hole=holes[0],mask_rotation_from_crop=3,twenty_press_anchor_advance=anchor_advance,Pfull_rotation=anchor_advance%26,explicit_label_map={'G':'X','Q':'G','X':'J','J':'Q'},proposed_P_matches_rotated_relabelled_blind_P=True,proposed_masks_match_rotated_blind_masks=True,crop_coordinate_crosscheck_exact=True,old_label_counts={chr(97+x):oldlabels.count(x)for x in range(26)},old_J_unused_full385=True,first5=pt[:5],first5_unresolved=True,input_relabeling_semantically_selected_not_unique=True,I_J_historical_preparation_not_established=True,plaintext=pt,adjacent_arcs=jumps,displacements=ds,source_sha256=hashlib.sha256(cp.read_bytes()).hexdigest()))
(B/'verification.json').write_text(json.dumps(out,indent=2));(B/'provenance.json').write_text(json.dumps({str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in [kp,wp,oldp]},indent=2));print([(x['number'],x['exact_full385_inverse'],x['twenty_press_anchor_advance'],x['first5'])for x in out])
