import random, math, sys, re
from collections import Counter
words_common=set(open('common_words.txt').read().split())
dictw=set(w.strip().lower() for w in open('/usr/share/dict/words') if w.strip().isalpha() and w.strip().islower())
dictw|=words_common
lines=[l.split(':',1)[1] for l in open(sys.argv[1]) if ':' in l and not l.startswith('#')]
rev = len(sys.argv)>2 and sys.argv[2]=='rev'
words=[]
for l in lines:
    for w in l.split('/'):
        t=w.split()
        if t: words.append(t[::-1] if rev else t)
syms=sorted(set(s for w in words for s in w))
freq={'e':12.7,'t':9.1,'a':8.2,'o':7.5,'i':7.0,'n':6.7,'s':6.3,'h':6.1,'r':6.0,'d':4.3,'l':4.0,'c':2.8,'u':2.8,'m':2.4,'w':2.4,'f':2.2,'g':2.0,'y':2.0,'p':1.9,'b':1.5,'v':1.0,'k':0.8,'j':0.15,'x':0.15,'q':0.1,'z':0.07}
alpha='abcdefghijklmnopqrstuvwxyz'
def score(key):
    s=0
    for w in words:
        p=''.join(key[x] for x in w)
        if p in words_common: s+= 3*len(p)
        elif p in dictw: s+= 1.0*len(p) if len(p)>2 else 0.3
        else: s-=0.5*len(p)
        for c in p: s+=0.15*math.log(freq[c]/4)
    return s
best=None
for run in range(int(sys.argv[3]) if len(sys.argv)>3 else 30):
    letters=random.sample(alpha,len(syms))
    key=dict(zip(syms,letters))
    cur=score(key);T=5
    for it in range(60000):
        k2=dict(key)
        a=random.choice(syms)
        if random.random()<0.5:
            b=random.choice(syms); k2[a],k2[b]=k2[b],k2[a]
        else:
            used=set(k2.values()); free=[c for c in alpha if c not in used]
            k2[a]=random.choice(free)
        sc=score(k2)
        if sc>cur or random.random()<math.exp((sc-cur)/T):
            key,cur=k2,sc
        T=max(0.05,T*0.9997)
    if best is None or cur>best[0]: best=(cur,key)
    print(round(cur,1),' '.join(''.join(key[x] for x in w) for w in words),flush=True)
print('BEST',best)
