import time,json,sys
def solve_isomorph(msgs,width):
 import itertools
 start=time.time();n=26+len(msgs)-1;A=[]
 for r in range(1,len(msgs)):
  for i in range(width):
   row=[0]*n;row[ord(msgs[r][i])-97]+=1;row[ord(msgs[0][i])-97]-=1;row[25+r]-=1;A.append(row)
 row=[0]*n;row[0]=1;A.append(row)
 def nullspace(prime):
  B=[[x%prime for x in row]for row in A];piv=[];k=0
  for col in range(n):
   at=next((r for r in range(k,len(B))if B[r][col]),None)
   if at is None:continue
   B[k],B[at]=B[at],B[k];scale=pow(B[k][col],-1,prime);B[k]=[(x*scale)%prime for x in B[k]]
   for r in range(len(B)):
    if r!=k and B[r][col]:
     v=B[r][col];B[r]=[(x-v*y)%prime for x,y in zip(B[r],B[k])]
   piv.append(col);k+=1
  basis=[]
  for col in range(n):
   if col in piv:continue
   v=[0]*n;v[col]=1
   for r,c in enumerate(piv):v[c]=-B[r][col]%prime
   basis.append(v)
  return basis
 bases={q:nullspace(q)for q in [2,13]};solutions={};dims={q:len(bases[q])for q in bases}
 for r in range(1,len(msgs)):
  pairs=list(zip(msgs[0][:width],msgs[r][:width]));forward={};back={}
  for x,y in pairs:
   if (x in forward and forward[x]!=y)or(y in back and back[y]!=x):
    return dict(rings=[],status=['inconsistent partial substitution'],elapsed=time.time()-start,width=width,nullity=dims)
   forward[x]=y;back[y]=x
  if any(x==y for x,y in pairs)and any(x!=y for x,y in pairs):
   return dict(rings=[],status=['zero shift forces unequal cipher letters to collide'],elapsed=time.time()-start,width=width,nullity=dims)

 if max(dims.values())>3:return dict(rings=[],status=['underconstrained enumeration not attempted'],elapsed=time.time()-start,width=width,nullity=dims)
 for q,basis in bases.items():
  vals=[]
  for coef in itertools.product(range(q),repeat=len(basis)):
   v=[sum(c*b[i]for c,b in zip(coef,basis))%q for i in range(n)]
   # A 26-place ring has 13 residues of each parity and 2 of each mod-13 residue.
   if all(v[:26].count(t)==26//q for t in range(q)):vals.append(v)
  solutions[q]=vals
 result=[]
 for a in solutions[2]:
  for b in solutions[13]:
   v=[(y+13*((x-y)%2))%26 for x,y in zip(a,b)]
   if len(set(v[:26]))==26:result.append(v[:26])
 return dict(rings=result,status=['exhaustive finite-field enumeration'],elapsed=time.time()-start,width=width,nullity=dims,residue_solutions={q:len(solutions[q])for q in solutions})

if __name__=='__main__':
 from pathlib import Path
 messages=json.loads(Path(sys.argv[1]).read_text())
 print(json.dumps(solve_isomorph(messages,int(sys.argv[2])),indent=2))
