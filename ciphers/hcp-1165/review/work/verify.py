#!/usr/bin/env python3
"""Reviewer's independent decode of hcp-1165: own row-by-row transcription, own key
(digit+mark -> letter), compared with the solver's printed cipher words.
Marks: ',' '.' ':' "'" after the digit; '.1' and ':1' are the left-dot signs.
'?' suffix = sign read by word sense (no clean table value)."""
import subprocess, re, sys, unicodedata
KEY = {'0':'o','0,':'ö','1':'i','1,':'b','1.':'a','1:':'e',"1'":'á','.1':'u',':1':'ü',
 '2,':'cs','2.':'é','3':'d','3,':'r','3.':'v','4':'f','4,':'g','4.':'gy','5':'h','5,':'l',
 '6':'j','6,':'n','6.':'ny','7':'k','7,':'s','7.':'sz','8':'m','8,':'t','9':'p','9,':'z'}
ROWS = """2. 3 1: 7, | 8 1. 3, 4, 1 8, 7 1' 8
2. 3, 8, 1: 7, 1 8, 5, 1: 7 | 5 0 4. | 7. 1: 3, 1: 6, 2, 2. 7, 1: 6, | 5 1. 9, 1. 2. 3, 8, 1: 8 | 6, 1. 4. 0 6,
6 0 | 1 3 0, | 3. 0 5, 8, | 7. 1 6, 8, 1: | 9 1. 7, 7. 1 0 | 3. 0 5, 8, | 6 0, 6, 6, 1 | 5 2. 8, | 0 3, 1' 3, 1.
2. 3, 8, 1: 8 | 1 | 3. 1' 3, 0 7, 1, 1. | 8 1: 3, 8, | 5 1. 7, 7, 1. 6, | 6 0, 8, 8, 1: 8 | 1 | 7. 1. 5, 0 7 1
4 1 .1 | 1 7, | .1 8, 0 5, 2. 3, 8, | 1 | 7. 0, 5, 5, 0, 7 | 7 0, 9, 8, | 8 1 3, 1: | 1. 9, | :1 9 5, 1: 8 5 1. 9,
2. 3, 8, :1 6, 7 | 8 1' 3, | 6. 1 8, 3. 1. | 3. 0 5, 8, | 3 1:
6, 1: 8 | 7. 0 5, 8 | 7, 1: 8 1 8, | 1. 9, | 0, 3, 1: 4, | 5, .1 1, 1
1 :1 1, 1' 6 8, 0 5, | 3. 0 6, 9, 3. 1.
7 1: 9, 1: 3 1: 8,
7. 1 3. 1, 1: 6, | 7. 1: 3, 1: 5, 1: 8
7, 0 7 7. 0 3, | 2, 0 7 0 5, 3. 1.
5 :1 | 1 8 1' 3 0 3 | 1 g 1. 9,
1 3. | 7 1: 3 3. 1: 7 1: 3 | 1' 3, 9 1' 3"""
words=[]; n=0; bad={}
for r in ROWS.splitlines():
    for w in r.split('|'):
        s=''
        for t in w.split():
            n+=1
            if t in KEY: s+=KEY[t]
            else: s+='<'+t+'>'; bad[t]=bad.get(t,0)+1
        words.append(s)
print('signs',n,'unkeyed',bad)
out=subprocess.run([sys.executable,'-I','../../work/decode.py'],capture_output=True,text=True).stdout
sol=' '.join(re.findall(r'\[([^\]]*)\]',out.split('[ ]')[0]))
def f(s):
    s=s.lower()
    for a,b in zip('óőíúűu','oöiüüü'): s=s.replace(a,b)
    return s.replace(' ','').replace('!','')
mine=''.join(words)
a,b=f(mine),f(sol)
print('mine :',' '.join(words))
print('solver:',sol)
import difflib
for op,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
    if op!='equal': print(op,repr(a[max(0,i-5):j+5]),'->',repr(b[max(0,k-5):l+5]))
