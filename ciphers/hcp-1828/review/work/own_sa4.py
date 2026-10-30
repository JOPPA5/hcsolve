import re,glob,math,random,collections
src=open('own_decode.py').read(); R=src.split('R="""')[1].split('"""')[0]
rows=[l.split() for l in R.strip().splitlines()]
txt=''
for f in glob.glob('../../../*/SOLUTION.md')+glob.glob('../../../*/NOTES.md'):
    if 'hcp-1828' in f: continue
    txt+=' '+open(f,errors='ignore').read()
L=re.sub('[^a-z]','',txt.lower()); print(len(L))
c=collections.Counter(L[i:i+4] for i in range(len(L)-3)); N=sum(c.values()); fl=math.log(.3/N); Q={k:math.log(v/N) for k,v in c.items()}
random.seed(11)
def climb(seq,rest=25,it=25000):
    sy=sorted(set(seq));idx=[sy.index(s) for s in seq];best=(-1e9,'');al='abcdefghijklmnopqrstuvwxyz'
    for r in range(rest):
        k=list(al);random.shuffle(k)
        p=lambda:''.join(k[i] for i in idx)
        def sc():
            t=p();return sum(Q.get(t[i:i+4],fl) for i in range(len(t)-3))
        s=sc()
        for n in range(it):
            T=4*(1-n/it)+.01
            i=random.randrange(len(sy));j=random.randrange(26)
            k[i],k[j]=k[j],k[i];t=sc()
            if t>=s or random.random()<math.exp((t-s)/T): s=t
            else: k[i],k[j]=k[j],k[i]
            if s>best[0]: best=(round(s,1),p())
    return best
print('rot180',climb([s for r in rows[::-1] for s in r[::-1]]),flush=True)
print('scan',climb([s for r in rows for s in r]),flush=True)
print('rowsrev',climb([s for r in rows[::-1] for s in r]),flush=True)
print('inplace',climb([s for r in rows for s in r[::-1]]),flush=True)
sol='THANKSFORCARDABEAUTYSENDANYTHINGINTHECASTLEORRUINLINEWHENYOUCANTGETANYMOREACTRESSESWITHLOVEFROMADE'.lower()
print('claimed',round(sum(Q.get(sol[i:i+4],fl) for i in range(len(sol)-3)),1))
