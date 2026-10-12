from pathlib import Path
import itertools,json
from engine import solve
B=Path(__file__).resolve().parent;p='naxnunu';widths=(2,3,4);records=[]
allobs=sorted(set(''.join(x)for x in itertools.permutations(p.replace('n','u',1))))
for progressive in [False,True]:
 legal=[]
 for keys in itertools.product(*(list(itertools.permutations(range(w)))for w in widths)):
  ranks=[k.index(0)+1 for k in keys]
  if ranks!=([ranks[0]+j for j in range(3)]if progressive else[ranks[0]]*3):continue
  v=p
  for key in keys:v=''.join(v[i]for col in key for i in range(col,len(v),len(key)))
  legal.append((keys,v))
 samples=allobs[::max(1,len(allobs)//12)][:12]+sorted(set(c[:i]+'u'+c[i+1:]for _,c in legal for i,ch in enumerate(c)if ch=='n'))[:8]
 for obs in samples:
  matches=[k for k,c in legal if sum(a!=b for a,b in zip(c,obs))==1 and all(a==b or(a=='n'and b=='u')for a,b in zip(c,obs))]
  r=solve(p,obs,widths=widths,seconds=5,progressive=progressive)
  assert r['status']!='unknown'and(r['status']=='sat')==bool(matches),(progressive,obs,r,len(matches))
  if r['status']=='sat':
   v=p
   for key in r['keys']:v=''.join(v[i]for col in key for i in range(col,len(v),len(key)))
   assert v==r['predicted_ciphertext']
  records.append(dict(progressive=progressive,ciphertext=obs,legal_triples=len(legal),enumerated_witnesses=len(matches),solver=r))
(B/'toy-results.json').write_text(json.dumps(records,indent=2)+'\n');print(len(records),'cases agree',sum(r['solver']['status']=='sat'for r in records),'SAT')
