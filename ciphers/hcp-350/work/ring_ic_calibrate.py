from pathlib import Path
import json,random
p=Path(__file__).resolve().parent;ct=(p/'ring-control-cipher.txt').read_text().strip();key=json.loads((p/'ring-control-key.json').read_text());steps=[7,6,7,5,6,7,6,8,6,10,5,6,5,7,6,5,9];H=[[0]*26 for _ in range(26)];d=0
for i,c in enumerate(ct):H[ord(c)-97][d]+=1;d=(d-steps[(6+i)%17])%26
def concentration(O):
 N=[0]*26
 for c in range(26):
  for x in range(26):N[(O[c]-x)%26]+=H[c][x]
 return sum(n*n for n in N)
true=concentration(key['output_positions']);rng=random.Random(35038520);null=[]
for i in range(10000):k=list(range(26));rng.shuffle(k);null.append(concentration(k))
rows=[]
for line in (p/'ring-ic-control-candidates.txt').read_text().splitlines():
 fields=line.split();O=[int(x)for x in fields[1].split(',')if x];assert int(fields[0])==concentration(O);matches=max(sum((x+off)%26==y for x,y in zip(O,key['output_positions']))for off in range(26));rows.append(dict(concentration=int(fields[0]),output_positions=O,matches_up_to_rotation=matches))
report=dict(length=len(ct),true_concentration=true,true_IC=(true-len(ct))/(len(ct)*(len(ct)-1)),random_permutations=10000,null_min=min(null),null_max=max(null),null_mean=sum(null)/len(null),null_at_least_true=sum(x>=true for x in null),stored_candidates=len(rows),optimized_min=rows[-1]['concentration'],optimized_max=rows[0]['concentration'],optimized_at_least_true=sum(x['concentration']>=true for x in rows),best_ring_matches=max(x['matches_up_to_rotation']for x in rows),rows=rows)
(p/'ring-ic-control-report.json').write_text(json.dumps(report,indent=2))
