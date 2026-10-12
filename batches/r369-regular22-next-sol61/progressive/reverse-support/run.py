from pathlib import Path
import importlib.util,json,random,os
B=Path(__file__).resolve().parent
source=(B.parent/'engine.py').read_text()
extra='''reverse_clauses=0
 for col2 in range(w):
  for r2,C in enumerate(R[2][col2]):
   for row2 in range(height):
    final=height*r2+row2;y=row2*w+col2;r1,row1=divmod(y,height)
    for col1 in range(w):
     B=R[1][col1][r1];x=row1*w+col1;r0,row0=divmod(x,height);allowed=[]
     for col0 in range(w):
      ch=p[row0*w+col0];A=R[0][col0][r0]
      if ch==c[final]:allowed.append(z3.And(A,z3.Not(E[final])) if final in E else A)
      elif ch=='n' and c[final]=='u':allowed.append(z3.And(A,E[final]))
     s.add(z3.Or(z3.Not(C),z3.Not(B),*allowed));reverse_clauses+=1
 '''
source=source.replace('build=time.monotonic()-begin',extra+'build=time.monotonic()-begin').replace('endpoint_clauses=clauses,','endpoint_clauses=clauses,reverse_endpoint_clauses=reverse_clauses,')
(B/'engine.py').write_text(source)
spec=importlib.util.spec_from_file_location('reverse',B/'engine.py');e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
tests=[]
for old in json.loads((B.parent/'toy-results.json').read_text()):
 result=e.solve('nanuxanxu',old['ciphertext'],w=3,seconds=5)
 assert result['status']!='unknown' and (result['status']=='sat')==bool(old['enumerated_witnesses'])
 if result['status']=='sat':
  v='nanuxanxu'
  for key in result['keys']:v=''.join(v[row*3+col]for col in key for row in range(3))
  assert v==result['predicted_ciphertext']
 tests.append(dict(ciphertext=old['ciphertext'],enumerated_witnesses=old['enumerated_witnesses'],solver=result))
def save(name,obj):(B/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n')
save('toy-results',tests);print('reverse toys',len(tests),'agree',flush=True)
(B/'owned-pid.txt').write_text(str(os.getpid())+'\n')
rows=json.loads(Path('batches/repeat369-365-sol61/closest-inventory.json').read_text());row=next(x for x in rows if x['first_sentence_X']==1 and x['second_sentence_X']==1);p=row['plaintext']
seed=3696122205;rng=random.Random(seed);n=rng.randrange(1,21);keys=[]
for j in range(3):
 key=list(range(1,22));rng.shuffle(key);key.insert(n-1+j,0);keys.append(key)
def independent(s,k):return ''.join(s[row*22+col]for col in k for row in range(5))
c=p
for key in keys:c=independent(c,key)
at=c.index('n');bad=c[:at]+'u'+c[at+1:];save('control-truth',dict(plaintext=p,ciphertext=c,observed_ciphertext=bad,keys=keys,n=n,seed=seed,error_position1=at+1))
known=e.solve(p,bad,seconds=10,known_keys=keys);save('control-known',known);print('known',known['status'],flush=True)
blind=e.solve(p,bad,seconds=120)
if blind['status']=='sat':blind['all_planted_keys_recovered']=blind['keys']==keys
save('control-blind',blind);print('blind',blind['status'],flush=True)
if blind['status']=='sat':
 save('control-second-witness',e.solve(p,bad,seconds=60,blocked_keys=blind['keys']))
 target=e.solve(row['plaintext'],row['ciphertext'],seconds=120);target['conditional_preparation']=row;save('target',target);print('target',target['status'],flush=True)
 if target['status']=='sat':save('target-second-witness',e.solve(row['plaintext'],row['ciphertext'],seconds=60,blocked_keys=target['keys']))
