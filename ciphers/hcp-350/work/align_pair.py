from pathlib import Path
from difflib import SequenceMatcher
from collections import Counter
p=Path(__file__).parent
x=p.joinpath('cipher.txt').read_text();y=''.join((p.parents[1]/'hcp-351/work/transcription.txt').read_text().lower().split())
print('Difflib longest exact blocks')
for b in SequenceMatcher(None,x,y,autojunk=False).get_matching_blocks():
 if b.size>=3:print(b,x[b.a:b.a+b.size])
print('Shared exact5letter groups and positions1based')
gx=[x[i:i+5] for i in range(0,len(x),5)];gy=[y[i:i+5] for i in range(0,len(y),5)]
for i,g in enumerate(gx):
 for j,h in enumerate(gy):
  if g==h:print(i+1,j+1,g)
print('Interior offsets -20..20: offset, matches, overlap, rate')
for d in range(-20,21):
 pairs=[(x[i],y[i+d]) for i in range(20,375) if 20<=i+d<375]
 c=sum(a==b for a,b in pairs);print(d,c,len(pairs),round(c/len(pairs),4))
# Exact Levenshtein substitution/insertion/deletion unit costs.
def align(x,y):
 n=len(x);m=len(y);d=[[0]*(m+1) for _ in range(n+1)]
 for i in range(n+1):d[i][0]=i
 for j in range(m+1):d[0][j]=j
 for i in range(1,n+1):
  for j in range(1,m+1):d[i][j]=min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+(x[i-1]!=y[j-1]))
 i=n;j=m;ax=[];ay=[];ops=Counter()
 while i or j:
  if i and j and d[i][j]==d[i-1][j-1]+(x[i-1]!=y[j-1]):
   ax.append(x[i-1]);ay.append(y[j-1]);ops['equal' if x[i-1]==y[j-1] else 'substitution']+=1;i-=1;j-=1
  elif i and d[i][j]==d[i-1][j]+1:ax.append(x[i-1]);ay.append('-');ops['deletion']+=1;i-=1
  else:ax.append('-');ay.append(y[j-1]);ops['insertion']+=1;j-=1
 return d[n][m],ops,''.join(ax[::-1]),''.join(ay[::-1])
for label,a,b in [('full',x,y),('interior',x[20:375],y[20:375])]:
 dist,ops,ax,ay=align(a,b);print('LEVENSHTEIN',label,dist,dict(ops))
 for i in range(0,len(ax),100):print(ax[i:i+100]);print(ay[i:i+100]);print()
print('A small insertion/deletion repair would yield nearfull matches and small distance; neither observed.')
