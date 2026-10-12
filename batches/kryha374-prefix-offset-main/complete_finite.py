"""Isolated finite-active-parameter continuation of six saved ordinary UNKNOWN cases.

Uses a separately audited solver helper. The previous SMT timeouts are retained.
"""
from pathlib import Path
import json,sys
root=Path(__file__).resolve().parents[2];out=Path(__file__).resolve().parent
sys.path.insert(0,str(root/'batches/kryha373-unemitted-spaces-sol61'))
from crt import solve
ct=(root/'batches/kryha373-collation-sol61/ciphertext650.txt').read_text().strip().lower();rows=[]
for i,x in enumerate(json.loads((out/'unknown-cases.json').read_text())):
 c=list(ct);c[52]=x['glyph53'];c[89]=x['glyph90'];c=''.join(c);segment=c[x['offset']:x['offset']+len(x['p'])]
 r=solve(x['p'],segment,x['m'],2000);row=dict(original_case=x,completion=r)
 if r['status']=='sat':
  P,O,K=r['P'],r['O'],r['K'];invP={v:chr(97+j)for j,v in enumerate(P)};r['full_context_decode']=''.join(invP[(O[ord(z)-97]-K[j%x['m']]-179*(j//x['m']))%26]for j,z in enumerate(c[x['offset']:]))
  print('SAT',i,r['full_context_decode'],flush=True)
 rows.append(row);(out/'finite-completion.json').write_text(json.dumps(rows,indent=2)+'\n');print(i,r['status'],r.get('finite_enumeration'),flush=True)
