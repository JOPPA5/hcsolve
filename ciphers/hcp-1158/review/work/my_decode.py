#!/usr/bin/env python3
"""Reviewer's independent decode of hcp-1158. Ciphertext re-keyed by the reviewer from review/work/g*_*.png crops,
one string per card line; key imported from FINAL sister card hcp-1174 only, so the two signs new on this card stay visible."""
import collections, re, sys, os
R=os.path.dirname(os.path.abspath(__file__)); C=os.path.join(R,'..','..')
L={'T':"2. 3 1: 7, | 8 1. 3, 4, 1 8, 7 1' 8",
'1':"8, 1: 3, 1: 8 | 3. 1 3, 1' 4, | 7 1 7, | 7 1: 3, 8, 1: 8 1, 1: 6,",
'2':"8, 1: 3, 1: 8 | 7 :1 6, 6, | 1. | 3, 2. 8, 1: 6,",
'3':"3 1: | 1. | 5, 1: 4, 7. 1: 1, 1, | 3. 1 3, 1' 4, | 8, 1: | 3. 1. 4.",
'4':"2. 3 1: 7, | 8 1 6, 3 1: 6, 7, 2. 4, 1: 8",
'5':"5 1. | 1: 4. 8 1' 7, 5 0 9, | 7 1 6, 2, 1: 8",
'6':"1 4, 1. 9, | 7. 1 3. 3. 1: 5, | 5, 1: 7. :1 6, 7",
'7':"1. | 1, 0 5, 3 0 4, 7, 1' 4, | 3, 2. 3. 2. 1, 1:",
'8':"8 1: 4, 5, 1' 7, 3 | 1, 1: 1: 3. 1: 9, :1 6, 7",
'9':"1 3, 3 | 8 1: 4, | 6, 2. 7 1: 8 | 2. 3 1: 7, | 7. 1: 6, 8, 1: 8,",
'10':"3 3, 1' 4, 1. | 3 1 3, 1' 4, 7. 1' 5, 0 8",
'11':"5, 1: 7. 1: 5, - 1: | 5 0 4. 5 1. | 8 1: 4, | 7 2. 3, 5, 1: 7",
'12':"1. | 7. 1: 3, 1: 8, 0, | 9 1' 3, 0 8",
'13':"1: 9, 8, | 1. | 9 1' 3, | 7, 0 3, 8, | 7 :1 5, 3 0, 8",
'14':"6, 1: 7 1: 3 | 7. 2. 9 | 1, 1. 1, 1' 8",
'15':"5, 2. 4. | 1, 0 5, 3 0 4, | 2. 7, | 4, 0 6, 3 0 5, 6",
'16':"6, 2. 5 1. - 6, 2. 5 1. | 3, 1' 8",
'17':"7. 1' 8 8, 1. 5, 1. 6, 7. 0 3, | :1 3 3. 0, 9, 0, 5, | 2. 7,",
'18':"2, 0 7 0 5, | 5 :1 | 7 1: 3 3. 1: 7, 1: 3 | 1' 3, 9 1' 3"}
KEY={'0':'o','0,':'ö','1':'i','1.':'a','1:':'e',"1'":'á',':1':'ü','1,':'b','2,':'cs','2.':'é','3':'d','3,':'r','3.':'v',
 '4,':'g','5':'h','5,':'l','6,':'n','7':'k','7,':'s','7.':'sz','8':'m','8,':'t','9':'p','9,':'z'}
cnt=collections.Counter(); n=0
for k,v in L.items():
    o=[]
    for w in v.split(' | '):
        s=''
        for t in w.split():
            if t=='-': s+='-'; continue
            n+=1; cnt[t]+=1; s+=KEY.get(t,'['+t+']')
        o.append(s)
    print(k.rjust(2),' '.join(o))
print('signs',n,'distinct',len(cnt)); print('outside hcp-1174 key:',{t:c for t,c in cnt.items() if t not in KEY}); print(sorted(cnt.items(),key=lambda x:-x[1]))
# compare token stream with the solver's
S=[]
for ln in open(os.path.join(C,'work/transcription.txt'),encoding='utf-8'):
    if ln.startswith('#') or not ln.strip(): continue
    S+= [re.sub(r'<.*>','',t) for t in ln.split()[1:] if t not in('/','-')]
M=[t for v in L.values() for t in v.split() if t not in('|','-')]
print('tokens solver',len(S),'mine',len(M),'identical',S==M)
