from pathlib import Path
import json
p=Path(__file__).resolve().parent
q={}
for line in (p/'quadgrams.tsv').read_text().splitlines():g,v=line.split();q[g]=float(v)
def score(s):return sum(q.get(s[i:i+4],-4) for i in range(len(s)-3))
def railseq(n,r,offset):
 period=2*r-2
 return [min((i+offset)%period,period-(i+offset)%period) for i in range(n)]
def decrypt(ct,r,offset,revrails,reverse):
 if reverse:ct=ct[::-1]
 rs=railseq(len(ct),r,offset);order=list(range(r));order=order[::-1] if revrails else order
 cols={};at=0
 for j in order:count=rs.count(j);cols[j]=iter(ct[at:at+count]);at+=count
 return ''.join(next(cols[j]) for j in rs)
control='ministerstvooznamujezevasuspravusmednesdostaliprosimza'
rs=railseq(len(control),7,3);ct=''.join(c for rail in range(7) for c,r in zip(control,rs) if r==rail)
assert decrypt(ct,7,3,False,False)==control
out=[];groups=(p/'transcription.txt').read_text().split()
for reading in ('c','o'):
 gs=groups.copy();gs[6]=reading+gs[6][1:]
 for omit in range(-1,11):
  ct=''.join(g for i,g in enumerate(gs) if i!=omit);best=[]
  for rails in range(2,len(ct)):
   for offset in range(2*rails-2):
    for rr in (False,True):
     for rev in (False,True):
      plain=decrypt(ct,rails,offset,rr,rev);best.append((score(plain),rails,offset,rr,rev,plain))
  best.sort(reverse=True);out.append(dict(reading=reading,omit=omit,tests=len(best),best=best[:5]))
(p/'railfence-results.json').write_text(json.dumps(dict(control_exact=True,scenarios=out),indent=2));print('Railfence control exact; target tests',sum(r['tests'] for r in out))
