from pathlib import Path
import random,json,os
from engine import solve
B=Path(__file__).resolve().parent;(B/'owned-pid.txt').write_text(str(os.getpid())+'\n')
def save(name,obj):(B/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n')
rows=json.loads(Path('batches/repeat369-365-sol61/closest-inventory.json').read_text());row=next(x for x in rows if x['first_sentence_X']==1 and x['second_sentence_X']==1);p=row['plaintext'];widths=(21,19,20)
seed=369612212001;rng=random.Random(seed);n=rng.randrange(1,20);keys=[]
for w in widths:
 key=list(range(1,w));rng.shuffle(key);key.insert(n-1,0);keys.append(key)
def independent(s,key):
 return ''.join(s[row*len(key)+col]for col in key for row in range((len(s)+len(key)-1)//len(key))if row*len(key)+col<len(s))
c=p
for key in keys:c=independent(c,key)
at=c.index('n');bad=c[:at]+'u'+c[at+1:];save('control-truth',dict(plaintext=p,ciphertext=c,observed_ciphertext=bad,keys=keys,n=n,seed=seed,error_position1=at+1,exact_preferred_published_profile=True))
known=solve(p,bad,widths=widths,seconds=10,known_keys=keys);save('control-known',known);print('known',known['status'],flush=True)
blind=solve(p,bad,widths=widths,seconds=120,verbose=True)
if blind['status']=='sat':blind['all_planted_keys_recovered']=blind['keys']==keys
save('control-blind',blind);print('blind',blind['status'],flush=True)
if blind['status']!='sat':print('No actual target: positive calibration gate failed.',flush=True);raise SystemExit(0)
save('control-second-witness',solve(p,bad,widths=widths,seconds=60,blocked_keys=blind['keys'],verbose=True))
target=solve(row['plaintext'],row['ciphertext'],widths=widths,seconds=120,verbose=True);target['conditional_preparation']=row;save('target',target);print('target',target['status'],flush=True)
if target['status']=='sat':save('target-second-witness',solve(row['plaintext'],row['ciphertext'],widths=widths,seconds=60,blocked_keys=target['keys'],verbose=True))
