from pathlib import Path
import json
from direct import solve
b=Path(__file__).resolve().parent;v=json.loads((b/'control-input.json').read_text());r=solve(v['plaintext'],v['ciphertext'],v['widths'],seconds=60,reverse_support=True)
if r['status']=='sat':
 x=v['ciphertext']
 for k in r['keys'][::-1]:
  a=['']*len(x);at=0
  for col in k:
   for pos in range(col,len(x),len(k)):a[pos]=x[at];at+=1
  x=''.join(a)
 assert x==v['plaintext'];r['independent_full65_inverse']=True
(b/'reverse-control-result.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
