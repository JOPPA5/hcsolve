from pathlib import Path
import json,random,os,importlib.util
B=Path(__file__).resolve().parent;(B/'owned-pid.txt').write_text(str(os.getpid())+'\n')
source=(B.parent/'engine.py').read_text()
old='for rank in range(w):s.add(R[0][0][rank]==R[1][0][rank],R[0][0][rank]==R[2][0][rank])'
new='for rank in range(w):\n  if rank+2>=w:s.add(z3.Not(R[0][0][rank]))\n  else:s.add(R[0][0][rank]==R[1][0][rank+1],R[0][0][rank]==R[2][0][rank+2])\n s.add(z3.Not(R[1][0][0]),z3.Not(R[1][0][w-1]),z3.Not(R[2][0][0]),z3.Not(R[2][0][1]))'
assert old in source;source=source.replace(old,new).replace('len(set(k.index(0)for k in keys))==1','[k.index(0)for k in keys]==[keys[0].index(0)+j for j in range(3)]').replace('unknown_common_alignment=True','unknown_progressive_alignment=True')
(B/'engine.py').write_text(source)
spec=importlib.util.spec_from_file_location('progressive',B/'engine.py');e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
rows=json.loads(Path('batches/repeat369-365-sol61/closest-inventory.json').read_text());row=next(x for x in rows if x['first_sentence_X']==1 and x['second_sentence_X']==1);p=row['plaintext']
seed=3696122204;rng=random.Random(seed);n=rng.randrange(1,21);keys=[]
for j in range(3):
 key=list(range(1,22));rng.shuffle(key);key.insert(n-1+j,0);keys.append(key)
def independent(s,k):return ''.join(s[row*22+col]for col in k for row in range(5))
c=p
for key in keys:c=independent(c,key)
at=c.index('n');bad=c[:at]+'u'+c[at+1:]
def save(name,obj):(B/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n')
save('control-truth',dict(plaintext=p,ciphertext=c,observed_ciphertext=bad,keys=keys,n=n,seed=seed,error_position1=at+1,X_count=5,rank_hints=False))
# Small independent finite audit is run before the blind full control.
import itertools
small='nanuxanxu';legal=[]
for ks in itertools.product(list(itertools.permutations(range(3))),repeat=3):
 if [k.index(0)for k in ks]==[ks[0].index(0)+j for j in range(3)]:
  text=small
  for k in ks:text=''.join(text[row*3+col]for col in k for row in range(3))
  legal.append((ks,text))
allobs=sorted(set(''.join(x)for x in itertools.permutations(small.replace('n','u',1))))
samples=allobs[::max(1,len(allobs)//12)][:12]+sorted(set(t[:i]+'u'+t[i+1:]for _,t in legal for i,ch in enumerate(t)if ch=='n'))[:8]
tests=[]
for obs in samples:
 matches=[k for k,t in legal if sum(a!=b for a,b in zip(t,obs))==1 and all(a==b or(a=='n'and b=='u')for a,b in zip(t,obs))]
 result=e.solve(small,obs,w=3,seconds=5);assert result['status']!='unknown'and(result['status']=='sat')==bool(matches)
 if result['status']=='sat':
  text=small
  for key in result['keys']:text=''.join(text[row*3+col]for col in key for row in range(3))
  assert text==result['predicted_ciphertext']
 tests.append(dict(ciphertext=obs,enumerated_witnesses=len(matches),solver=result))
save('toy-results',tests);print('progressive toys',len(tests),'agree',flush=True)
known=e.solve(p,bad,seconds=10,known_keys=keys);save('control-known',known);print('known',known['status'],flush=True)
blind=e.solve(p,bad,seconds=120)
if blind['status']=='sat':blind['all_planted_keys_recovered']=blind['keys']==keys
save('control-blind',blind);print('blind',blind['status'],flush=True)
if blind['status']=='sat':
 save('control-second-witness',e.solve(p,bad,seconds=60,blocked_keys=blind['keys']))
 target=e.solve(row['plaintext'],row['ciphertext'],seconds=120);target['conditional_preparation']=row;save('target',target);print('target',target['status'],flush=True)
 if target['status']=='sat':save('target-second-witness',e.solve(row['plaintext'],row['ciphertext'],seconds=60,blocked_keys=target['keys']))
