from pathlib import Path
import random,json,os
from engine import solve
B=Path(__file__).resolve().parent;(B/'owned-pid.txt').write_text(str(os.getpid())+'\n')
def save(name,obj):(B/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n')
def independent(s,k):return ''.join(s[row*len(k)+col]for col in k for row in range(len(s)//len(k)))
raw=['potvrdprijemtajnejzpravyaposlidnesvecerpresnyprehladodovzdanychdokladovzastupcanashouraducakanaodpoved','preverihnedbezpecnostspojeniaapredodchodomodovzdajvsetkypisomnedokladynovemuzastupcovivyslanectva']
for case,(base,seed)in enumerate(zip(raw,[3696122201,3696122202])):
 assert len(base)<=110;p=base.ljust(110,'x');rng=random.Random(seed);n=rng.randrange(1,23);keys=[]
 for _ in range(3):
  key=list(range(1,22));rng.shuffle(key);key.insert(n-1,0);keys.append(key)
 c=p
 for key in keys:c=independent(c,key)
 at=c.index('n');bad=c[:at]+'u'+c[at+1:];save(f'control{case}-truth',dict(plaintext=p,lexical_length=len(base),ciphertext=c,observed_ciphertext=bad,keys=keys,n=n,seed=seed,error_position1=at+1,authorship='independently authored artificial control'))
 known=solve(p,bad,seconds=10,known_keys=keys);save(f'control{case}-known',known);print(case,'known',known['status'],flush=True)
 for backend,cap in [('eager',120),('native',60)]:
  result=solve(p,bad,seconds=cap,backend=backend)
  if result['status']=='sat':result['all_planted_keys_recovered']=result['keys']==keys
  save(f'control{case}-{backend}',result);print(case,backend,result['status'],flush=True)
  if result['status']=='sat':
   second=solve(p,bad,seconds=60,backend=backend,blocked_keys=result['keys']);save(f'control{case}-second-witness',second)
   if case==1:
    rows=json.loads(Path('batches/repeat369-365-sol61/closest-inventory.json').read_text());row=next(x for x in rows if x['first_sentence_X']==1 and x['second_sentence_X']==1)
    target=solve(row['plaintext'],row['ciphertext'],seconds=120,backend=backend);target['conditional_preparation']=row;save('target',target);print('target',target['status'],flush=True)
    if target['status']=='sat':save('target-second-witness',solve(row['plaintext'],row['ciphertext'],seconds=60,backend=backend,blocked_keys=target['keys']))
   break
