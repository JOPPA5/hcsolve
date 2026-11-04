import random, math, sys
common=set(open('common_words.txt').read().split())
dictw=set(w.strip().lower() for w in open('/usr/share/dict/words') if w.strip().isalpha() and w.strip().islower() and len(w.strip())>=3)
W={}
for w in dictw:
    if len(w)>=4: W[w]=0.8*len(w)-1.5
for w in common: W[w]=(1.6*len(w)+0.5) if len(w)>=3 else 1.0*len(w)

MAXL=12
lines=[l.split(':',1)[1] for l in open(sys.argv[1]) if ':' in l and not l.startswith('#')]
merge=dict(p.split('=') for p in sys.argv[3].split(',')) if len(sys.argv)>3 and sys.argv[3] else {}
allowrev = sys.argv[4]=='1' if len(sys.argv)>4 else False
segs=[[merge.get(x,x) for x in l.split() if x!='/'] for l in lines]
syms=sorted(set(s for w in segs for s in w)); alpha='abcdefghijklmnopqrstuvwxyz'
cache={}
def segscore(p):
    if p in cache: return cache[p]
    n=len(p); best=[-1e9]*(n+1); best[0]=0
    for i in range(1,n+1):
        b=best[i-1]-2.2   # unknown letter
        for L in range(1,min(MAXL,i)+1):
            w=p[i-L:i]
            if w in W:
                v=best[i-L]+W[w]
                if v>b: b=v
        best[i]=b
    cache[p]=best[n]; return best[n]
def dec(key,dirs):
    return [''.join(key[x] for x in (sg[::-1] if d else sg)) for sg,d in zip(segs,dirs)]
def score(key,dirs): return sum(segscore(p) for p in dec(key,dirs))
def seg_print(p):
    n=len(p); best=[-1e9]*(n+1); bp=[None]*(n+1); best[0]=0
    for i in range(1,n+1):
        best[i]=best[i-1]-2.2; bp[i]=(i-1,False)
        for L in range(1,min(MAXL,i)+1):
            w=p[i-L:i]
            if w in W and best[i-L]+W[w]>best[i]: best[i]=best[i-L]+W[w]; bp[i]=(i-L,True)
    out=[];i=n
    while i>0:
        j,ok=bp[i]; out.append(p[j:i] if ok else p[j:i].upper()); i=j
    return ' '.join(out[::-1])
random.seed(int(sys.argv[5]) if len(sys.argv)>5 else None)
for run in range(int(sys.argv[2])):
    key=dict(zip(syms,random.sample(alpha,len(syms)))); dirs=[False]*len(segs)
    cur=score(key,dirs);T=6
    for it in range(int(sys.argv[6]) if len(sys.argv)>6 else 40000):
        k2=dict(key); d2=list(dirs); r=random.random()
        if allowrev and r<0.04: i=random.randrange(len(d2)); d2[i]=not d2[i]
        else:
            a=random.choice(syms)
            if r<0.5: b=random.choice(syms); k2[a],k2[b]=k2[b],k2[a]
            else:
                used=set(k2.values()); k2[a]=random.choice([c for c in alpha if c not in used])
        sc=score(k2,d2)
        if sc>cur or random.random()<math.exp((sc-cur)/T): key,dirs,cur=k2,d2,sc
        T=max(0.05,T*0.9997)
        if len(cache)>200000: cache.clear()
    print(round(cur,1),' | '.join(seg_print(p) for p in dec(key,dirs)),flush=True)
