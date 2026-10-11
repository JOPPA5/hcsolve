from pathlib import Path
from collections import defaultdict
import sys,json,random,math
p=Path(__file__).resolve().parent
ct=Path(sys.argv[1]).read_text().strip()
def pat(s):
 d={};return tuple(d.setdefault(c,len(d)) for c in s)
index=defaultdict(list)
for l in (p/'words.tsv').read_text().splitlines():
 w,f=l.split('\t');f=int(f)
 if 8<=len(w)<=15:index[pat(w)].append((w,f))
seeds=[];stats=[]
for n in range(15,7,-1):
 for off in range(len(ct)-n+1):
  span=ct[off:off+n];matches=index[pat(span)]
  if not matches:continue
  stats.append({'offset':off,'length':n,'matches':len(matches)})
  for w,f in matches:
   k={ord(c)-97:ord(a)-97 for c,a in zip(span,w)}
   # Candidate priority is generic length/word frequency, independent of crib.
   rank=n*n+5*math.log(1+f)
   seeds.append((rank,off,w,k))
seeds.sort(key=lambda s:(-s[0],s[1],s[2]))
r=random.Random(610333)
out=[]
for _,off,w,k in seeds[:2000]:
 avail=list(set(range(26))-set(k.values()));r.shuffle(avail)
 key=[k.get(i,-1) for i in range(26)]
 for i in range(26):
  if key[i]<0:key[i]=avail.pop()
 out.append(''.join(chr(97+x) for x in key))
prefix=Path(sys.argv[2]);prefix.with_suffix('.txt').write_text('\n'.join(out)+'\n');prefix.with_suffix('.json').write_text(json.dumps({'seeds_total':len(seeds),'written':len(out),'windows':stats,'first_candidates':[{'offset':off,'word':w} for _,off,w,_ in seeds[:30]]},indent=2)+'\n')
print('total matching seeds',len(seeds),'selected',len(out),'by lengths',{n:sum(x['matches'] for x in stats if x['length']==n) for n in range(8,16)})
