import math,random,sys
M={};fl=None
for l in open('/Users/tomaspavuk/Desktop/hcsolve/batches/scoring-sol61/german/model4.tsv'):
    if l.startswith('#'): fl=float(l.split()[1]);continue
    k,v=l.split('\t');M[k]=float(v)
W={}
for l in open('/Users/tomaspavuk/Desktop/hcsolve/batches/scoring-sol61/german/words.tsv'):
    w,f=l.split('\t');W[w]=int(f)
words=[]
for line in open(sys.argv[1]):
    for w in line.split('/'):
        t=w.split()
        if t: words.append(t)
syms=sorted({s for w in words for s in w})
A=list('abcdefghijklmnopqrstuvwxyz')
def score(k):
    s=0
    for w in words:
        p=''.join(k[c] for c in w)
        q='_'+p+'_'
        for i in range(len(q)-3): s+=M.get(q[i:i+4],M.get(p[i:i+4] if i+4<=len(p) else '',fl))
        if len(p)>=2 and p in W: s+=4*len(p)+math.log(1+W[p])
    return s
random.seed(int(sys.argv[3]) if len(sys.argv)>3 else 1)
best=None
for r in range(int(sys.argv[2])):
    perm=A[:];random.shuffle(perm)
    k={c:perm[i] for i,c in enumerate(syms)};spare=perm[len(syms):]
    cur=score(k);T=15
    for it in range(40000):
        if random.random()<0.5:
            a,b=random.sample(syms,2);k[a],k[b]=k[b],k[a]
            n=score(k)
            if n>cur or random.random()<math.exp((n-cur)/T): cur=n
            else: k[a],k[b]=k[b],k[a]
        else:
            a=random.choice(syms);j=random.randrange(len(spare));old=k[a];k[a]=spare[j];spare[j]=old
            n=score(k)
            if n>cur or random.random()<math.exp((n-cur)/T): cur=n
            else: spare[j]=k[a];k[a]=old
        T=max(0.3,T*0.99985)
    if best is None or cur>best[0]: best=(cur,dict(k))
    print(round(cur,1),' '.join(''.join(k[c] for c in w) for w in words),flush=True)
print(best)
