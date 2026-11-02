#!/usr/bin/env python3
# Reviewer's independent decode: rows typed from review/work/crops, no word division;
# greedy table built from the FINAL card hcp-1174 plus four sister signs, listed separately.
import re, sys
ROWS = """7 1: 3 3. 1: 7, 8 1. 3, 4, 1 8, 7 1' 8
7 1: 3 3. 1: 7,
8 1. 3, 4, 1 8, 7 1' 8 6, 1: 8 5 1 7. 1: 8
5 0 4. 6, 1: 8 5 1. 3, 1. 4, .1 3 6, 1' 5, 6, 1:
1 7, 8, 1. 4, 1. 3 8 1: 3. 8, 8, 1: 4, 6, 1. 9 2. 7.
3, 1: 3. 1: 8, 8, 1: 8 1. 7. 8, 9 1: 3 1 4, 1: 5,
7, 1: 7 2. 9 9, 1: 5, 1: 3 5 0 4. 4 1' 6 1: 9,
6, 1: 7 1: 8""".split('\n')
T = dict(zip("0 1 1. 1: 1' 2. 3 3, 3. 4, 5 5, 6, 7 7, 7. 8 8, 9 9,".split(),
             "o i a e á é d r v g h l n k s sz m t p z".split()))
S = {'4.':'gy','.1':'u','4':'f','6':'j'}
for r in ROWS: print(''.join({**T,**S}[t] for t in r.split()))
tok=[t for r in ROWS for t in r.split()]
print(len(tok),'signs',len(set(tok)),'distinct; FINAL table',sum(t in T for t in tok),'sister',sum(t in S for t in tok))
sol=[]
for l in open(sys.argv[1],encoding='utf-8'):
    if l[0]!='#': sol+= [('3.' if t=='3.r' else t) for t in l.split() if t not in '|!-']
print('token streams identical to solver (3.r taken as written):', sol==tok)
