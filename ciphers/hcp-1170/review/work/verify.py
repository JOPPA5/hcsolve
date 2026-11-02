# Reviewer's independent decode. Rows below were keyed from review/work/r*.png, not copied from work/transcription.txt.
K={'0':'o','0,':'ö','1':'i','1.':'a','1:':'e',"1'":'á',':1':'ü','2.':'é','3':'d','3,':'r','3.':'v','4,':'g',
   '4.':'gy','5':'h','5,':'l','6':'j','6,':'n','6.':'ny','7':'k','7,':'s','7.':'sz','8':'m','8,':'t','9,':'z','.1':'u'}
R="""3 3, 1' 4, 1. 8 1. 3, 4, 1 8, 7 1' 8
:1 3 3. 0, 9, 0, 5, 5, 1: 7 2. 7,
8, 2. 4, 1: 3 2. 7, 8 1 6, 3 6. 1' 6 1.
8, 0 7 1. 8, 8 1 .1 6 7, 1' 4, 3. 1. 6,
0 8, 2. 7, 5 0 4. 3. 1. 4. 8, 0 7 3, 0 7.
:1 3 0, 3. 1. 6, 1: 0 8,""".splitlines()
from collections import Counter
n=Counter()
for r in R:
    t=r.split(); n.update(t); print(''.join(K[x] for x in t))
print(sum(n.values()),len(n)); print(sorted(n.items(),key=lambda x:x[1]))
