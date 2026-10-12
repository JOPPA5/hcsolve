from pathlib import Path
import json,random,sys,hashlib
from engine import run,enc
b=Path(__file__).resolve().parent
def save(name,result):
    (b/(name+'.json')).write_text(json.dumps(result,indent=2)+'\n')
def callback(name):
    def fn(result):
        save(name,result);row=result['rows'][-1];print(name,row['n'],row['status'],round(row['seconds'],2),flush=True)
    return fn
source=Path('batches/repeat369-365-sol61/closest-inventory.json')
rows=json.loads(source.read_text());cases={row['plaintext']:row for row in rows}
p=next(row['plaintext'] for row in rows if row['first_sentence_X']==1 and row['second_sentence_X']==1)
rng=random.Random(3691221221);n=rng.randrange(1,22);keys=[];c=p
for w in [22,22,21]:
    key=list(range(1,w));rng.shuffle(key);key.insert(n-1,0);keys.append(key);c=enc(c,key)
at=rng.choice([i for i,x in enumerate(c) if x=='n']);observed=c[:at]+'u'+c[at+1:]
save('control-truth',dict(seed=3691221221,keys=keys,n=n,plaintext=p,expected_ciphertext=c,observed_ciphertext=observed,error_position1=at+1))
save('provenance',dict(source=str(source),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),scope='conditional widths22/22/21, common alignment, known public365 quote, exactly one predicted N to literal U'))
control=run(p,observed,cap=8,on_row=callback('control'))
if not any(row['status']=='sat' for row in control['rows']):
    print('No full blind control recovery; historical target gated off',flush=True);sys.exit(0)
for j,case in enumerate(cases.values()):
    run(case['plaintext'],case['ciphertext'],cap=15,on_row=callback('target'+str(j)))
