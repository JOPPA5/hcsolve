#!/usr/bin/env python3
"""Reviewer's independent decoder for hcp-1164: table built per digit/mark, not imported."""
import re,collections,sys,os
R='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1164/work/transcription.txt'
T={'':'o i - d f h j k m p'.split(),'.':'- a é v gy ly ny sz ty zs'.split(),',':'ö b cs r g l n s t z'.split()}
def dec(s):
    if s=="1:":return 'e'
    if s=="1'":return 'á'
    if s==":1":return 'ü'
    m=re.fullmatch(r'(\d)([.,]?)',s)
    if not m: raise ValueError(s)
    v=T[m[2]][int(m[1])]
    if v=='-':raise ValueError(s)
    return v
words=[];signs=collections.Counter();bad=0
for l in open(R,encoding='utf-8'):
    l=l.rstrip('\n')
    if not l or l[0] in '#@/':continue
    ct,rd=[x.strip() for x in l.split('|')]
    w=''
    for t in ct.split():
        if t[0]=='=':w+=t[1:]
        else:
            w+=dec(t);signs[t]+=1
    words.append((w,rd))
print(' '.join(w for w,_ in words))
print('signs',sum(signs.values()),'distinct',len(signs))
print(sorted(signs.items(),key=lambda x:-x[1]))
