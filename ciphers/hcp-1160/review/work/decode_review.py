#!/usr/bin/env python3
"""Reviewer's independent decode of hcp-1160. Ciphertext retyped from the reviewer's own crops (review/work/r*.png, v.png),
as one string per card row, no word division. Key rebuilt from the sister-card tables, grouped by digit."""
import re, os, sys
ROWS = [
"7 1: 3 3. 1: 7, 8 1. 3, 4, 1 8, 7 1' 8",
"1. 5, 1. 9 0 3 1. 8, 8 1: 4, 7 1. 9 8, 1. 8 8 1: 5.",
"6, 1: 7 6, 1. 4. 0 6, 8 1: 4, 0, 3, :1 5, 8, 1: 8",
"7 1: 3 3. 1: 7, 8 1. 3, 4, 1 8, 7 1' 8 8, .1 3 5 1.",
"8, 0 3 5 0 4. 5 1. 2, 1. 7 5, 1: 5 1: 8, 4 1: 5,",
"8 1: 4. 1: 7 3 1: 5 1. 6, 1. 4. 0 6, 3, 0 7.",
":1 3 0, 5, 1: 7. 6, 1: 8 8 1: 5 1: 8, 1: 7",
"1: 5, 5 1: 3, 3. 1. 3 0 7 9 0 3, 1, 1. 5 .1 5, 5, 0 7",
"8 1 6, 8, 3, 0 9. 1' 3, 0 5, 1. 7. 1 3, 0 8",
"6, 1: 8 1: 6 8, 7 0, 6, 6? 1: 8, 7, 1: 6, 7 1 2. 3, 8, 1: 8",
"9 .1 7. 8, 1' 6, 1' 5, 5, 8 1. 6 3 1. 7, 1 3, 0 8",
"1. 9, 1: 3, 3 1: 1 7 1 7, 3 1. 5, 0 7, 0 7",
"9, 1: 6, 4, 1 7 1: 5, 5 1. 8, 8. .1 3 1. 5, 0 8",
"1: 4. 1, 0 5 0 7. 1: 4, 2. 6. 4 1 .1 3. 1. 5,",
"7 1: 3. 1: 7, 1: 1, 1, 5, 1: 7. 8 0 6, 3 5 1. 8, 0 8",
"1, 0 2, 1' 7, 8 1: 4,",
"7. 1' 8 8, 1. 5, 1. 6, 7. 0 3, 2, 0 7 0 5, 5, 1. 7",
"1. 4 2. 6. 7 2. 9 7 2. 7. 1: 3. 1. 6,",
"9 2. 6, 7. 8, 7 :1 5, 4. 2. 5, 5, 1:",
"8 1. 6 3 7 1 3. 1' 5, 8, 0 8 2. 7,",
"4 1: 3. 1 7. 1: 8",
]
K = {}
for d, plain in {'0':'o','1':'i','2':'?','3':'d','4':'f','5':'h','6':'j','7':'k','8':'m','9':'p'}.items(): K[d]=plain
K.update({'0,':'ö','1.':'a','1:':'e',"1'":'á',':1':'ü','.1':'u','1,':'b','2,':'cs','2.':'é','3,':'r','3.':'v',
 '4,':'g','4.':'gy','5,':'l','5.':'ly','6,':'n','6.':'ny','7,':'s','7.':'sz','8,':'t','8.':'ty','9,':'z','9.':'zs','6?':'[ny|n]'})
n=0; used=set()
for r in ROWS:
    t=r.split(); n+=len(t); used|=set(t)
    print(''.join(K[x] for x in t))
print('signs',n,'distinct',len(used))
# compare with the solver's tokens
D=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sol=[]
for l in open(os.path.join(D,'work/transcription.txt'),encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    sol+= [x for x in l.split('\t')[1].split() if x!='|']
mine=[x for r in ROWS for x in r.split()]
print('solver tokens',len(sol))
import difflib
for op,a,b,c,d in difflib.SequenceMatcher(None,sol,mine,autojunk=False).get_opcodes():
    if op!='equal': print(op,a,sol[max(a-2,0):b+2],'->',mine[max(c-2,0):d+2])
