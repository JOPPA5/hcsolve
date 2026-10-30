#!/usr/bin/env python3
"""Reviewer's independent decode of hcp-1321. No use of work/key.json or work/transcription.txt.
Signs are recorded from the reviewer's own crops as (shape, dot-class). The value of each
class is derived from a rule: shapes in order square,triangle,circle,angle,diamond,caret take
... no such block rule is assumed here: a dictionary search finds every word assignment
that fits the repeat pattern of the sign classes (the five sign groups as written)."""
import sys,re,collections
W=[['dC','aU','aD'],['oT','tT','oL','dT'],
   ['sTL','dT','dT','oL','v','tT','sBR'],['aV','sTL','dC','dB'],['aD','oL','tLR','oT','dB']]
def load(p,minfreq=None):
    w=set()
    for l in open(p,errors='ignore'):
        l=l.strip()
        if l.isalpha() and l.islower(): w.add(l)
    return w
def solve(words,W):
    def pat(x):
        d={}
        return tuple(d.setdefault(c,len(d)) for c in x)
    bylen=collections.defaultdict(list)
    for w in words: bylen[pat(w)].append(w)
    res=[]
    order=sorted(range(len(W)),key=lambda i:-len(W[i]))
    def rec(k,m,inv,ch):
        if k==len(order):
            res.append(dict(zip(order,ch)));return
        G=W[order[k]]
        for w in bylen[pat(G)]:
            m2=dict(m);i2=dict(inv);ok=True
            for s,c in zip(G,w):
                if m2.get(s,c)!=c or i2.get(c,s)!=s: ok=False;break
                m2[s]=c;i2[c]=s
            if ok: rec(k+1,m2,i2,ch+[w])
    rec(0,{},{},[])
    return res
def show(name,W,words):
    r=solve(words,W)
    print(name,len(r),'solutions')
    return r
if __name__=='__main__':
    words=load('/usr/share/dict/words')
    print('dict',len(words))
    r=show('merged',W,words)
    out=sorted(' '.join(x[i] for i in range(5)) for x in r)
    print('\n'.join(out[:40]))
    # pure English frequent-word filter: words seen in the repo's FINAL English plaintext is not used; length-filter only
    common=set(l.split()[0] for l in open(sys.argv[1])) if len(sys.argv)>1 else None
    # relaxed: split the three merges the solver disclosed
    W2=[list(x) for x in W]; W2[1][0]='oTR'; W2[1][1]='tTR'; W2[1][3]='dTR'
    r=show('unmerged (all three split)',W2,words)
    out=sorted(' '.join(x[i] for i in range(5)) for x in r)
    print(len(out)); print('\n'.join(out[:25]))
