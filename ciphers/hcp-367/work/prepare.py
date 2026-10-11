from pathlib import Path
from collections import Counter
import json
p=Path(__file__).parent;s=''.join((p/'analysis-reading.txt').read_text().split());assert len(s)==85
q={a:float(b) for a,b in (l.split() for l in (p/'quadgrams.tsv').read_text().splitlines())}
def score(t):return sum(q.get(t[i:i+4],-4) for i in range(len(t)-3))
def stats(s):
 c=Counter(s);n=len(s);return {'n':n,'counts':dict(sorted(c.items())),'IC':sum(v*(v-1) for v in c.values())/(n*(n-1))}
def code(n):return [(n+i)%10 for i in range(5)] if n<10 else list(map(int,str(n)+'0'+str(n+1)))
def consistent(g,n):
 d={}
 for c,x in zip(g,code(n)):
  if c in d and d[c]!=x:return False
  d[c]=x
 return all(list(d.values()).count(x)<=3 for x in range(10))
results={}
for name,g in [('full',0),('drop1',1),('drop7',7)]:
 t=s if not g else s[:5*(g-1)]+s[5*g:]
 (p/f'cipher-{name}.txt').write_text(t+'\n');results[name]=stats(t)
routes=[]
for omit in range(-1,17):
 t=s if omit<0 else s[:5*omit]+s[5*omit+5:]
 for w in range(2,len(t)):
  for rev in [False,True]:
   z=t[::-1] if rev else t;out=''.join(z[i::w] for i in range(w));routes.append([score(out),omit+1,w,rev,out])
out={'warning':'Assumed reading XAETN; question marks in diplomatic transcription are not recovered letters.','stats':results,'indicator_encoding_candidates':[{'group':i+1,'text':g,'possible_n':[n for n in range(1,23) if consistent(g,n)]} for i,g in enumerate((p/'analysis-reading.txt').read_text().split())],'route_count':len(routes),'best_routes':sorted(routes,reverse=True)[:20]}
(p/'baseline.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(results))
