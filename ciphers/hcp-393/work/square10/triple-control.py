from pathlib import Path
import json,random
w=Path(__file__).resolve().parent
p=next(r['plaintext'] for r in json.loads((w/'controls.json').read_text()) if r['label']=='authored-0')
rng=random.Random(393310);keys=[]
for i in range(3):
 k=list(range(10));rng.shuffle(k);keys.append(k)
s=p
for k in keys:s=''.join(s[r*10+c] for c in k for r in range(10))
t=''.join(s[r*10+c] for c in range(10) for r in range(10));w.joinpath('triple-control-transposed.txt').write_text(t+'\n');w.joinpath('triple-control.txt').write_text(s+'\n');combined=[keys[0][j] for j in keys[2]]
w.joinpath('triple-control.json').write_text(json.dumps(dict(plaintext=p,keys=keys,column_order=[combined.index(i) for i in range(10)],row_order=[keys[1].index(i) for i in range(10)]),indent=2))
s=w.parent.joinpath('cipher.txt').read_text().strip();assert len(s)==100
w.joinpath('target-transposed.txt').write_text(''.join(s[r*10+c] for c in range(10) for r in range(10))+'\n')
