from pathlib import Path
from crt import solve,expressions
import random,json
B=Path(__file__).resolve().parent;t=json.loads((B/'control-truth.json').read_text());p=t['p'];out=[]
for m,seed in [(20,3732020),(30,3733030)]:
 rng=random.Random(seed);P=rng.sample(range(26),26);O=rng.sample(range(26),26);K=[rng.randrange(26)for _ in range(m)];inv={v:chr(97+i)for i,v in enumerate(O)};c=''.join(inv[(P[ord(a)-97]+K[i%m]+179*(i//m))%26]for i,a in enumerate(p));r=solve(p,c,m,5000);assert r['status']=='sat';pi={v:chr(97+i)for i,v in enumerate(r['P'])};back=''.join(pi[(r['O'][ord(b)-97]-r['K'][i%m]-179*(i//m))%26]for i,b in enumerate(c));assert back==p;r['independent_inverse_exact']=True
 scan=[solve(p,c,j,1000)for j in range(2,53)];h=solve(p[:-20],c[:-20],m,5000,heldout=(p,c));out.append({'planted':{'m':m,'P':P,'O':O,'K':K,'p':p,'c':c},'fit':r,'unknown_period_scan':scan,'heldout':h});print(m,r['status'],'feasible',[x['m']for x in scan if x['status']=='sat'],'heldout',h.get('heldout_matches'),flush=True)
(B/'additional-controls.json').write_text(json.dumps(out,indent=2)+'\n')
# Difference between complete-key witnesses is not evaluated as planted-key recovery.
a=json.loads((B/'crt-control-fullfit.json').read_text());b=json.loads((B/'crt-control-second-witness.json').read_text());usedp=set(p);usedc=set(t['c']);d={'P_changed':[chr(97+i)for i in range(26)if a['P'][i]!=b['P'][i]],'O_changed':[chr(97+i)for i in range(26)if a['O'][i]!=b['O'][i]],'K_changed':[i for i in range(23)if a['K'][i]!=b['K'][i]],'used_plaintext_letters':sorted(usedp),'used_ciphertext_letters':sorted(usedc)};d['all_changes_unused']=not(d['K_changed'])and all(x not in usedp for x in d['P_changed'])and all(x not in usedc for x in d['O_changed']);(B/'second-witness-diagnosis.json').write_text(json.dumps(d,indent=2)+'\n')
