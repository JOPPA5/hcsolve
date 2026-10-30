# Keyword-alphabet screen for HCP 1434 (Claude Opus 5.5, 2026-10-30)
import math,sys
F=dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',[8.2,1.5,2.8,4.3,12.7,2.2,2.0,6.1,7.0,.15,.77,4.0,2.4,6.7,7.5,1.9,.1,6.0,6.3,9.1,2.8,1.0,2.4,.15,2.0,.07]))
LF={k:math.log(v/100) for k,v in F.items()}
words=[w.strip().upper() for w in open('/usr/share/dict/words') if w.strip().isalpha() and w.strip().islower() and 3<=len(w.strip())<=8]
CTS={'full':'PHSTNAAHSEHHGGTOGAAAAFNYNJASFCEAN','noA':'PHSTNHSEHHGGTOGFNYNJSFCEN'}
def mixed(kw):
    s=[]
    for c in kw+'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if c not in s: s.append(c)
    return ''.join(s)
A='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res=[]
for kw in set(words):
    m=mixed(kw)
    for d,tab in (('dec',str.maketrans(m,A)),('enc',str.maketrans(A,m))):
        for n,ct in CTS.items():
            p=ct.translate(tab)
            sc=sum(LF[c] for c in p)/len(p)
            res.append((sc,kw,d,n,p))
res.sort(reverse=True)
for r in res[:40]: print(r)
