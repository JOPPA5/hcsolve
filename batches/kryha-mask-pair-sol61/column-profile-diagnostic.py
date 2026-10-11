from pathlib import Path
import json,collections,math,random
b=Path(__file__).resolve().parent;r=b.parents[1];logs=sorted(float(s.split()[1]) for s in (r/'ciphers/hcp-350/work/ring-unigrams.tsv').read_text().splitlines());results=[]
for folder in [b,b/'framing355-control']:
 t=json.load(open(folder/'control.json'));cts=(folder/'ciphertexts.txt').read_text().split()
 def score(O):
  H=[collections.Counter() for _ in range(26)]
  for ct in cts:
   for i,c in enumerate(ct):H[i%26][(O[ord(c)-97]-23*(i//26))%26]+=1
  return sum(sum(n*l-math.lgamma(n+1) for n,l in zip(sorted(h[i] for i in range(26)),logs)) for h in H)
 false=[]
 for line in (folder/'pair-cycle.tsv').read_text().splitlines():
  ix,sc,key=line.split('\t');false.append(score(list(map(int,key.split(',')))))
 rng=random.Random(52771555);null=[]
 for _ in range(1000):O=list(range(26));rng.shuffle(O);null.append(score(O))
 results.append(dict(control=folder.name,true_score=score(t['output_positions']),old_false_min=min(false),old_false_max=max(false),old_false_mean=sum(false)/len(false),null_max=max(null),null_mean=sum(null)/len(null),interpretation='post-search landscape only; no true seed'))
(b/'column-profile-diagnostic.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results,indent=2))
