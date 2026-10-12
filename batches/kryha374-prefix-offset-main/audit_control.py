from pathlib import Path
import json
out=Path(__file__).resolve().parent;a=json.loads((out/'control.json').read_text());rows=[]
for row in a['cases']:
 r=row['result']
 if r['status']!='sat':continue
 P,O,K,m=r['P'],r['O'],r['K'],r['m'];letters='abcdefghijklmnopqrstuvwxyz';p=a['p'];ct=a['framed_ciphertext'][row['offset']:row['offset']+len(p)];invP={x:letters[j]for j,x in enumerate(P)};invO={x:letters[j]for j,x in enumerate(O)}
 assert sorted(P)==sorted(O)==list(range(26));enc=[];dec=[];turn=0
 for i,(x,y)in enumerate(zip(p,ct)):
  if i and i%m==0:turn=(turn+179)%26
  enc.append(invO[(P[letters.index(x)]+K[i%m]+turn)%26]);dec.append(invP[(O[letters.index(y)]-K[i%m]-turn)%26])
 assert ''.join(enc)==ct and ''.join(dec)==p
 rows.append(dict(offset=row['offset'],period=m,positions=len(p),independent_forward=True,independent_inverse=True))
(out/'control-audit.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows))
