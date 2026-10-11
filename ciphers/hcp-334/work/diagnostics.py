from pathlib import Path
from collections import Counter,defaultdict
p=Path(__file__).parent
s=''.join(c.lower() for c in (p/'transcription.txt').read_text() if c.isalpha())
def ic(t):
 c=Counter(t); n=len(t)
 return sum(v*(v-1) for v in c.values())/(n*(n-1)) if n>1 else 0
print('N',len(s),'visible_letters_only_no_gap_phase','IC',ic(s),'uniform alphabet26 expected',1/26)
print('Period / mean column IC / matching letters at shift')
for w in range(1,41): print(w,round(sum(ic(s[i::w]) for i in range(w))/w,5),sum(a==b for a,b in zip(s,s[w:])))
rep=defaultdict(list)
for i in range(len(s)-2):rep[s[i:i+3]].append(i)
print('Repeated trigrams zero-based:',{k:v for k,v in rep.items() if len(v)>1})
