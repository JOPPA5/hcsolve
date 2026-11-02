# Independent decode of the reviewer's own sign-by-sign reading (typed from review crops, rows as on the card).
import collections
K={'0':'o','1':'i','1.':'a','1:':'e',"1'":'á','.1':'u','1,':'b','2.':'é','3':'d','3,':'r','3.':'v','4,':'g','4.':'gy',
'5':'h','5,':'l','6':'j','6,':'n','7':'k','7,':'s','7.':'sz','8':'m','8,':'t'}
R=["7 1: 3 3. 1: 7, | 8 1. 3, 4, 1 8, 7 1' 8",
"7 1: 3 3, 1: 7, | 8 1. 3, 4, 1 8, 7 1' 8 | 8 1' 3,",
".1 4. | 5, 1' 8, 7. 1 7 | 5 0 4. | 5 1 1' 1, 1. | 7 2. 3,",
"5, 1: 7 | 5 0 4. | 1 3, 6 1' 5, | 8 1' 3, | 6, 1: 8 | 1 3, 7.",
"6, 0 | 2. 6, | 1 3, 0 7 | 8 1 4, | 2. 5, 1: 7 | 5 1 7",
"1: 7 8, | .1 4. 7, 1: 8 | 7, 0 7 1' 1 4, | 1, 1 3, 0 8",
"1: 5, 3. 1 7, 1: 5, 6, 1",
"7. 1: 3, 1: 8, 6, 1"]
c=collections.Counter()
for r in R:
    o=[]
    for w in r.split('|'):
        t=w.split(); c.update(t); o.append(''.join(K[x] for x in t))
    print(' '.join(o))
print('signs',sum(c.values()),'distinct',len(c), 'unused key', set(K)-set(c))
print(sorted(c.items(),key=lambda x:-x[1]))
