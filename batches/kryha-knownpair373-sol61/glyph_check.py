from pathlib import Path
from crt import solve
import json,concurrent.futures
B=Path(__file__).resolve().parent;old=json.loads((B/'results.json').read_text());cases=[r['case']for r in old];base=Path('batches/kryha373-collation-sol61/ciphertext650.txt').read_text().strip();assert base[52]=='l'and base[89]=='e'
def task(x):
 ca,L,E,short=x;ct=list(base);ct[52]=L;ct[89]=E;full=''.join(ct)[ca['omitprefix']:ca['omitprefix']+len(ca['p'])];p=ca['p'];c=full
 if short:p=p[:73];c=c[:73]
 r=solve(p,c,ca['m'],3000 if short else 2000,heldout=(ca['p'],full)if short else None);r.update(case=ca,glyph53=L,glyph90=E,fit73=short)
 if r['status']=='sat':r['second_witness']=solve(p,c,ca['m'],1000,blocked=r)
 return r
if __name__=='__main__':
 fulltasks=[(c,L,E,False)for c in cases for L,E in [('l','a'),('i','e'),('i','a')]];shorttasks=[(c,L,'e',True)for c in cases if c['m']in[20,21,23,25]for L in ['l','i']]
 for label,tasks in [('glyph-full',fulltasks),('glyph-fit73',shorttasks)]:
  rows=[]
  with concurrent.futures.ProcessPoolExecutor(max_workers=3)as pool:
   for r in pool.map(task,tasks):
    rows.append(r)
    if r['status']=='sat':print(label,r['case']['label'],r['case']['omitprefix'],r['m'],r['glyph53'],r['glyph90'],r.get('heldout_matches'),r.get('heldout_total'),flush=True)
  (B/f'{label}.json').write_text(json.dumps(rows,indent=2)+'\n');print(label,len(rows),{s:sum(r['status']==s for r in rows)for s in ['sat','unsat','unknown']},flush=True)
