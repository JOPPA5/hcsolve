import math,random,sys
from collections import Counter
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
A='abcdefghiklmnoprstuwz'
pen=float(sys.argv[4])
def score(k):
    s=0
    for w in words:
        p=''.join(k[c] for c in w)
        q='_'+p+'_'
        for i in range(len(q)-3): s+=M.get(q[i:i+4],fl)
        if len(p)>=2 and p in W and W[p]>0: s+=5*len(p)+math.log(1+W[p])
    c=Counter(k.values())
    s-=pen*sum(v-1 for v in c.values() if v>1)+1000*sum(1 for v in c.values() if v>2)
    return s
random.seed(int(sys.argv[3]))
best=None
for r in range(int(sys.argv[2])):
    k={c:random.choice(A) for c in syms}
    cur=score(k);T=15
    for it in range(40000):
        if random.random()<0.3:
            a,b=random.sample(syms,2);k[a],k[b]=k[b],k[a]
            n=score(k)
            if n>cur or random.random()<math.exp((n-cur)/T): cur=n
            else: k[a],k[b]=k[b],k[a]
        else:
            a=random.choice(syms);old=k[a];k[a]=random.choice(A)
            n=score(k)
            if n>cur or random.random()<math.exp((n-cur)/T): cur=n
            else: k[a]=old
        T=max(0.3,T*0.99985)
    if best is None or cur>best[0]: best=(cur,dict(k))
    print(round(cur,1),' '.join(''.join(k[c] for c in w) for w in words),flush=True)
print(best)
