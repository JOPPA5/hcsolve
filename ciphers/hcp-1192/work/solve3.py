import random, math, sys, re
from collections import Counter
txt=re.sub('[^a-z]','',open(sys.argv[1],errors='ignore').read().lower())
q=Counter(txt[i:i+4] for i in range(len(txt)-3)); N=sum(q.values())
floor=math.log10(0.01/N); qs={k:math.log10(v/N) for k,v in q.items()}
lines=[l.split(':',1)[1] for l in open(sys.argv[2]) if ':' in l and not l.startswith('#')]
merge=dict(p.split('=') for p in sys.argv[4].split(',')) if len(sys.argv)>4 and sys.argv[4] else {}
segs=[[merge.get(x,x) for x in l.split() if x!='/'] for l in lines]
syms=sorted(set(s for w in segs for s in w)); alpha='abcdefghijklmnopqrstuvwxyz'
def score(key,dirs):
    s=0
    for sg,d in zip(segs,dirs):
        p=''.join(key[x] for x in (sg[::-1] if d else sg))
        for i in range(len(p)-3): s+=qs.get(p[i:i+4],floor)
    return s
res=[]
for run in range(int(sys.argv[3])):
    key=dict(zip(syms,random.sample(alpha,len(syms)))); dirs=[random.random()<0.5 for _ in segs]
    cur=score(key,dirs);T=10
    for it in range(40000):
        k2=dict(key); d2=list(dirs); r=random.random()
        if r<0.05: i=random.randrange(len(d2)); d2[i]=not d2[i]
        else:
            a=random.choice(syms)
            if r<0.5: b=random.choice(syms); k2[a],k2[b]=k2[b],k2[a]
            else:
                used=set(k2.values()); k2[a]=random.choice([c for c in alpha if c not in used])
        sc=score(k2,d2)
        if sc>cur or random.random()<math.exp((sc-cur)/T): key,dirs,cur=k2,d2,sc
        T=max(0.1,T*0.9998)
    print(round(cur,1),' | '.join(''.join(key[x] for x in (sg[::-1] if d else sg)) for sg,d in zip(segs,dirs)),flush=True)
