import sys,math,random
Q={}
for l in open('/Users/tomaspavuk/Desktop/hcsolve/batches/scoring-sol61/german/quadgrams.tsv'):
    k,v=l.split('\t'); Q[k]=float(v)
tot=math.log(sum(math.exp(v) for v in Q.values()))
for k in Q: Q[k]-=tot
floor=min(Q.values())-3
W={}
for l in open('/Users/tomaspavuk/Desktop/hcsolve/batches/scoring-sol61/german/words.tsv'):
    k,v=l.rstrip('\n').split('\t'); v=int(v)
    if v>=3 and len(k)>=2: W[k]=math.log(v)
args=sys.argv[2:]
fixed={}; merge={}; iters=int(40)
for a in args:
    if a.startswith('fix:'): s,t=a[4:].split('='); fixed[s]=t
    elif a.startswith('n:'): iters=int(a[2:])
    else: s,t=a.split('='); merge[s]=t
txt=open(sys.argv[1]).read().strip()
lines=[[ [merge.get(ch,ch) for ch in w] for w in line.split()] for line in txt.split('\n')]
words=[w for line in lines for w in line]
seq=[c for w in words for c in w]
from collections import Counter
syms=[s for s,_ in Counter(seq).most_common()]
letters=list('enisratdhulcgmobwfkzpvjyxq')
def dec(k,w): return ''.join(k[c] for c in w)
def score(k):
    p=''.join(k[c] for c in seq)
    s=sum(Q.get(p[i:i+4],floor) for i in range(len(p)-3))
    for w in words:
        d=dec(k,w)
        if d in W: s+=1.0*W[d]*min(len(d),5)/3
    return s
res=[]
for r in range(iters):
    perm=letters[:]; random.shuffle(perm)
    k=dict(zip(syms,perm[:len(syms)]))
    for s,t in fixed.items():
        o=[x for x in k if k[x]==t]
        if o: k[o[0]]=k[s]
        k[s]=t
    sc=score(k); T=4.0
    free=[s for s in syms if s not in fixed]
    for it in range(25000):
        a=random.choice(free)
        if random.random()<0.5:
            b=random.choice(free); k[a],k[b]=k[b],k[a]; undo=('s',a,b)
        else:
            used=set(k.values()); un=[l for l in letters if l not in used]
            if not un: continue
            old=k[a]; k[a]=random.choice(un); undo=('r',a,old)
        ns=score(k)
        if ns>sc or random.random()<math.exp((ns-sc)/T): sc=ns
        else:
            if undo[0]=='s': k[a],k[b]=k[b],k[a]
            else: k[a]=undo[2]
        T=max(0.05,T*0.9997)
    out=' / '.join(' '.join(dec(k,w) for w in line) for line in lines)
    res.append((sc,out,''.join(f'{s}{k[s]} ' for s in syms)))
res.sort()
for r in res[-6:]: print(round(r[0],1),r[1]); print('   ',r[2])
