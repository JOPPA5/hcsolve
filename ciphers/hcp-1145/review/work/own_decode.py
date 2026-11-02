#!/usr/bin/env python3
"""Reviewer's independent decode: rows typed from review crops r01..r20 (not copied from work/transcription.txt).
Signs as seen on the card; key rebuilt below only from hcp-1174's table plus b,f,gy,j,ny.
Then a token-by-token diff against the solver's transcription."""
import re,sys,os
R="""2. 3 1: 7, 8 1. 3, 4, 1 8, 7 1' 8
2. 3, 8, 1: 7, 1 8, 5, 1: 7 5 0 4. 5 1. 2, 1. 7 5, 1:
5 1: 8, 3. 1. 7, 1' 3, 6, 1. 9 4 1: 5, 8 1: 4. :1 6, 7
9 1 7, 8, 1' 3 1. 5, 7. 1: 3, 1: 8, 8, 1: 8 3. 0 5, 6, 1.
5 1. 8 2. 4, 1. 3 3 1 4, 0 8, 5, 1: 8, 3. 0 5, 6, 1. 2. 3 1: 7,
1. 6. 1' 8 6, 1: 8 1 7, 4, 0 6, 3 0 5, 8, 1. 8 5 0 4.
5 1. 9, 1. 6 0, 6 6 0, 6, 5, 1: 4, 1. 5, 1' 1, 1, 6, 1.
4. 0 8, 6, 2. 9, 1: 8, 3. 0 5, 6, 1. 8 1 7 0 3, 1, 1: 8, 0 9
9 1. 6, 8, 1. 8 3. 0 5, 6, 1. 1. 9, 1. 6 8, 0 6, 6, 0 3 1:
1: 9, 8, 8 0 7, 8, 5 1. 3 6 :1 7 8 1. 6 3 7. 0 3 1. 5, 8, 0, 1,
1, 1: 8,
8, 1 8, 7 0 6, 1 3, 0 7 2, 1. 7 5, 1: 3. 1: 5, 1: 8,
8, 1 8, 7 0 6, 7. 1: 3, 1: 8, 5, 1: 7 8, 2. 4, 1: 3 1: 8,
6, 1 6, 2, 1: 6, 6, 1. 4. 0 1, 1, 4. 0, 8, 3, 1: 5, 1: 8
8 1 6, 8, 1. 8, 1 8, 7 0 5, 8, 7. 1: 3, 1: 5, 1: 8
1. 7 1' 3, 1. 5, 3. 1. 1. 7 1' 3, 2. 1, 3, 1: 6,
8 1 6, 3 1 4, 8, 1: 3. 7. 4. 1. 9, 1: 7. 1: 8 1, 1: 6,
7, 0 7 7. 0 3, 0, 5, 1: 5, 3. 1: 2. 7, 2, 0 7 0 5,
3. 1. 8 1. 3, 1. 3 0 7 5 :1 7, 2. 4, 1: 7,
7 1: 3 3. 1: 7, 1: 8 2. 7, 1 8 1' 3 0 3 1' 3 9 1' 3"""
K={}
for g,v in zip("0 0, 1 1. 1: 1' :1 1, 2, 2. 3 3, 3. 4 4, 4. 5 5, 6 6, 6. 7 7, 7. 8 8, 9 9,".split(),
 "o ö i a e á ü b C é d r v f g Y h l j n Ñ k s S m t p z".split()): K[g]=v
mine=' '.join(R.split('\n')).split()
d=os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../work/transcription.txt')
sol=[]
for l in open(d,encoding='utf-8'):
    if l.startswith('#'): continue
    for t in l.replace(';',' ').split():
        if t in '-!).(': continue
        sol.append(t)
print(len(mine),len(sol))
for i,(a,b) in enumerate(zip(mine,sol)):
    if a!=b.split('>')[0]: print('DIFF',i,a,b)
print(''.join(K[t] for t in mine))
from collections import Counter
print(Counter(mine).most_common())
print(sorted(set(K)-set(mine)))
