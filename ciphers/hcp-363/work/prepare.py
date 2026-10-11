from pathlib import Path
from collections import Counter
p=Path(__file__).parent;g=p.joinpath('transcription-raw.txt').read_text().split();s=''.join(g).lower()
print('Groups',len(g),'symbols',len(s),'non5groups',[(i+1,v) for i,v in enumerate(g) if len(v)!=5]);print('raw counts',dict(sorted(Counter(s).items())))
# Explicit hypothesis only: telegraphic4->A,8->B,obscuredlastglyphUIDA?->X orA.
for unknown in ['x','a']:
 t=s.replace('4','a').replace('8','b').replace('?',unknown);p.joinpath('cipher-'+unknown+'.txt').write_text(t)
 c=Counter(t);print('variant',unknown,'IC',sum(v*(v-1) for v in c.values())/(len(t)*(len(t)-1)))
p.joinpath('cipher.txt').write_text(p.joinpath('cipher-x.txt').read_text())
