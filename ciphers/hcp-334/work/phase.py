from pathlib import Path
from collections import Counter
import random,json
p=Path(__file__).parent
groups=(p/'transcription.txt').read_text().split()
s=''.join(groups).lower()
assert len(groups)==30 and len(s)==150 and s.count('?')==2
print('30 visible group tokens; hypothesis150positions;148read letters;2erasures')
def ic(x):
 c=Counter(c for c in x if c!='?');n=sum(c.values());return sum(v*(v-1) for v in c.values())/(n*(n-1)) if n>1 else 0
def pooled(x,period):
 num=den=0
 for off in range(period):
  c=Counter(z for z in x[off::period] if z!='?');n=sum(c.values());num+=sum(v*(v-1) for v in c.values());den+=n*(n-1)
 return num/den if den else 0
variants=[]
for off in range(5):
 g=groups.copy();g[18]='FWXX'[:off]+'?'+'FWXX'[off:];variants.append(''.join(g).lower())
scores=sorted([(pooled(x,w),off,w) for off,x in enumerate(variants) for w in range(2,21)],reverse=True)
print('Top pooled column IC; FWXX insertion offset0..4,period:',scores[:10])
rng=random.Random(334);known=[c for c in s if c!='?'];exceeds=0;trials=1000
for trial in range(trials):
 rng.shuffle(known);it=iter(known);rand=''.join('?' if c=='?' else next(it) for c in s)
 # Five insertion-position variants move the hypothetical missing position
 # within the same group, preserving known-letter order.
 rvariants=[rand[:90]+rand[90:94][:i]+'?'+rand[90:94][i:]+rand[95:] for i in range(5)]
 best=max(pooled(x,w) for x in rvariants for w in range(2,21))
 exceeds+=best>=scores[0][0]
print('Conditional random-order max-statistic check:',exceeds,'/',trials,'at least observed; add-one p=',(exceeds+1)/(trials+1))
