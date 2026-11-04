#!/usr/bin/env python3
"""Reviewer's independent decoder for hcp-1100 (does not import the solver's decode.py).
Key re-entered by the reviewer from his own reading of the enlarged crops."""
import sys, collections, re
KEY = {  # letter -> shape codes as seen by the reviewer
 'A':['c','cq','arc','gam'],'D':['sev'],'E':['b','bb','bf','lp'],'F':['hi'],'G':['p'],
 'H':['blob'],'I':['i'],'J':['cross'],'K':['el'],'L':['eps','rev3','zh'],'M':['hk'],
 'N':['yn','eta'],'O':['sq','sq4'],'P':['nine'],'Q':['tri'],'R':['h'],'S':['lam'],
 'T':['u','bar','dx'],'U':['vs','vt'],'V':['crl'],'W':['hn'],'Y':['pen'],'&':['amp']}
INV = {}
for L, cs in KEY.items():
    for c in cs:
        assert c not in INV, c
        INV[c] = L
path = sys.argv[1]
use = collections.Counter(); out = []
for line in open(path, encoding='utf-8'):
    line=line.strip()
    if not line or line.startswith('#'): continue
    tag, body = line.split(':',1)
    words=[]
    for w in body.split('|'):
        w=w.strip()
        if w.startswith('='): words.append(w[1:]); continue
        if w.startswith('['): words.append('[struck]'); continue
        s=''
        for c in w.split():
            use[c]+=1
            s += INV.get(c,'?')
        words.append(s)
    out.append(f"{tag}: {' '.join(words)}")
print('\n'.join(out))
print('signs decoded:', sum(use.values()), 'unknown:', [c for c in use if c not in INV])
print('single-occurrence codes:', sorted(c for c,n in use.items() if n==1))
print('unused key codes:', sorted(set(INV)-set(use)))
