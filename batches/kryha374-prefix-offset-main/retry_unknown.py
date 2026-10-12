from pathlib import Path
import sys,json,time
root=Path(__file__).resolve().parents[2];out=Path(__file__).resolve().parent
sys.path.insert(0,str(root/'batches/kryha-knownpair373-sol61'))
from crt import solve
ct=(root/'batches/kryha373-collation-sol61/ciphertext650.txt').read_text().strip().lower();results=[]
for i,x in enumerate(json.loads((out/'unknown-cases.json').read_text())):
 cc=list(ct);cc[52]=x['glyph53'];cc[89]=x['glyph90'];cc=''.join(cc);p=x['p'];c=cc[x['offset']:x['offset']+len(p)];r=solve(p,c,x['m'],30000);case=dict(x,retry=r)
 if r['status']=='sat':
  P,O,K=r['P'],r['O'],r['K'];inv={v:chr(97+i)for i,v in enumerate(P)};r['full_context_decode']=''.join(inv[(O[ord(z)-97]-K[i%x['m']]-179*(i//x['m']))%26]for i,z in enumerate(cc[x['offset']:]))
  print('SAT',i,r['full_context_decode'],flush=True)
 results.append(case);(out/'unknown-retries.json').write_text(json.dumps(results,indent=2)+'\n');print(i,r['status'],r.get('seconds'),flush=True)
