import re,glob,math,random,sys,collections
txt=''
for f in glob.glob('../../*/SOLUTION.md')+glob.glob('../../*/NOTES.md')+['../../../README.md']:
    t=open(f,errors='ignore').read()
    txt+=' '+t
L=re.sub('[^a-z]','',txt.lower())
print(len(L))
q=collections.Counter(L[i:i+4] for i in range(len(L)-3))
N=sum(q.values());fl=math.log(0.3/N)
Q={k:math.log(v/N) for k,v in q.items()}
rows=[l.split() for l in open('transcription.txt') if not l.startswith('#')]
base=[s for r in rows for s in r]
print(len(base),collections.Counter(base).most_common())
def run(seq,iters=60000,restarts=60):
    syms=sorted(set(seq)); idx=[syms.index(s) for s in seq]; n=len(syms)
    res=[]
    alpha=list('abcdefghijklmnopqrstuvwxyz')
    def score(k):
        p=[k[i] for i in idx]
        return sum(Q.get(''.join(p[i:i+4]),fl) for i in range(len(p)-3))
    for r in range(restarts):
        a=alpha[:];random.shuffle(a);k=a
        s=score(k);best=(s,k[:]);T=4.0
        for it in range(iters):
            T=4.0*(1-it/iters)+0.01
            i=random.randrange(n);j=random.randrange(26)
            k[i],k[j]=k[j],k[i]
            t=score(k)
            if t>s or random.random()<math.exp((t-s)/T):
                s=t
                if s>best[0]:best=(s,k[:])
            else:k[i],k[j]=k[j],k[i]
        res.append(best)
    res.sort(key=lambda x:-x[0])
    out=[]
    for s,k in res[:6]:
        out.append((round(s,1),''.join(k[i] for i in idx)))
    return out,syms
for name,seq in [('fwd',base),('rev',base[::-1])]:
    o,_=run(seq,iters=int(sys.argv[1]),restarts=int(sys.argv[2]))
    print(name);[print(x) for x in o]
