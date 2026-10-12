import sys,time
sys.path.insert(0,'/private/tmp/hcsolve-z3')
import z3

def solve(p,c,m,timeout=3000,blocked=None,heldout=None):
 assert len(p)==len(c)
 s=z3.Solver();s.set(timeout=timeout,random_seed=373374)
 P=[z3.Int('P'+str(i))for i in range(26)];O=[z3.Int('O'+str(i))for i in range(26)];K=[z3.Int('K'+str(i))for i in range(m)]
 for x in P+O+K:s.add(x>=0,x<26)
 s.add(z3.Distinct(P),z3.Distinct(O),P[0]==0,O[0]==0)
 for i,(a,b)in enumerate(zip(p,c)):s.add((O[ord(b)-97]-P[ord(a)-97]-K[i%m]-179*(i//m))%26==0)
 if blocked:s.add(z3.Or([x!=v for x,v in zip(P+O+K,blocked['P']+blocked['O']+blocked['K'])]))
 t=time.monotonic();r=s.check();out={'status':str(r),'seconds':time.monotonic()-t,'m':m,'fitted_positions':len(p),'timeout_ms':timeout}
 if r==z3.sat:
  model=s.model();ps=[model.eval(x).as_long()for x in P];os=[model.eval(x).as_long()for x in O];ks=[model.eval(x).as_long()for x in K]
  out.update(P=ps,O=os,K=ks)
  inv={v:chr(97+i)for i,v in enumerate(os)};pred=''.join(inv[(ps[ord(a)-97]+ks[i%m]+179*(i//m))%26]for i,a in enumerate(p));assert pred==c;out['full_fit_reencryption_exact']=True
  if heldout:
   pp,cc=heldout;assert len(pp)==len(cc);o_inv={v:chr(97+i)for i,v in enumerate(ps)};decoded=''.join(o_inv[(os[ord(b)-97]-ks[i%m]-179*(i//m))%26]for i,b in enumerate(cc));out.update(heldout_decoded=decoded,heldout_expected=pp,heldout_matches=sum(a==b for a,b in zip(decoded[len(p):],pp[len(p):])),heldout_total=len(pp)-len(p),heldout_full_exact=decoded==pp)
 else:out['reason']=s.reason_unknown()if r==z3.unknown else'UNSAT in declared modular family'
 return out
