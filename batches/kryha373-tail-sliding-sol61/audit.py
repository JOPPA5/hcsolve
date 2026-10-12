from pathlib import Path
import ast,random,json,sys
import numpy as np
B=Path(__file__).resolve().parent
sys.path.insert(0,str(Path('batches/kryha373-comma-marker-sol61').resolve()))
from engine import expressions
source=ast.parse((B/'run.py').read_text());node=next(x for x in source.body if isinstance(x,ast.FunctionDef)and x.name=='linear');scope={'np':np};exec(compile(ast.Module(body=[node],type_ignores=[]),'<linear>','exec'),scope)
d=json.loads((B/'inputs.json').read_text());rng=random.Random(373612501);rows=[]
for j in range(80):
 pr=rng.choice(d['preparations']);p=pr['p'];off=rng.randrange(651-len(p));m=rng.randrange(2,53);ix=[i for i in range(len(p))if off+i+1 not in d['erased_absolute_onebased']];pp=''.join(p[i]for i in ix);cc=''.join(d['ciphertext'][off+i]for i in ix);n=52+m;a=[]
 for x,y,t in zip(pp,cc,ix):
  r=[0]*(n+1);r[ord(y)-97+26]+=1;r[ord(x)-97]-=1;r[52+t%m]-=1;r[-1]=179*(t//m);a.append(r)
 for k in [0,26]:r=[0]*(n+1);r[k]=1;a.append(r)
 expected=all(expressions(a,n,q)[0]is not None for q in [2,13]);actual=scope['linear'](pp,cc,ix,m);assert actual==expected;rows.append(dict(offset=off,m=m,consistent=actual))
(B/'linear-audit.json').write_text(json.dumps(rows,indent=2)+'\n');print('Independent modular implementations agree:80 cases')
