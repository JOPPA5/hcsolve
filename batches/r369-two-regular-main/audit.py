"""Small exhaustive audit with a separate grid implementation."""
import itertools,random,json
from pathlib import Path
from engine import run
b=Path(__file__).resolve().parent
def grid(p,key):
    width=len(key);rows=[list(p[i:i+width]) for i in range(0,len(p),width)]
    return ''.join(row[col] for col in key for row in rows if col<len(row))
def compatible(predicted,observed):
    mismatch=[(a,c) for a,c in zip(predicted,observed) if a!=c]
    return mismatch==[('n','u')]
rng=random.Random(36910221221);p='annbcd';families=[]
for n in range(3):
    keys3=[k for k in itertools.permutations(range(3)) if k[n]==0]
    keys4=[k for k in itertools.permutations(range(4)) if k[n]==0]
    families.extend(itertools.product(keys3,keys3,keys4))
assert len(families)==72
predictions=[]
for keys in families:
    c=p
    for key in keys:c=grid(c,key)
    predictions.append(c)
results=[]
for j in range(24):
    if j<12:
        c=rng.choice(predictions);idx=rng.choice([i for i,x in enumerate(c) if x=='n']);c=c[:idx]+'u'+c[idx+1:]
    else:
        letters=list('anubcd');rng.shuffle(letters);c=''.join(letters)
    expected=any(compatible(pred,c) for pred in predictions)
    result=run(p,c,cap=3,w=3,v=4);got=any(row['status']=='sat' for row in result['rows'])
    assert not any(row['status']=='unknown' for row in result['rows']) and got==expected
    if got:
        keys=next(row['keys'] for row in result['rows'] if row['status']=='sat');pred=p
        for key in keys:pred=grid(pred,key)
        assert compatible(pred,c)
    results.append(dict(plaintext=p,ciphertext=c,expected_sat=expected,result=result))
(b/'audit.json').write_text(json.dumps(dict(independent_key_triples=72,cases=results),indent=2)+'\n')
print('24 exhaustive cases PASS; SAT',sum(r['expected_sat'] for r in results),'UNSAT',sum(not r['expected_sat'] for r in results))
