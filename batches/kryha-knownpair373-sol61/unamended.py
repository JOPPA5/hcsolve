from pathlib import Path
from crt import solve
from selective import steps
import json,random,concurrent.futures
B=Path(__file__).resolve().parent;old=json.loads((B/'results.json').read_text());base=Path('batches/kryha373-collation-sol61/ciphertext650.txt').read_text().strip();cases=[]
for r in old:
 c=r['case'].copy();p=c['p'];assert p.count('ustredni')==1;at=p.index('ustredni')+5;assert p[at]=='d';c.update(p=p[:at]+p[at+1:],deleted_d_position1=at+1,preparation_stage='unamended typed USTRENI before handwritten D insertion');cases.append(c)
def control(ca=None,selective=False,seed=3733742701):
 p=(ca or cases[0])['p'];ix=steps(p)if selective else list(range(len(p)));rng=random.Random(seed);m=23;P=rng.sample(range(26),26);O=rng.sample(range(26),26);K=[rng.randrange(26)for _ in range(m)];inv={v:chr(97+i)for i,v in enumerate(O)};c=''.join(inv[(P[ord(a)-97]+K[ix[i]%m]+179*(ix[i]//m))%26]for i,a in enumerate(p));fit=solve(p,c,m,5000,press_indices=ix);assert fit['status']=='sat';h=solve(p[:-20],c[:-20],m,5000,heldout=(p,c),press_indices=ix);scan=[solve(p,c,j,1000,press_indices=ix)for j in range(2,53)];return dict(planted=dict(p=p,c=c,m=m,P=P,O=O,K=K),fit=fit,heldout=h,unknown_period=scan)
def task(x):
 ca,L,E,selective=x;ct=list(base);ct[52]=L;ct[89]=E;p=ca['p'];c=''.join(ct)[ca['omitprefix']:ca['omitprefix']+len(p)];ix=steps(p)if selective else list(range(len(p)));r=solve(p,c,ca['m'],2000,press_indices=ix);r.update(case=ca,glyph53=L,glyph90=E,selectiveJ=selective)
 if r['status']=='sat':
  r['second_witness']=solve(p,c,ca['m'],1000,press_indices=ix,blocked=r);r['heldout']=solve(p[:-20],c[:-20],ca['m'],1000,press_indices=ix,heldout=(p,c))
 return r
if __name__=='__main__':
 co=control();(B/'unamended-control.json').write_text(json.dumps(co,indent=2)+'\n');print('control',co['fit']['status'],'heldout',co['heldout'].get('heldout_matches'),co['heldout'].get('heldout_total'),flush=True)
 sj=control(next(c for c in cases if c['separator']=='j'and c['natural_j_to_i']),True,3733742702);(B/'unamended-selective-control-reproduction.json').write_text(json.dumps(sj,indent=2)+'\n');assert sj['fit']['status']=='sat'
 stages=[('unamended-none',[c for c in cases if c['separator']==''],False),('unamended-markers',[c for c in cases if c['separator']!=''],False),('unamended-selective',[c for c in cases if 'j'in c['p']],True)]
 for label,sub,sel in stages:
  out=[]
  with concurrent.futures.ProcessPoolExecutor(max_workers=3)as pool:
   for r in pool.map(task,[(c,L,E,sel)for c in sub for L in ['l','i']for E in ['e','a']]):
    out.append(r)
    if r['status']=='sat':print(label,r['case']['label'],r['m'],r['case']['omitprefix'],r['glyph53'],r['glyph90'],'heldout',r['heldout'].get('heldout_matches'),r['heldout'].get('heldout_total'),flush=True)
  (B/f'{label}.json').write_text(json.dumps(out,indent=2)+'\n');print(label,len(out),{s:sum(r['status']==s for r in out)for s in ['sat','unsat','unknown']},flush=True)
