#!/usr/bin/env python3
"""Independent decode of hcp-1156: signs retyped by the reviewer from own crops, key from
hcp-1174/1178/1179 SOLUTION tables plus the three card-specific values under test."""
S = """7 1: 3 3. 1: 7, / 1 4, 1. 9, 7. 1 3. :1 / 8 1. 3, 4, 1 8, 7 1' 8
1 3, 5 1. 8, 7. / 1. 7 1. 3, 8 1 8, / 6, 1: / 4 2. 5, 6
:1 4. 7, 1: | 8 1: 4, / 7, 1: 6, 7 1 / 5 1.
1, 1: 8, :1 3. 1: 5, / 6, 1: 8 / 1. 7 7 0 3, / 1 3, 6 1. 5,
? 1. 8 0 7 7 1. 5, / 1, 1 9, 5 1. 8, 7. / 1, 1: 6, 6, 1: 8
8, 1: 7, 8, 3. 2. 3, / 2. 6, / :1 4. / 1, 1 9, 0 7
1, 1: 6, 6, 1: 3 / 8 1 6, 8, / 1. / 6 0 / 1 7, 8, 1: 6, 7 2. 1, 1: 6,
5 :1 / 7 1: 3 3. 1: 7, 1: 3 / 1' 3, 9 1' 3"""
K = dict(zip("0 1 1. 1: 1' :1 1, 2. 3 3, 3. 4 4, 4. 5 5, 6 6, 7 7, 7. 8 8, 9 9,".split(),
 "o i a e á ü b é d r v f g gy h l j n k s sz m t p z".split()))
from collections import Counter
n=Counter()
for line in S.splitlines():
    out=[]
    for tok in line.split():
        if tok in '/|': out.append(' ' if tok=='/' else ' <lássa> ')
        else:
            n[tok]+=1; out.append(K.get(tok,'?'))
    print(''.join(out))
print(sum(n.values()),'signs',len(n),'distinct',n)
