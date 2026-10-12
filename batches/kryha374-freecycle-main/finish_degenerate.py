from pathlib import Path
import json,time
from crt_finite import solve
out=Path(__file__).resolve().parent;root=out.parents[1]
controls=json.loads((out/'controls.json').read_text());results=[]
for j,x in enumerate(controls):
 r=solve(x['p'],x['c'],x['m'],2000,cycle=x['planted_D']);results.append(dict(control_index=j,cycle=x['planted_D'],result=r));(out/'finite-controls.json').write_text(json.dumps(results,indent=2)+'\n');print('control',j,x['planted_D'],r['status'],r.get('finite_enumeration'),flush=True)
 if r['status']!='sat':raise SystemExit('Incomplete positive calibration; no actualdegeneratecases')
ct=(root/'batches/kryha373-collation-sol61/ciphertext650.txt').read_text().strip().lower();preps=json.loads((out/'preparations.json').read_text());actual=[];t=time.monotonic()
for D in [0,13]:
 for prep in preps:
  for omit in [0,5]:
   for a in ['l','i']:
    for b in ['e','a']:
     c=list(ct);c[52]=a;c[89]=b;c=''.join(c)
     for m in range(2,53):
      r=solve(prep['p'],c[omit:omit+len(prep['p'])],m,2000,cycle=D);case=dict(cycle=D,p=prep['p'],omit=omit,glyph53=a,glyph90=b,m=m,result=r)
      if r['status']=='sat':
       P,O,K=r['P'],r['O'],r['K'];inv={v:chr(97+i)for i,v in enumerate(P)};r['full_context_decode']=''.join(inv[(O[ord(x)-97]-K[i%m]-D*(i//m))%26]for i,x in enumerate(c[omit:]));print('SAT',case,flush=True)
      actual.append(case)
     (out/'degenerate-actual.json').write_text(json.dumps(actual,indent=2)+'\n');print('progress',D,len(actual),round(time.monotonic()-t,1),flush=True)
(out/'degenerate-summary.json').write_text(json.dumps(dict(cases=len(actual),counts={s:sum(x['result']['status']==s for x in actual)for s in ['sat','unsat','unknown']},seconds=time.monotonic()-t),indent=2)+'\n')
