from pathlib import Path
import json
from direct import solve
b=Path(__file__).resolve().parent;v=json.loads((b/'r-control-input.json').read_text());r=solve(v['plaintext'],v['ciphertext'],v['widths'],seconds=8,reverse_support=True,common_rank=True,rank_partition=True)
if r['status']=='sat':
 x=v['ciphertext']
 for k in r['keys'][::-1]:
  a=['']*len(x);z=0
  for col in k:
   for i in range(col,len(x),len(k)):a[i]=x[z];z+=1
  x=''.join(a)
 assert x==v['plaintext'];r['independent_inverse_full65']=True
(b/'rank-control-result.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
