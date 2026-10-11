from pathlib import Path
import json
p=Path(__file__).parent
controls=json.loads((p/'controls.json').read_text())
def dec(ct,key):
 w=len(key);h,r=divmod(len(ct),w);cols=['']*w;off=0
 for col in key:
  n=h+(col<r);cols[col]=ct[off:off+n];off+=n
 return ''.join(cols[j][i] for i in range(h+1) for j in range(w) if i<len(cols[j]))
for name,data in controls.items():
 s=(p/(name+'.txt')).read_text()
 for key in data['keys'][::-1]:s=dec(s,key)
 assert s==data['plaintext'],name
 print(name,'independent known-key inverse PASS')
