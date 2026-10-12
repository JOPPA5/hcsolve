from pathlib import Path
import json,random,os
from engine import solve
B=Path(__file__).resolve().parent;(B/'matched-owned-pid.txt').write_text(str(os.getpid())+'\n')
rows=json.loads(Path('batches/repeat369-365-sol61/closest-inventory.json').read_text());row=next(x for x in rows if x['first_sentence_X']==1 and x['second_sentence_X']==1);p=row['plaintext']
assert len(p)==110 and p.count('x')==5
seed=3696122203;rng=random.Random(seed);n=rng.randrange(1,23);keys=[]
for _ in range(3):
 key=list(range(1,22));rng.shuffle(key);key.insert(n-1,0);keys.append(key)
def independent(s,k):return ''.join(s[row*22+col]for col in k for row in range(5))
c=p
for key in keys:c=independent(c,key)
at=c.index('n');bad=c[:at]+'u'+c[at+1:]
def save(name,obj):(B/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n')
save('control2-truth',dict(plaintext=p,lexical_length=105,X_count=5,ciphertext=c,observed_ciphertext=bad,keys=keys,n=n,seed=seed,error_position1=at+1,authorship='attributed published365 plaintext with frozen conditional369 preparation; no target ciphertext used for keys'))
known=solve(p,bad,seconds=10,known_keys=keys);save('control2-known',known);print('matched known',known['status'],flush=True)
blind=solve(p,bad,seconds=120)
if blind['status']=='sat':blind['all_planted_keys_recovered']=blind['keys']==keys
save('control2-eager',blind);print('matched blind',blind['status'],flush=True)
if blind['status']=='sat':save('control2-second-witness',solve(p,bad,seconds=60,blocked_keys=blind['keys']))
