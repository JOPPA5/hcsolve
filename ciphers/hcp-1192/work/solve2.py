import random, math, sys, re, pickle, os
from collections import Counter
corp=sys.argv[1]
txt=re.sub('[^a-z]','',open(corp,errors='ignore').read().lower())
q=Counter(txt[i:i+4] for i in range(len(txt)-3)); N=sum(q.values())
floor=math.log10(0.01/N)
qs={k:math.log10(v/N) for k,v in q.items()}
lines=[l.split(':',1)[1] for l in open(sys.argv[2]) if ':' in l and not l.startswith('#')]
mode=sys.argv[3]
segs=[]
for l in lines:
    t=[x for x in l.split() if x!='/']
    segs.append(t[::-1] if mode=='rev' else t)
syms=sorted(set(s for w in segs for s in w))
alpha='abcdefghijklmnopqrstuvwxyz'
def score(key):
    s=0
    for sg in segs:
        p=''.join(key[x] for x in sg)
        for i in range(len(p)-3): s+=qs.get(p[i:i+4],floor)
    return s
best=None
for run in range(int(sys.argv[4])):
    key=dict(zip(syms,random.sample(alpha,len(syms))))
    cur=score(key);T=10
    for it in range(30000):
        k2=dict(key); a=random.choice(syms)
        if random.random()<0.5:
            b=random.choice(syms); k2[a],k2[b]=k2[b],k2[a]
        else:
            used=set(k2.values()); k2[a]=random.choice([c for c in alpha if c not in used])
        sc=score(k2)
        if sc>cur or random.random()<math.exp((sc-cur)/T): key,cur=k2,sc
        T=max(0.1,T*0.9997)
    print(round(cur,1),' | '.join(''.join(key[x] for x in sg) for sg in segs),flush=True)
