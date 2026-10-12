from pathlib import Path
import itertools,json
from engine import solve
B=Path(__file__).resolve().parent;p='nanuxanxu';w=3;legal=[]
def independent(s,k):return ''.join(s[row*w+col]for col in k for row in range(len(s)//w))
for keys in itertools.product(list(itertools.permutations(range(w))),repeat=3):
 if len(set(k.index(0)for k in keys))==1:
  c=p
  for key in keys:c=independent(c,key)
  legal.append((keys,c))
obs=sorted(set(''.join(t)for t in itertools.permutations(p.replace('n','u',1))));sample=obs[::max(1,len(obs)//16)][:16]
sample+=sorted(set(c[:i]+'u'+c[i+1:]for _,c in legal for i,x in enumerate(c)if x=='n'))[:8]
records=[]
for c in sample:
 matches=[k for k,pred in legal if sum(a!=b for a,b in zip(pred,c))==1 and all(a==b or(a=='n'and b=='u')for a,b in zip(pred,c))]
 for backend in ['eager','native']:
  r=solve(p,c,w=w,seconds=5,backend=backend);assert r['status']!='unknown';assert (r['status']=='sat')==bool(matches)
  if r['status']=='sat':
   v=p
   for key in r['keys']:v=independent(v,key)
   assert v==r['predicted_ciphertext']
  records.append(dict(ciphertext=c,legal_key_triples=len(legal),enumerated_witnesses=len(matches),solver=r))
(B/'toy-results.json').write_text(json.dumps(records,indent=2)+'\n');print(len(records),'cases agree; SAT',sum(x['solver']['status']=='sat'for x in records))
