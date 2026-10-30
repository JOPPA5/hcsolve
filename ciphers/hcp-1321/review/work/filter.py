#!/usr/bin/env python3
"""Second stage: (a) keep dictionary solutions whose sign->letter map gives each shape an unbroken alphabet block;
(b) repeat the search with a repo-derived common-word list, merged and with the solver's 3 merges split."""
import re,glob,collections
from independent import W,solve,load
base=load('/usr/share/dict/words')
# web2 has no inflected forms (no ARRIVED); add regular -d/-ed/-s/-ing forms
words=set(base)
for w in base:
    if 3<=len(w)<=6:
        words|={w+'s',w+'ed',w+'d',w+'ing'}
R=solve(words,W)
def ok(x):
    m={}
    for i,g in enumerate(W):
        for s,c in zip(g,x[i]): m[s]=c
    o=sorted(m,key=lambda k:m[k]); seq=[k[0] for k in o]
    ch=[seq[0]]
    for a in seq[1:]:
        if a!=ch[-1]: ch.append(a)
    return len(ch)==len(set(ch))
print('all',len(R)); B=[x for x in R if ok(x)]
print('block-consistent',len(B))
for x in B: print('  ',' '.join(x[i] for i in range(5)))
C=collections.Counter()
for f in glob.glob('../../../*/SOLUTION.md'):
    for w in re.findall(r"[A-Za-z]+",open(f,errors='ignore').read()): C[w.lower()]+=1
com={w for w,n in C.items() if n>=3 and len(w)>=2 and w in words}
print('common list',len(com))
r=solve(com,W); print('merged, common words',len(r))
for x in r[:30]: print('  ',' '.join(x[i] for i in range(5)))
for name,repl in [('circle split',{(1,0):'oTR'}),('triangle split',{(1,1):'tTR'}),('diamond split',{(1,3):'dTR'}),('all split',{(1,0):'oTR',(1,1):'tTR',(1,3):'dTR'})]:
    W2=[list(g) for g in W]
    for (i,j),v in repl.items(): W2[i][j]=v
    r=solve(com,W2); print(name,len(r))
    for x in sorted(r,key=str)[:12]: print('  ',' '.join(x[i] for i in range(5)))
