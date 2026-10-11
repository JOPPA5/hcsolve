from pathlib import Path
import json
p=Path(__file__).resolve().parent
g395=(p/'transcription.txt').read_text().split()
# Independently transcribed396groups disclosed in that cipher's notes; only395files are written.
g396='vepes nmono drtsi uzoip ujpta sztra cscnu dwjpm ciasi ujiui oormt'.split()
def code(n):return ''.join(str((n+j)%10) for j in range(5)) if n<10 else str(n)+'0'+str(n+1)
def possible(a,n,b,m):
 mapping={}
 for s,num in ((a,n),(b,m)):
  for c,d in zip(s,code(num)):
   if c in mapping and mapping[c]!=d:return False
   mapping[c]=d
 return all(list(mapping.values()).count(d)<=3 for d in set(mapping.values()))
assert possible('defgh',3,'jabcd',9)
assert not possible('defgh',3,'dehij',4)
out=[]
for reading in ('c','o'):
 gs=g396.copy();gs[6]=reading+gs[6][1:]
 for pos in range(11):
  pairs=[(a,b)for a in range(1,23)for b in range(1,23)if possible(g395[pos],a,gs[pos],b)]
  out.append(dict(reading396=reading,position=pos+1,group395=g395[pos],group396=gs[pos],possible_pairs=pairs))
(p/'joint-indicator-constraints.json').write_text(json.dumps(out,indent=2))
for r in out:print(r['reading396'],r['position'],len(r['possible_pairs']),r['possible_pairs'] if len(r['possible_pairs'])<20 else '')
