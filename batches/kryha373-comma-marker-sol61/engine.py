from pathlib import Path
import sys,json,hashlib
sys.path.insert(0,str(Path('batches/kryha373-unemitted-spaces-sol61').resolve()))
from crt import expressions
sys.path.insert(0,str(Path('batches/kryha373-invisible-finite-sol61').resolve()))
from vector import enumerate_observed
b=Path(__file__).resolve().parent;old=Path('batches/kryha373-unemitted-spaces-sol61')
def fit(p,c,ix,m):
 n=52+m;rows=[]
 for a,cc,t in zip(p,c,ix):
  r=[0]*(n+1);r[26+ord(cc)-97]+=1;r[ord(a)-97]-=1;r[52+t%m]-=1;r[-1]=179*(t//m);rows.append(r)
 for j in [0,26]:r=[0]*(n+1);r[j]=1;rows.append(r)
 e2,v2=expressions(rows,n,2);e13,v13=expressions(rows,n,13)
 if e2 is None or e13 is None:return dict(status='unsat',reason='linear CRT inconsistency')
 obs=[sorted({ord(ch)-97 for ch in s}|{0})for s in [p,c]];r=enumerate_observed(e2,v2,e13,v13,obs[0]+[26+i for i in obs[1]])
 if r['status']=='sat':
  vals=r.pop('values');P,O,K=vals[:26],vals[26:52],vals[52:]
  for ring,known in zip([P,O],obs):
   rest=iter(sorted(set(range(26))-{ring[i]for i in known}))
   for i in range(26):
    if i not in known:ring[i]=next(rest)
  assert sorted(P)==sorted(O)==list(range(26));ip={v:chr(97+i)for i,v in enumerate(P)};io={v:chr(97+i)for i,v in enumerate(O)}
  enc=''.join(io[(P[ord(a)-97]+K[t%m]+179*(t//m))%26]for a,t in zip(p,ix));dec=''.join(ip[(O[ord(a)-97]-K[t%m]-179*(t//m))%26]for a,t in zip(c,ix));assert enc==c and dec==p
  r.update(P=P,O=O,K=K,independent_full_prefix_encoder_inverse=True)
 return r
