#!/usr/bin/env python3
# Independent decode: own key (written from the sister-card tables + this card's claims), own parser.
import re,collections,sys,os
D=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
key={}
for v,s in {'i':'1','a':'1.','e':'1:','á':"1'",'ü':':1','b':'1,','o':'0','ö':'0,','c':'2','[cs]':'2,','é':'2.','d':'3','r':'3,','v':'3.',
 'f':'4','g':'4,','[gy]':'4.','h':'5','l':'5,','j':'6','n':'6,','[ny]':'6.','k':'7','s':'7,','[sz]':'7.','m':'8','t':'8,','p':'9','z':'9,'}.items():
    key[s]=v
print('distinct signs in reviewer key',len(key))
toks=[];per=[];rows=[[]]
for l in open(D+'/work/transcription.txt',encoding='utf-8'):
    if l.startswith('#') or '=' not in l: continue
    w,ct=l.strip().split(' = ')
    o=''
    for t in ct.split():
        if t=='/': rows.append([]); continue
        s=t.split('~')[0]; toks.append(s); rows[-1].append(s)
        o+= t.split('~')[1] if '~' in t else key[s]
    per.append((w,o))
print('tokens',len(toks)); 
cnt=collections.Counter(toks); print('distinct used',len(cnt),cnt.most_common())
print(' '.join(o for w,o in per))
print('rows',len(rows),[len(r) for r in rows])
print('row-signs:'); [print(i+1,' '.join(r)) for i,r in enumerate(rows)]
