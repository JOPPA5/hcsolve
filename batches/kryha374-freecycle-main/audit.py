"""Independent forward and inverse audit of saved algebraic controls, not physical wheel evidence."""
from pathlib import Path
import json
out=Path(__file__).resolve().parent
rows=[]
for x in json.loads((out/'controls.json').read_text()):
 r=x['result']
 if r['status']!='sat':continue
 p,c,m,D=x['p'],x['c'],x['m'],x['planted_D'];P,O,K=r['P'],r['O'],r['K']
 assert sorted(P)==sorted(O)==list(range(26))
 letters='abcdefghijklmnopqrstuvwxyz';invP={v:letters[j]for j,v in enumerate(P)};invO={v:letters[j]for j,v in enumerate(O)}
 enc=[];dec=[];displacement=0
 # Separate stepping recurrence: return to the first residue and advance D at a cycle boundary.
 for j,(a,b)in enumerate(zip(p,c)):
  slot=j%m
  if slot==0 and j:displacement=(displacement+D)%26
  enc.append(invO[(P[letters.index(a)]+K[slot]+displacement)%26])
  dec.append(invP[(O[letters.index(b)]-K[slot]-displacement)%26])
 assert ''.join(enc)==c and ''.join(dec)==p
 rows.append(dict(m=m,D=D,positions=len(p),forward_exact=True,inverse_exact=True))
(out/'control-audit.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows))
