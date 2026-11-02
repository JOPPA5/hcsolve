#!/usr/bin/env python3
"""Reviewer's independent decode of hcp-1146. Own key (written by hand from hcp-1174 + review crops),
own parsing; takes signs from solver transcription only as token lists, applying reviewer corrections."""
import re,collections,sys
D='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1146/'
key=dict(x.split('=') for x in """0=o 0,=ö 1=i 1.=a 1:=e 1'=á 1,=b :1=ü .1=u 2,=cs 2.=é 3=d 3,=r 3.=v 4=f 4,=g 4.=gy
5=h 5,=l 6=j 6,=n 6.=ny 7=k 7,=s 7.=sz 8=m 8,=t 8.=ty 9=p 9,=z""".split())
fix={'városian':("3. 1' 3, 0 7, 1, 1. 6,",'városban')}   # review correction: comma under the 1
c=collections.Counter(); tot=0; odd=0; out=[]
for l in open(D+'work/transcription.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip(): continue
    sec,r=l.split(' ',1); ct,rd=[s.strip() for s in r.split('|')]
    if rd in fix: ct,rd=fix[rd]
    w=''
    for t in ct.split():
        tot+=1
        if '~' in t: odd+=1; t={'5~l':'5,','8~t':'8,','7~s':'7,'}[t]
        c[t]+=1; w+=key[t]
    out.append(w)
print(' '.join(out)); print('signs',tot,'by sense',odd,'distinct',len(c))
print('unused table signs',sorted(set(key)-set(c))); print(sorted(c.items()))
