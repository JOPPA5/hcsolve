from pathlib import Path
from collections import Counter
import math
p=Path(__file__).parent
s=''.join(c for c in (p/'transcription.txt').read_text() if c.isalpha())
n=len(s); c=Counter(s)
print('N',n,'IC',sum(x*(x-1) for x in c.values())/(n*(n-1)))
print(c)
for w in range(2,50):
 if n%w==0:
  for rev in [False,True]:
   x=s[::-1] if rev else s
   print('transpose',w,'reverse',rev, ''.join(x[i::w] for i in range(w)))
