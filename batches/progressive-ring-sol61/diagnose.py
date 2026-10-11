from pathlib import Path
from collections import Counter
import json,math,random
b=Path(__file__).resolve().parent;manifest=json.load(open(b/'manifest.json'));logs=sorted(float(line.split()[1]) for line in Path(manifest['model_files']['ring-unigrams.tsv']).read_text().splitlines())
def score(ct,O):
 N=[0]*26
 for i,c in enumerate(ct):N[(O[ord(c)-97]-i)%26]+=1
 return sum(n*p-math.lgamma(n+1) for n,p in zip(sorted(N),logs))
records=[]
for c in json.load(open(b/'controls.json')):
 folder=b/c['label'];truth=score(c['ciphertext'],c['output_positions']);rows=[]
 if (folder/'profile.txt').exists():
  for line in (folder/'profile.txt').read_text().splitlines():
   sc,key=line.split();key=list(map(int,key.rstrip(',').split(',')));ind=score(c['ciphertext'],key);assert abs(float(sc)-ind)<.02;rows.append((ind,key))
 rng=random.Random(26115000+c['length']);null=[]
 for _ in range(1000):key=list(range(26));rng.shuffle(key);null.append(score(c['ciphertext'],key))
 record={'label':c['label'],'true_profile':truth,'null_max':max(null),'retained_profiles_above_truth':sum(sc>truth for sc,k in rows),'retained_count':len(rows),'max_profile':max((sc for sc,k in rows),default=None),'profile_candidates_independently_rescored':len(rows)}
 if (folder/'ranked.json').exists():
  ranked=json.load(open(folder/'ranked.json'));record['exact_plaintext_in_any_MASC_candidate']=any(x['plaintext']==c['plaintext'] for x in ranked);record['best_matching_letters_diagnostic_only']=max(sum(a==z for a,z in zip(x['plaintext'],c['plaintext'])) for x in ranked)
 records.append(record)
(b/'diagnostics.json').write_text(json.dumps(records,indent=2)+'\n');print(json.dumps(records,indent=2))
