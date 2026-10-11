from pathlib import Path
import math,sys,json
p=Path(__file__).resolve().parent
words={}
for l in (p/'words-pos.tsv').read_text().splitlines():
 w,f,mask=l.split();words[w]=(int(f),int(mask))
tr={(int(a),int(b)):float(c) for a,b,c in (l.split() for l in (p/'pos-transitions.tsv').read_text().splitlines())}
for s in sys.argv[1:]:
 dp={(0,8):0};back={};n=len(s)
 for i in range(n):
  for t in range(9):
   val=dp.get((i,t),-1e9)
   if val-3>dp.get((i+1,t),-1e9):dp[i+1,t]=val-3;back[i+1,t]=((i,t),'?'+s[i])
   for j in range(i+2,min(i+25,n)+1):
    w=s[i:j]
    if w not in words:continue
    f,mask=words[w];reward=1.2*len(w)-5+min(4,math.log(1+f))
    for nt in range(8):
     if mask&(1<<nt):
      v=val+tr[t,nt]+reward
      if v>dp.get((j,nt),-1e9):dp[j,nt]=v;back[j,nt]=((i,t),w)
 end=max(((dp.get((n,t),-1e9)+tr[t,9],(n,t)) for t in range(9)))
 chain=[];at=end[1]
 while at in back:at,w=back[at];chain.append(w)
 print(end[0],' '.join(chain[::-1]))
