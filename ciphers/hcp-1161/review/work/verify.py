#!/usr/bin/env python3
"""Reviewer's independent decode of hcp-1161. Tokens typed from my own enlarged crops, row by row.
Marks as seen: '?b' = blot where a mark should be."""
import re, sys
KEY={'0':'o','0,':'ö','1':'i','1.':'a','1:':'e',"1'":'á','.1':'u','-1':'ú','1,':'b','2,':'cs','2.':'é','3':'d','3,':'r','3.':'v',
'4,':'g','4.':'gy','5':'h','5,':'l','6,':'n','6.':'ny','7':'k','7,':'s','7.':'sz','8':'m','8,':'t','9':'p','9,':'z'}
ROWS=["7 1: 3 3. 1: 7, / 8 1' 3, 4, 1 8, 7 1' 8",
"2. 6, / 1. 7. 8, / 7, 1: 8","8, .1 3 0 8 / 5 0 4. / 8 1 8, / 1 3, 8, 1. 8",
"1. 7 7 0 3, / -1 4. / 1: 5, / 3?b 0 5, 8, 1. 8","7 1' 1, .1 5, 3. 1. / 6, 0",
"8, 1: 6, 6, 2. 8 / 2. 3, 8, 1: 3 / 5 1.","5 1 3 1: 4, 1: 6, / 1: 5, .1 8, 1. 7, 1 8, 1.","6, 1' 5,",
"1: 5, 3. 1 7, 1: 5, 6, 1","5 1 7. / 1 4, / 7, 1 6, 2, / 7, 1: 6, 7 1","5 1' 8, / -1 4?b / 8 1: 4, / 7 1 / 3. 0 5, 6, 1.",
"5 1. / 8, 1: / 7, 1: / 3. 0 5, 6, 1' 5, / 8 1' 3,","8 0 7, 8, / 1 7, / 2. 3 1: 7, / 1. 6. 1' 8 / 1 7,",
"8 1: 4, / 3, 0 9, 1. / 1 7, / 1 3, 8, 1. 7 / 8 1' 7,","6, 1. 7",
"7. 1' 8 8, 1. 5, 1. 6, 7. 0 3, / 0, 5, 1: 5, 5, 1: 7","2. 7, / 2, 0 7 0 5, 5, 1. 7 / 1' 3, 9, 1' 3"]
out=[]
for r in ROWS:
    o=[]
    for w in r.split(' / '):
        o.append(''.join(KEY.get(t,'['+t+']') for t in w.split()))
    out.append(' '.join(o)); print(out[-1])
n=sum(len(w.split()) for r in ROWS for w in r.split(' / '))
print('signs',n)
# compare with solver's token list, parsed as text (not executed)
s=open('work/decode.py',encoding='utf8').read()
sol=[a for a,_ in re.findall(r'\("([^"]+)", \'([^\']+)\'\)',s)]
mine=' '.join(r.replace(' / ',' ') for r in ROWS).split()
ss=' '.join(sol).split()
print('solver signs',len(ss))
norm={"1'~low":"1'","4,~gy":"4,","4blot":"4?b","3blot":"3?b","9,~p":"9,"}
ss=[norm.get(t,t) for t in ss]
# my rows: másnak split over the line break, joined here for count only
print('diff positions',[(i,a,b) for i,(a,b) in enumerate(zip(mine,ss)) if a!=b])
print('unused keys',sorted(set(KEY)-set(mine)))
