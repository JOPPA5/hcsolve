from pathlib import Path
import sys,json,time,random,itertools,collections
sys.path.insert(0,str(Path(__file__).resolve().parent))
from reencrypt_periodic import a,b,shifts
p=Path(__file__).resolve().parent
def nullspace(inp,out,T,prime,ignored=()):
 n=53+T;rows=[]
 for i,(x,y)in enumerate(zip(inp,out)):
  if i in ignored:continue
  row=[0]*n;row[26+ord(y)-97]+=1;row[ord(x)-97]-=1;row[52+i%T]-=1;row[-1]-=i//T;rows.append([v%prime for v in row])
 for j in (0,52):row=[0]*n;row[j]=1;rows.append(row)
 pivot=[];r=0
 for c in range(n):
  at=next((j for j in range(r,len(rows))if rows[j][c]),None)
  if at is None:continue
  rows[r],rows[at]=rows[at],rows[r];inv=pow(rows[r][c],-1,prime);rows[r]=[(v*inv)%prime for v in rows[r]]
  for j in range(len(rows)):
   if j!=r and rows[j][c]:
    v=rows[j][c];rows[j]=[(x-v*y)%prime for x,y in zip(rows[j],rows[r])]
  pivot.append(c);r+=1
  if r==len(rows):break
 free=[c for c in range(n)if c not in pivot];basis=[]
 for c in free:
  v=[0]*n;v[c]=1
  for j,col in enumerate(pivot):v[col]=-rows[j][c]%prime
  basis.append(v)
 return basis
def forms(basis,prime):
 if not basis:yield None;return
 for coeff in itertools.product(range(prime),repeat=len(basis)):
  if not any(coeff):continue
  yield [sum(c*v[i]for c,v in zip(coeff,basis))%prime for i in range(len(basis[0]))]
def solve(inp,out,T,ignored=()):
 start=time.monotonic();u=nullspace(inp,out,T,13,ignored);v=nullspace(inp,out,T,2,ignored);rec=dict(period=T,nullity13=len(u),nullity2=len(v));
 if not u or not v:rec.update(status='UNSAT',reason='zero nullspace in a prime component forces nonpermutation rings',seconds=time.monotonic()-start);return rec
 if len(u)>3 or len(v)>8:rec.update(status='UNRESOLVED',reason='nullspace enumeration budget exceeded',seconds=time.monotonic()-start);return rec
 vs=list(forms(v,2))
 for x in forms(u,13):
  if any(max(collections.Counter(x[j:j+26]).values())>2 for j in (0,26)):continue
  for y in vs:
   z=[r if r%2==t else r+13 for r,t in zip(x,y)]
   if len(set(z[:26]))<26 or len(set(z[26:52]))<26:continue
   rs=z[52:52+T];cycle=z[-1];steps=[(rs[i+1]-rs[i])%26 for i in range(T-1)]+[(cycle-rs[-1])%26];d=shifts(len(inp),steps);ringout={r:chr(97+j)for j,r in enumerate(z[26:52])};reproduced=''.join(ringout[(z[ord(c)-97]+r)%26]for c,r in zip(inp,d));assert all(x==y for i,(x,y)in enumerate(zip(reproduced,out))if i not in ignored)
   rec.update(actual_mismatch_positions=[i for i,(x,y)in enumerate(zip(reproduced,out))if x!=y],status='SAT',ring_in=z[:26],ring_out=z[26:52],steps=steps,reproduced=reproduced,seconds=time.monotonic()-start);return rec
 rec.update(status='UNSAT',reason='exhausted all CRT nullspace combinations, none are ring permutations',seconds=time.monotonic()-start);return rec
if __name__=='__main__':
 rng=random.Random(35035152);controls=[]
 for T in (17,26,52):
  iv=list(range(26));ov=list(range(26));rng.shuffle(iv);rng.shuffle(ov);steps=[rng.randrange(26)for _ in range(T)];d=shifts(len(a),steps);ringout={r:chr(97+j)for j,r in enumerate(ov)};out=''.join(ringout[(iv[ord(c)-97]+r)%26]for c,r in zip(a,d));rec=solve(a,out,T);assert rec['status']=='SAT' and rec['reproduced']==out;controls.append(dict(input=a,output=out,planted_input_ring=iv,planted_output_ring=ov,planted_steps=steps,result=rec));print('CONTROL',T,rec['status'],rec['nullity13'],rec['nullity2'],flush=True)
 (p/'periodic-algebra-controls.json').write_text(json.dumps(controls,indent=2));results=[]
 for T in range(1,53):
  rec=solve(a,b,T);results.append(rec);print('TARGET',T,rec['status'],rec['nullity13'],rec['nullity2'],flush=True);(p/'periodic-algebra-target.json').write_text(json.dumps(results,indent=2))
