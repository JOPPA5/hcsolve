from pathlib import Path
import sys,json,time,itertools,collections
sys.path.insert(0,str(Path(__file__).resolve().parent))
from reencrypt_periodic import a,b
from periodic_algebra import solve as ring_solve
p=Path(__file__).resolve().parent;prime=13
def matrix(inp,out,T):
 n=53+T;rows=[]
 for i,(x,y)in enumerate(zip(inp,out)):
  r=[0]*n;r[26+ord(y)-97]+=1;r[ord(x)-97]-=1;r[52+i%T]-=1;r[-1]-=i//T;rows.append([v%13 for v in r])
 for j in (0,52):r=[0]*n;r[j]=1;rows.append(r)
 return rows

def certificate(inp,out,T):
 started=time.monotonic();A=matrix(inp,out,T);n=len(A[0]);echelon={};basis=[]
 for idx,row in enumerate(A):
  v=row.copy()
  for c,r in echelon.items():
   if v[c]:f=v[c];v=[(x-f*y)%13 for x,y in zip(v,r)]
  c=next((j for j,x in enumerate(v)if x),None)
  if c is not None:
   inv=pow(v[c],-1,13);echelon[c]=[(x*inv)%13 for x in v];basis.append(idx)
  if len(basis)==n:break
 if len(basis)<n:return dict(period=T,status='NOT_FULL_RANK',rank=len(basis),seconds=time.monotonic()-started)
 # Invert square basis matrix, then obtain a systematic parity-check matrix H.
 B=[A[idx].copy()+[int(rowno==j)for j in range(n)]for rowno,idx in enumerate(basis)]
 for c in range(n):
  r=next(j for j in range(c,n)if B[j][c]);B[c],B[r]=B[r],B[c];inv=pow(B[c][c],-1,13);B[c]=[(x*inv)%13 for x in B[c]]
  for j in range(n):
   if j!=c and B[j][c]:f=B[j][c];B[j]=[(x-f*y)%13 for x,y in zip(B[j],B[c])]
 inverse=[r[n:]for r in B];assert all(B[i][j]==int(i==j)for i in range(n)for j in range(n));assert all(sum(A[basis[i]][k]*inverse[k][j]for k in range(n))%13==int(i==j)for i in range(n)for j in range(n));nonbase=[i for i in range(len(A))if i not in basis];H=[[0]*len(nonbase)for _ in A]
 for j,idx in enumerate(nonbase):
  coeff=[sum(A[idx][k]*inverse[k][c]for k in range(n))%13 for c in range(n)]
  for c,orig in enumerate(basis):H[orig][j]=-coeff[c]%13
  H[idx][j]=1
 # Error flags apply only to cipher positions, not the two fixed normalization equations.
 active=[i for i in basis if i<len(inp)];unit={j:i for j,i in enumerate(nonbase)if i<len(inp)}
 def found(support):return dict(period=T,status='SPARSE_CODEWORD',support=sorted(support),seconds=time.monotonic()-started)
 # Cases with zero, one or two basis coordinates; remaining nonbasis columns are distinct unit vectors.
 for i in active:
  supp=[j for j,v in enumerate(H[i])if v]
  if len(supp)<=2 and all(j in unit for j in supp):return found([i]+[unit[j]for j in supp])
 independent={}
 for aa,i in enumerate(active):
  u=H[i]
  for j in active[aa+1:]:
   v=H[j]
   # Every nonzero combination of two basis columns must have >=2 nonbasis coordinates.
   for t in range(1,13):
    supp=[]
    for k,(x,y)in enumerate(zip(u,v)):
     if (x+t*y)%13:
      supp.append(k)
      if len(supp)>1:break
    if len(supp)<=1 and all(k in unit for k in supp):return found([i,j]+[unit[k]for k in supp])
   k=next((k for k,x in enumerate(u)if x),None)
   # Find a 2x2 nonsingular minor for solving any candidate third column against this pair.
   l=next((l for l in range(len(u))if (u[k]*v[l]-u[l]*v[k])%13),None)
   if l is not None:independent[(i,j)]=(k,l,pow((u[k]*v[l]-u[l]*v[k])%13,-1,13))
 # Three basis coordinates: exact linear-dependence test, coefficients solved by one nonsingular minor.
 for aa,i in enumerate(active):
  u=H[i]
  for bb in range(aa+1,len(active)):
   j=active[bb];v=H[j];minor=independent.get((i,j))
   if minor is None:continue
   k,l,inv=minor
   for h in active[bb+1:]:
    w=H[h];alpha=(w[k]*v[l]-w[l]*v[k])*inv%13;beta=(u[k]*w[l]-u[l]*w[k])*inv%13
    if not alpha or not beta:continue
    if all((alpha*x+beta*y-z)%13==0 for x,y,z in zip(u,v,w)):return found([i,j,h])
 return dict(period=T,status='NO_CODEWORD_WEIGHT_LE3',rank=n,basis_error_columns=len(active),parity_check_rows=len(nonbase),seconds=time.monotonic()-started)
if __name__=='__main__':
 controls=json.loads((p/'periodic-algebra-controls.json').read_text());checks=[]
 for c in controls:
  out=list(c['output'])
  for i in (31,167,302):out[i]=chr((ord(out[i])-97+11)%26+97)
  out=''.join(out);r=certificate(c['input'],out,c['result']['period']);assert r['status']=='SPARSE_CODEWORD',r;recovery=ring_solve(c['input'],out,c['result']['period'],r['support']);assert recovery['status']=='SAT' and recovery['reproduced']==c['output'];checks.append(dict(period=c['result']['period'],typo_positions=[31,167,302],result=r,recovered_underlying_control=recovery));print('CONTROL3',r,flush=True)
 (p/'periodic-three-error-controls.json').write_text(json.dumps(checks,indent=2));results=[]
 for T in range(1,53):
  r=certificate(a,b,T);results.append(r);print('TARGET3',r,flush=True);(p/'periodic-three-error-target.json').write_text(json.dumps(results,indent=2))
