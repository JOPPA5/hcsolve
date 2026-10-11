from pathlib import Path
from crt import solve
import random,json,concurrent.futures
B=Path(__file__).resolve().parent
def steps(p):
 out=[];n=0
 for ch in p:out.append(n);n+=2 if ch=='j' else 1
 return out
# Independent matched controls with unknown alphabet/schedule, before actual extension.
def control(m,seed):
 ca=json.loads((B/'preparation-cases.json').read_text())['hypotheses'];p=next(r['p']for r in ca if r['separator']=='j'and r['natural_j_to_i']);rng=random.Random(seed);P=rng.sample(range(26),26);O=rng.sample(range(26),26);K=[rng.randrange(26)for _ in range(m)];inv={v:chr(97+i)for i,v in enumerate(O)};ix=steps(p);c=''.join(inv[(P[ord(a)-97]+K[n%m]+179*(n//m))%26]for a,n in zip(p,ix));r=solve(p,c,m,5000,press_indices=ix);assert r['status']=='sat';h=solve(p[:73],c[:73],m,5000,press_indices=ix,heldout=(p,c));scan=[solve(p,c,j,1000,press_indices=ix)for j in range(2,53)];return dict(planted=dict(p=p,c=c,P=P,O=O,K=K,m=m),fit=r,heldout=h,unknown_period_scan=scan)
def target(row):
 ca=row['case'];p=ca['p'];base=Path('batches/kryha373-collation-sol61/ciphertext650.txt').read_text().strip();ct=list(base);ct[52]=row['glyph53'];ct[89]=row['glyph90'];c=''.join(ct)[ca['omitprefix']:ca['omitprefix']+len(p)];r=solve(p,c,ca['m'],2000,press_indices=steps(p));r.update(case=ca,glyph53=row['glyph53'],glyph90=row['glyph90'],press_rule='extra one stop advance after literal prepared J')
 if r['status']=='sat':
  r['second_witness']=solve(p,c,ca['m'],1000,blocked=r,press_indices=steps(p));r['heldout']=solve(p[:73],c[:73],ca['m'],1000,heldout=(p,c),press_indices=steps(p))
 return r
if __name__=='__main__':
 controls=[control(23,3732302),control(30,3733002)];(B/'selective-controls.json').write_text(json.dumps(controls,indent=2)+'\n');print('controls',[(c['planted']['m'],c['fit']['status'],c['heldout'].get('heldout_matches'),c['heldout'].get('heldout_total'))for c in controls],flush=True)
 rows=json.loads((B/'results.json').read_text())
 for r in rows:r.update(glyph53='l',glyph90='e')
 rows+=json.loads((B/'glyph-full.json').read_text());results=[]
 # J-extra is identical when the prepared string contains no J; retain deduplicated scope.
 rows=[r for r in rows if 'j'in r['case']['p']]
 with concurrent.futures.ProcessPoolExecutor(max_workers=3)as pool:
  for r in pool.map(target,rows):
   results.append(r)
   if r['status']=='sat':print(r['case']['label'],r['m'],r['case']['omitprefix'],r['glyph53'],r['glyph90'],r['heldout'].get('heldout_matches'),flush=True)
 (B/'selective-results.json').write_text(json.dumps(results,indent=2)+'\n');print('target',len(results),{s:sum(r['status']==s for r in results)for s in ['sat','unsat','unknown']},flush=True)
