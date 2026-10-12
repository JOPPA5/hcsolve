from pathlib import Path
import json,hashlib
from crt import solve
b=Path(__file__).resolve().parent
def check(r,p,c,ix):
 if r['status']!='sat':return
 P,O,K,m=r['P'],r['O'],r['K'],r['m'];assert sorted(P)==sorted(O)==list(range(26));ip={v:chr(97+i)for i,v in enumerate(P)};io={v:chr(97+i)for i,v in enumerate(O)};dec='';enc=''
 for ch,cipher,t in zip(p,c,ix):
  d=K[t%m]+179*(t//m);enc+=io[(P[ord(ch)-97]+d)%26];dec+=ip[(O[ord(cipher)-97]-d)%26]
 assert enc==c and dec==p;r['independent_full_prefix_encoder_inverse']=True
if __name__=='__main__':
 audits=[]
 for j in range(8):
  v=json.loads((b/f'control{j}-input.json').read_text());p=v['case']['p'];ix=v['case']['press_indices'];c=v['ciphertext'];f=b/f'control{j}-blind-periods.json'
  if f.exists():rows=json.loads(f.read_text())
  else:
   rows=[]
   for m in range(2,53):
    r=solve(p,c,m,2000,press_indices=ix);check(r,p,c,ix);rows.append(r)
   f.write_text(json.dumps(rows,indent=2)+'\n')
  updated=[]
  for r in rows:
   if r['status']=='unknown':
    new=solve(p,c,r['m'],2000,press_indices=ix);check(new,p,c,ix);new['previous_status']='unknown';updated.append(new)
   else:updated.append(r)
  rows=updated;(b/f'control{j}-unused-completion-periods.json').write_text(json.dumps(rows,indent=2)+'\n')
  truth=json.loads((b/f'control{j}-truth.json').read_text());r=next(z for z in rows if z['m']==truth['m']);assert r['status']=='sat';h=solve(p[:-20],c[:-20],truth['m'],5000,press_indices=ix,heldout=(p,c));check(h,p[:-20],c[:-20],ix[:-20]);(b/f'control{j}-heldout.json').write_text(json.dumps(h,indent=2)+'\n');audit=dict(control=j,length=len(p),extra=v['case']['extra'],policy=v['case']['policy'],unamended=v['case']['unamended'],natural_j_to_i=v['case']['natural_j_to_i'],original_scan_sha256=hashlib.sha256(f.read_bytes()).hexdigest(),blind_periods_sha256=hashlib.sha256((b/f'control{j}-unused-completion-periods.json').read_bytes()).hexdigest(),truth_read_after_all_blind_periods_saved=True,planted_period=truth['m'],planted_period_accepted=True,sat_periods=[z['m']for z in rows if z['status']=='sat'],unknown_periods=[z['m']for z in rows if z['status']=='unknown'],heldout_status=h['status'],heldout_matches=h.get('heldout_matches'),heldout_total=20,whole_fit_independently_verified=True);audits.append(audit);(b/'controls-summary.json').write_text(json.dumps(audits,indent=2)+'\n');print('control',j,len(p),v['case']['extra'],v['case']['policy'],'SAT',audit['sat_periods'],'heldout',audit['heldout_matches'],flush=True)
