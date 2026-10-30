#!/usr/bin/env python3
"""Reviewer's independent transcription and mechanical decoder for hcp-1786 (own reading of the hi-res scan).
Rules tested: consonant sign + optional modifiers; '/' crossed = +o; '#' heavy stroke = +a;
'^' caron (^- = e with caron = ě; ^~ = caron on the consonant, then e); vowels - . : after a sign. No free a/o insertion, unlike work/decode.py.
Run: python3 -I ciphers/hcp-1786/review/work/decode_review.py"""
import re, unicodedata
V={'0':'l','1':'d','2':'n','3':'m','4':'r','5':'s','6':'p','8':'h','9':'k','x':'z','j':'j','c':'c','v':'v','a':'a'}
C={'4':'ř','5':'š','x':'ž','c':'č','1':'ď'}
L="""64^.j3^-1- 64/x#1.3 1.31/ 1.9.
x# 65#2.c^9/ 2-53.5^ 5- x0#1c^9/
x0/6.1. vx^1.1^ j5-3 1. 65#0 x^~
j5/: 1/ 90-6.
1.2-5 j5-3 v 9:12- 8/4^ 64/ 4^~
6/v- 5-3-2/ x#5-1/ j.x^ 3#3- j-5^1^-
9/:5-9 4^~6. a 6:1- 8/1/v/
1^-5^.3 5- x^ 64^.j-1-1- 14^.v- 1/3:
j5/: x1- 80#12# a0- x0#1- 50:2.c^9/
64^~c- 01-v.4# 4.80- 94#5: 64.4/1.""".split('\n')
EXP="""přijměte prozatím tímto díky
za psaníčko nesmíš se zlatíčko
zlobiti vždyť jsem ti psal že
jsou to klepy
dnes jsem v kutné hoře pro ře
pové semeno zaseto již máme ještě
kousek řepy a bude hotovo
těším se až přijedete dříve domů
jsou zde chladna ale zlaté sluníčko
přece otevírá rychle krásu přírody""".split('\n')
tok=re.compile(r'([0-9xjcva])(/?)(#?)(\^(?!-))?|(\^-)|([-.:~])')
def dec(w):
    o=''
    for s,cr,h,car,he,m in tok.findall(w):
        if he: o+='ě'
        elif m: o+={'-':'e','~':'e','.':'i',':':'u'}[m]
        else:
            o+=(C[s] if car else V[s])
            if cr: o+='o'
            if h: o+='a'
    return o
def fold(t):
    t=unicodedata.normalize('NFD',t.lower()); t=''.join(c for c in t if not unicodedata.combining(c))
    return t.replace('ch','h').replace('y','i').replace('b','p').replace('t','d')
ok=bad=sg=0
for l,e in zip(L,EXP):
    lit=[dec(w) for w in l.split()]; ew=e.split()
    print(' '.join(lit)); 
    assert len(lit)==len(ew),(lit,ew)
    for a,b in zip(lit,ew):
        if fold(a)==fold(b): ok+=1
        else: bad+=1; print('   differs: literal',a,'reading',b)
print('words',ok+bad,'exact after folding b/p d/t h/ch i/y and accents:',ok,'different:',bad)
