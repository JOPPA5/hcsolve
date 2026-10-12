"""Published373 context toward unresolved374; arbitrary cycle residue, not physical machine proof."""
from pathlib import Path
import json,random,time,sys
from crt_free import solve
out=Path(__file__).resolve().parent;root=out.parents[1]
preps=json.loads((root/'batches/kryha374-qcontext-main/preparations.json').read_text())['variants']
ct=(root/'batches/kryha373-collation-sol61/ciphertext650.txt').read_text().strip().lower()
controls=[]
for j,D in enumerate([0,2,13,23]):
 rng=random.Random(37437362120+j);p=preps[j%len(preps)]['p'];m=17+j;P=rng.sample(range(26),26);O=rng.sample(range(26),26);K=[rng.randrange(26)for _ in range(m)];inv={v:chr(97+i)for i,v in enumerate(O)}
 c=''.join(inv[(P[ord(a)-97]+K[i%m]+D*(i//m))%26]for i,a in enumerate(p))
 r=solve(p,c,m,10000);controls.append(dict(p=p,c=c,m=m,planted_P=P,planted_O=O,planted_K=K,planted_D=D,result=r));(out/'controls.json').write_text(json.dumps(controls,indent=2)+'\n');print('CONTROL',j,r['status'],r.get('D'),flush=True)
 if r['status']!='sat':raise SystemExit('Blind calibration failed, target not run')
results=[];t=time.monotonic()
# Include unmarked names in addition to the new Q hypotheses; source words unchanged.
preps=preps+[dict(x,p=x['p'].replace('q',''),Q_markers_removed=True)for x in preps[::4]+preps[1::4]+preps[2::4]+preps[3::4]]
seen=set();preps=[x for x in preps if not(x['p']in seen or seen.add(x['p']))]
(out/'preparations.json').write_text(json.dumps(preps,indent=2)+'\n')
for prep in preps:
 for omit in [0,5]:
  for a in ['l','i']:
   for b in ['e','a']:
    cc=list(ct);cc[52]=a;cc[89]=b;cc=''.join(cc)
    for m in range(2,53):
     c=cc[omit:omit+len(prep['p'])];r=solve(prep['p'],c,m,1500);case=dict(p=prep['p'],omit=omit,glyph53=a,glyph90=b,m=m,result=r)
     if r['status']=='sat':
      P,O,K,D=r['P'],r['O'],r['K'],r['D'];inv={v:chr(97+i)for i,v in enumerate(P)}
      r['full_context_decode']=''.join(inv[(O[ord(z)-97]-K[i%m]-D*(i//m))%26]for i,z in enumerate(cc[omit:]));print('SAT',len(results),m,D,r['full_context_decode'],flush=True)
     results.append(case)
    (out/'results.json').write_text(json.dumps(results,indent=2)+'\n')
    print('progress',len(results),'elapsed',round(time.monotonic()-t,1),flush=True)
(out/'summary.json').write_text(json.dumps(dict(cases=len(results),counts={s:sum(x['result']['status']==s for x in results)for s in ['sat','unsat','unknown']},seconds=time.monotonic()-t),indent=2)+'\n')
