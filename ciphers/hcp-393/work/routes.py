from pathlib import Path
from math import ceil
import json,heapq
p=Path(__file__).parent
quad={a:float(b) for a,b in (x.split() for x in (p/'quadgrams.tsv').read_text().splitlines())}
def score(s):return sum(quad.get(s[i:i+4],-4.) for i in range(len(s)-3))
def routes(n,w):
 h=ceil(n/w);cells=[(i//w,i%w,i) for i in range(n)];out={}
 def add(name,path):
  t=tuple(i for _,_,i in path)
  if t not in out:out[t]=name
  t=t[::-1]
  if t not in out:out[t]=name+' reversed'
 for flipr in (0,1):
  for flipc in (0,1):
   cv=[(h-1-r if flipr else r,w-1-c if flipc else c,i) for r,c,i in cells]
   for axis in (0,1):
    if axis:cv2=[(c,r,i) for r,c,i in cv]
    else:cv2=cv
    add(f'row-{flipr}{flipc}-axis{axis}',sorted(cv2))
    add(f'snake-{flipr}{flipc}-axis{axis}',sorted(cv2,key=lambda z:(z[0],z[1] if z[0]%2==0 else -z[1])))
    add(f'diagonal-{flipr}{flipc}-axis{axis}',sorted(cv2,key=lambda z:(z[0]+z[1],z[0])))
    add(f'diagonal-snake-{flipr}{flipc}-axis{axis}',sorted(cv2,key=lambda z:(z[0]+z[1],z[0] if (z[0]+z[1])%2 else -z[0])))
   by={(r,c):i for r,c,i in cv};path=[];top,left,bottom,right=0,0,h-1,w-1
   while top<=bottom and left<=right:
    coords=[(top,c) for c in range(left,right+1)];top+=1
    coords += [(r,right) for r in range(top,bottom+1)];right-=1
    if top<=bottom:coords += [(bottom,c) for c in range(right,left-1,-1)];bottom-=1
    if left<=right:coords += [(r,left) for r in range(bottom,top-1,-1)];left+=1
    path += [(r,c,by[r,c]) for r,c in coords if (r,c) in by]
   assert len(path)==n
   add(f'spiral-{flipr}{flipc}',path)
 return out
def attack(s,label,expected=None):
 best=[];tested=0;seen=set();exact=False
 for w in range(2,31):
  rr=routes(len(s),w)
  for R,rname in rr.items():
   inv=[0]*len(s)
   for j,i in enumerate(R):inv[i]=j
   for F,fname in rr.items():
    perm=tuple(inv[i] for i in F)
    if perm in seen:continue
    seen.add(perm);t=''.join(s[i] for i in perm);tested+=1
    if t==expected:exact=True
    row=(score(t),w,fname,rname,t)
    if len(best)<10:heapq.heappush(best,row)
    elif row>best[0]:heapq.heapreplace(best,row)
 report={'label':label,'cases':tested,'expected_seen':exact if expected else None,'best':sorted(best,reverse=True)}
 print(label,tested,report['best'][0],flush=True);return report
plain=Path('ciphers/hcp-334/work/control-vig-plain.txt').read_text().strip()[:100];rr=routes(100,10);F=next(t for t,k in rr.items() if k=='snake-00-axis0');R=next(t for t,k in rr.items() if k=='spiral-00');inv={v:i for i,v in enumerate(F)};control=''.join(plain[inv[i]] for i in R)
report=attack(control,'independent-control',plain)
assert report['expected_seen']
report['planted_plaintext']=plain;report['planted_ciphertext']=control
(p/'routes-control.json').write_text(json.dumps(report,indent=2)+'\n')
ct=''.join(c.lower() for c in (p/'transcription.txt').read_text() if c.isalpha());assert len(ct)==100
allreports=[attack(ct,'full100')]
for omit in range(20):allreports.append(attack(ct[:omit*5]+ct[(omit+1)*5:],f'omit-group-{omit+1}'))
(p/'routes-target.json').write_text(json.dumps(allreports,indent=2)+'\n')
