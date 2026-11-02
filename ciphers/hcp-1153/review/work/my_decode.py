#!/usr/bin/env python3
"""Reviewer's own decoder: separately typed transcription from review crops (not read from work/transcription.txt).
Table is keyed by digit -> mark, hcp-1174 values plus this card's extra signs. Run from ciphers/hcp-1153."""
import re
T={'0':{'':'o',',':'ö'},'1':{'':'i',',':'b','.':'a',':':'e','°':'á'},'2':{',':'cs','.':'é'},'3':{'':'d',',':'r','.':'v'},
   '4':{',':'g','.':'gy'},'5':{'':'h',',':'l','.':'ly'},'6':{'':'j',',':'n','.':'ny'},'7':{'':'k',',':'s','.':'sz'},
   '8':{'':'m',',':'t'},'9':{'':'p',',':'z'}}
PRE={'.1':'u',':1':'ü'}
MY='''2. 3 1: 7, 8 1. 3, 4, 1 8, 7 1. 8
2. 3, 8, 1: 7, 1 8, 5, 1: 7 5 0 4. 7. 1: 3, 1: 6, 2, 2. 7, 1: 6, 5, 1: 2. 3,
8, 1: 8 8 0 7, 8, 9 1: 3 1 4, 1 8, 8, 3. 1. 4. 0 7 1. 9, 1. 5, 5, 0
8 1. 7, 0 6, 3. 1. 3, 0 8 1. 3. 0 6, 1. 8, 0 8, 1. 3. 0 6, 1. 8, 8 2. 4,
7, 0 7 1. 6 0, 6, 8, 1: 5 1. 8, 3, 1. 2. 3, 1: 7 1 3, 6, 1 3 3, 1. 4, 1.
8 1. 3, 4, 1 8, 7 1. 8 1 8, 8, 5, 1. 8, 0 7
7, 1 3, 0 1. 7, 7. 0 6. 0 7 1. 8, 1. 8 1 6, 8,
3. 1. 5, 6, 1. 7 1: 5, 1. 9, 0, 3. 2. 1 7
8, 0, 5, 2. 7, 8 0 7, 8, 2. 6, 1 7, 1 7. 0
6. 0 3 3. 1. 4, 0 6, 3 0 5, 0 7 1. 9, 1: 5,
3. 1. 5, 1. 7, 3, 1. 8 1: 3, 8, 8 2. 4, 5 1
8 1. 7, 8, 5, 1. 8, 1 7, 1. 9, 1: 8 1, 1: 3, 8 2. 4,
1. 9, 1 7, 7 0, 6, 6. 1: 8, 2, 1. 5, 1. 7. 1: 8 2. 1, 1:
5, 1° 6. 7 1.
6 .1 8, 7. 2. 6, 6, 2. 7 1: 8
0 5. 7. 1: 3, 2. 6. 3. 1. 4. 8, 1: 2. 9 1: 6,
2. 7, 0 5. 7. 2. 9 1 7, 2. 3 1: 7, 1: 8
8 0 7, 8, 9 1: 3 1 4, 7. 1. 8, 1. 5, 1. 6, 7. 0 3,
0, 5, 1: 5, 2. 7, 2, 0 7 0 5, 5 :1
1 8 1. 3 0 3 1. 3, 9 1. 3'''.split('\n')
def dec(t):
    if t in PRE: return PRE[t]
    return T[t[0]][t[1:]]
mine=[l.split() for l in MY]
sol=[]
for l in open('work/transcription.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    b=re.sub(r'\{[^}]*\}','',l.split(': ',1)[1])
    sol.append([x.rstrip('?') for x in b.split() if x not in (')','!')])
assert len(mine)==len(sol)
n=sum(map(len,mine)); print('signs',n)
for i,(a,b) in enumerate(zip(mine,sol)):
    assert len(a)==len(b),i
    for j,(x,y) in enumerate(zip(a,b)):
        if x!=y: print('row',i,'pos',j,'mine',x,dec(x),'solver',y,dec(y))
    print(''.join(dec(t) for t in a))
print('distinct signs',len({t for r in mine for t in r}))
