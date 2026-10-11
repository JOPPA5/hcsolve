from pathlib import Path
import json,random,statistics,itertools
root=Path(__file__).resolve().parents[2];p=root/'ciphers/hcp-399/work'
keys=json.loads((p/'control-240-3stage-key.json').read_text());ct=(p/'control-240-3stage.txt').read_text().strip();plain=(p/'control-240-plain.txt').read_text().strip()
q={a:float(b) for line in (root/'ciphers/hcp-393/work/quadgrams.tsv').read_text().splitlines() for a,b in [line.split()]}
def dec(s,k):
 out=['']*len(s);at=0
 for c in k:
  for pos in range(c,len(s),len(k)):out[pos]=s[at];at+=1
 return ''.join(out)
def cascade(ks):
 s=ct
 for k in ks[::-1]:s=dec(s,k)
 return s
def score(s):return sum(q.get(s[i:i+4],-4) for i in range(len(s)-3))
assert cascade(keys)==plain
rng=random.Random(61011)
random_scores=[]
for _ in range(200):
 ks=[rng.sample(k,len(k)) for k in keys];random_scores.append(score(cascade(ks)))
report={'known_key_roundtrip':True,'true_score':score(plain),'random_200_score_median':statistics.median(random_scores),'layers':[]}
for l,k in enumerate(keys):
 rows=[]; by_length={'same':[],'different':[]}
 for a,b in itertools.combinations(range(len(k)),2):
  ks=[x[:] for x in keys];ks[l][a],ks[l][b]=ks[l][b],ks[l][a];s=cascade(ks)
  row=(sum(a==b for a,b in zip(s,plain)),score(s));rows.append(row)
  category='same' if (k[a]<len(ct)%len(k))==(k[b]<len(ct)%len(k)) else 'different';by_length[category].append(row)
 report['layers'].append({'length_classes':{name:{'count':len(v),'matches_median':statistics.median(x[0] for x in v),'score_median':statistics.median(x[1] for x in v)} for name,v in by_length.items()},'encryption_stage':l+1,'swap_count':len(rows),'matches_median':statistics.median(x[0] for x in rows),'matches_min':min(x[0] for x in rows),'score_median':statistics.median(x[1] for x in rows),'score_min':min(x[1] for x in rows)})
(root/'batches/sol61-audit/landscape.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
