from pathlib import Path
import importlib.util,itertools,json
B=Path(__file__).resolve().parent;sp=importlib.util.spec_from_file_location('d',B/'direct_engine.py');e=importlib.util.module_from_spec(sp);sp.loader.exec_module(e)
p='naxnunu';widths=[2,3,4];keys=[]
for k in itertools.product(*(list(itertools.permutations(range(w)))for w in widths)):
 if len(set(x.index(0) for x in k))==1:
  c=p
  for stage in k:c=''.join(c[i]for col in stage for i in range(col,len(c),len(stage)))
  keys.append((k,c))
samples=sorted(set(c[:i]+'u'+c[i+1:]for _,c in keys for i,ch in enumerate(c)if ch=='n'))
all_observations=sorted(set(''.join(t)for t in itertools.permutations(p.replace('n','u',1))))
samples=samples[:12]+all_observations[::max(1,len(all_observations)//12)][:12]
records=[]
for c in samples:
 matches=[k for k,pred in keys if sum(x!=y for x,y in zip(pred,c))==1 and all(x==y or(x=='n'and y=='u')for x,y in zip(pred,c))]
 r=e.solve(p,c,widths,seconds=5,common_rank=True);assert r['status']!='unknown';assert (r['status']=='sat')==bool(matches)
 if r['status']=='sat':
  v=p
  for stage in r['keys']:v=''.join(v[i]for col in stage for i in range(col,len(v),len(stage)))
  assert v==r['predicted_ciphertext']
 records.append(dict(ciphertext=c,enumerated_witnesses=len(matches),solver=r))
(B/'direct-toy-audit.json').write_text(json.dumps(records,indent=2)+'\n');print('direct one-error checks',len(records))
