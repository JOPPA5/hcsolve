from model import z3
import time
from finite import enumerate_observed

def expressions(rows,n,q):
 a=[[v%q for v in r]for r in rows];piv=[];at=0
 for col in range(n):
  k=next((j for j in range(at,len(a))if a[j][col]),None)
  if k is None:continue
  a[at],a[k]=a[k],a[at];inv=pow(a[at][col],-1,q);a[at]=[(v*inv)%q for v in a[at]]
  for j in range(len(a)):
   if j!=at and a[j][col]:
    mul=a[j][col];a[j]=[(x-mul*y)%q for x,y in zip(a[j],a[at])]
  piv.append(col);at+=1
  if at==len(a):break
 if any(not any(r[:n])and r[n]for r in a):return None,None
 free=[i for i in range(n)if i not in piv];xs={i:z3.Int(f'q{q}_{i}')for i in free};expr=[None]*n
 for i in free:expr[i]=xs[i]
 for col,r in zip(piv,a):expr[col]=(r[n]-sum(r[i]*xs[i]for i in free if r[i]))%q
 return expr,list(xs.values())

def solve(p,c,m,timeout=10000,blocked=None,heldout=None,press_indices=None):
 n=52+m;rows=[];press_indices=list(range(len(heldout[0])if heldout else len(p)))if press_indices is None else press_indices;assert len(press_indices)>=len(p)
 for i,(a,b)in enumerate(zip(p,c)):
  r=[0]*(n+1);r[26+ord(b)-97]+=1;r[ord(a)-97]-=1;r[52+press_indices[i]%m]-=1;r[-1]=179*(press_indices[i]//m);rows.append(r)
 for j in [0,26]:r=[0]*(n+1);r[j]=1;rows.append(r)
 e2,v2=expressions(rows,n,2);e13,v13=expressions(rows,n,13)
 if e2 is None or e13 is None:return dict(status='unsat',reason='linear CRT inconsistency',m=m,seconds=0)
 s=z3.Solver();s.set(timeout=timeout,random_seed=373374)
 for x in v2:s.add(x>=0,x<2)
 for x in v13:s.add(x>=0,x<13)
 x=[z3.IntVal(a+13*((b-a)%2))if isinstance(a,int)and isinstance(b,int)else a+13*((b-a)%2)for a,b in zip(e13,e2)];observed=[sorted({ord(ch)-97 for ch in text}|{0})for text in [p,c]]
 s.add(z3.Distinct([x[i]for i in observed[0]]),z3.Distinct([x[26+i]for i in observed[1]]))
 if blocked:
  relevant=observed[0]+[26+i for i in observed[1]]+list(range(52,n));old=blocked['P']+blocked['O']+blocked['K'];s.add(z3.Or([x[i]!=old[i]for i in relevant]))
 finite=None if blocked else enumerate_observed(e2,v2,e13,v13,observed[0]+[26+i for i in observed[1]])
 t=time.monotonic();r=(z3.sat if finite['status']=='sat'else z3.unsat)if finite else s.check();out=dict(status=str(r),seconds=time.monotonic()-t,m=m,fitted_positions=len(p),nullity2=len(v2),nullity13=len(v13),timeout_ms=timeout,unused_letter_completion=True,observed_input_slots=len(observed[0]),observed_output_slots=len(observed[1]))
 if finite:out.update(finite_enumeration={k:v for k,v in finite.items()if k!='values'},seconds=finite['seconds'])
 if r==z3.sat:
  if finite:values=finite['values']
  else:
   md=s.model();values=[md.eval(a).as_long()if isinstance(a,z3.ExprRef)else a for a in x]
  P,O,K=values[:26],values[26:52],values[52:]
  for ring,known in zip([P,O],observed):
   remaining=iter(sorted(set(range(26))-{ring[i]for i in known}))
   for i in range(26):
    if i not in known:ring[i]=next(remaining)
  inv={v:chr(97+i)for i,v in enumerate(O)}
  assert ''.join(inv[(P[ord(a)-97]+K[press_indices[i]%m]+179*(press_indices[i]//m))%26]for i,a in enumerate(p))==c
  out.update(P=P,O=O,K=K,full_fit_reencryption_exact=True)
  if heldout:
   pp,cc=heldout;pi={v:chr(97+i)for i,v in enumerate(P)};decoded=''.join(pi[(O[ord(b)-97]-K[press_indices[i]%m]-179*(press_indices[i]//m))%26]for i,b in enumerate(cc));out.update(heldout_decoded=decoded,heldout_expected=pp,heldout_matches=sum(a==b for a,b in zip(decoded[len(p):],pp[len(p):])),heldout_total=len(pp)-len(p),heldout_full_exact=decoded==pp)
 else:out['reason']=s.reason_unknown()if r==z3.unknown else'linear family incompatible with ring permutations'
 return out
