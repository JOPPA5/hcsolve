from pathlib import Path
from collections import Counter
import json, math
p=Path(__file__).parent
s=''.join((p/'transcription.txt').read_text().split())
assert len(s)==85
(p/'cipher-group6.txt').write_text(s[:25]+s[30:]+'\n');(p/'cipher-full.txt').write_text(s+'\n');(p/'cipher.txt').write_text(s[:10]+s[15:]+'\n')
q={a:float(b) for a,b in (l.split() for l in (p/'quadgrams.tsv').read_text().splitlines())}
def score(t): return sum(q.get(t[i:i+4],-4) for i in range(len(t)-3))
def stats(t):
 c=Counter(t);n=len(t);return {'n':n,'counts':dict(sorted(c.items())),'IC':sum(v*(v-1) for v in c.values())/(n*(n-1))}
routes=[]
for omit in range(-1,17):
 t=s if omit<0 else s[:5*omit]+s[5*omit+5:]
 for w in range(2,len(t)):
  for rev in [False,True]:
   x=t[::-1] if rev else t
   v=''.join(x[j::w] for j in range(w))
   routes.append((score(v),omit+1,w,rev,v))
caesars=[]
for reverse in [False,True]:
 for sign in [1,-1]:
  for shift in range(26):
   t=s[::-1] if reverse else s
   x=''.join(chr(97+(sign*(ord(c)-97)+shift)%26) for c in t)
   caesars.append((score(x),reverse,sign,shift,x))
out={'full':stats(s),'without_group3':stats(s[:10]+s[15:]),'without_group6':stats(s[:25]+s[30:]),'route_tests':len(routes),'best_routes':sorted(routes,reverse=True)[:20],'caesar_affine_sign_controls':len(caesars),'best_caesars':sorted(caesars,reverse=True)[:10]}
(p/'baseline.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if not k.startswith('best')},indent=2))
