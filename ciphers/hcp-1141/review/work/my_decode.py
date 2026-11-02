#!/usr/bin/env python3
# Independent decode of work/transcription.txt: rebuilt table from hcp-1174 prose, ignoring ~ overrides optional
import re,sys,collections
T="""0 o|0, ö|1 i|1. a|1: e|1' á|1, b|:1 u|2 c|2, cs|2. é|3 d|3, r|3. v|4 f|4, g|4. gy|5 h|5, l|6 j|6, n|6. ny|7 k|7, s|7. sz|8 m|8, t|9 p|9, z"""
K=dict(x.split() for x in T.split('|'))
raw = len(sys.argv)>1
c=collections.Counter()
for l in open('work/transcription.txt',encoding='utf-8'):
    if l.startswith('#'):continue
    o=''
    for t in l.split():
        if t=='/':o+=' '
        elif t.startswith('<') or t=='-':o+=t
        else:
            b=t.split('~')
            c[b[0]]+=1
            o+= (('['+K[b[0]]+'>'+b[1]+']') if len(b)>1 else K[b[0]])
    print(o)
print(sum(c.values()),len(c),sorted(c.items(),key=lambda x:-x[1]))
