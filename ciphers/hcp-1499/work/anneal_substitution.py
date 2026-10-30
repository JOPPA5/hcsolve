import sys, random, math, collections
S=sys.argv[1]; tf=sys.argv[2]; R=int(sys.argv[3])
fixed=dict(a.split('=') for a in sys.argv[4:])
words=[]
for line in open(tf):
    for w in line.strip().split('|'):
        t=w.split()
        if t: words.append(t)
syms=sorted({s for w in words for s in w})
corp=open(S+'/corpus.txt').read().lower().split()+open(S+'/common.txt').read().split()*3
wf=collections.Counter(corp)
dic=set(w.strip().lower() for w in open('/usr/share/dict/words') if w.strip().isalpha() and w.strip().islower())
tri=collections.Counter(); bi=collections.Counter()
for w in corp:
    w='^'+w+'$'
    for i in range(len(w)-2): tri[w[i:i+3]]+=1; bi[w[i:i+2]]+=1
cache={}
def wscore(w):
    if w in cache: return cache[w]
    w2='^'+w+'$'; s=0
    for i in range(len(w2)-2): s+=math.log((tri[w2[i:i+3]]+0.1)/(bi[w2[i:i+2]]+2.7))
    if w in wf: r=4+math.log(wf[w])
    elif w in dic and len(w)>=3: r=1+0.3*s
    else: r=s-4
    cache[w]=r; return r
alpha='abcdefghijklmnopqrstuvwxyz'
def score(m): return sum(wscore(''.join(m[s] for s in w)) for w in words)
free=[s for s in syms if s not in fixed]
best=None
for r in range(R):
    pool=[c for c in alpha if c not in fixed.values()]
    random.shuffle(pool)
    m=dict(fixed); 
    for s in free: m[s]=pool.pop()
    sc=score(m); T=3.0
    for it in range(20000):
        s=random.choice(free)
        # swap with another free symbol or unused letter
        used=set(m.values())
        if random.random()<0.5:
            s2=random.choice(free); m[s],m[s2]=m[s2],m[s]; undo=('sw',s,s2)
        else:
            un=[c for c in alpha if c not in used]
            if not un: continue
            old=m[s]; m[s]=random.choice(un); undo=('set',s,old)
        ns=score(m)
        if ns>=sc or random.random()<math.exp((ns-sc)/T): sc=ns
        else:
            if undo[0]=='sw': m[undo[1]],m[undo[2]]=m[undo[2]],m[undo[1]]
            else: m[undo[1]]=undo[2]
        T=max(0.1,T*0.9997)
    if best is None or sc>best[0]: best=(sc,dict(m))
    print(round(sc,1),' '.join(''.join(m[s] for s in w) for w in words), flush=True)
print('BEST',round(best[0],1),best[1])
