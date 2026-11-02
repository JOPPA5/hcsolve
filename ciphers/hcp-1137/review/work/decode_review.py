#!/usr/bin/env python3
"""hcp-1137 reviewer: own transcription (typed from review crops, row order of the card), own key,
then token diff against the solver's ROWS in work/decode.py."""
import re,ast,sys
KEY=dict(zip("0 0, 1 1. 1: 1' 1, .1 :1 2, 2. 3 3, 3. 4 4, 4. 5 5, 6 6, 6. 7 7, 7. 8 8, 9 9, 9.".split(),
 "o ö i a e á b u ü cs é d r v f g gy h l j n ny k s sz m t p z zs".split()))
MINE=""" 2. 3 1: 7, 8 1. 3, 4, 1 8, 7 1' 8
7, 1 8, 5, 1: 7 5 0 4. 8 1' 3, 1 8, 8, 3. 1. 4. 0 7 8, 1: 3, 1: 6. 2. 6,
8 2. 4, 3, 0 9, 1' 3. 1. 5, 6, 1: 8 8, 1. 5, 1' 5, 7 0 9, 8, 1. 8
5, 1: 5 1: 8, 5 0 4. 1: 5, 8 1: 4. 1: 7 1. 7. 1: 6, 8,
7 .1 8, 5 0 9, 1 7, 1: 4. 1: 1, .1 6 7, 1' 4, 0 8, 6, 1: 8 8, .1 3 0 7
1 3, 6, 1 7. 1: 3, 3. .1 7.
1: 5, 5 1: 3, 3. 1. 3 1. 3, 0 9. 1 7. 1' 5, 1 7,
5 1. 8 1: 4, 2, 1 9 8, 1: 8 1' 3, 1. 3 2. 3,
1: 5, 5 1: 3, 3. 1. 3 1. 5, 1: 1' 6. 1 7, 5 0 4. 5 1.
6, 1: 8 4 0 3, 1, 1: 6, 6, 1: 8 1' 3, 1. 3. 2. 3,
:1 3 1: 1. 9, 2. 6, 3, 0 9. 1. 7. 1' 5, 1. 8
8 1: 5, 1: 4, 1' 4. 1, 1. 6, 1' 9 0 5, 0 8
4 0 3, 3, 1. 3. 2. 3, 1: 1. 1, 1. 1, 1' 8 6, 1. 7
8 1: 3, 8, 5 1 7. 4. 1. 7 3, 1. 6, 2, 0 7 0 5 0 8
1. 9, 2. 3, 8, 5 0 4. 1: 5, 6 0, 8, 8, 1: 8
7. 1: 3, 1: 7, 7, 2, 1. 7 8, 0 3. 1' 1, 1, 3, 1.
8 1: 3, 8, 8 2. 4, 3. 1 7, 7. 1. 8, 2. 3, 1: 7
1 7, 8 2. 8, 5 0 9, 9, 1' 3 5 1' 6. 7 1.
7. 1' 8, 1. 5, 1. 6, 7. 0 3, 0, 5, 1: 5, 2. 7, 2, 0 7 0 5,
1. 8, 1' 3. 0 5, 1, 0 5,
5 :1 1 8 1' 3 0 3 1' 3, 9 1' 3""".split('\n')
src=open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1137/work/decode.py',encoding='utf8').read()
ROWS=ast.literal_eval(re.search(r'^ROWS = (\[.*?^\])',src,re.S|re.M).group(1))
n=d=0
for i,(m,r) in enumerate(zip(MINE,ROWS),1):
    a=m.split(); b=[t for c,_ in r for t in c.split()]
    print(i,''.join(KEY[t] for t in a))
    n+=len(a)
    if a!=b:
        d+=1; print('   DIFF mine/solver:',[x for x in a if x not in b],[x for x in b if x not in a],len(a),len(b))
print('signs',n,'rows differing',d, 'distinct',len({t for m in MINE for t in m.split()}))
