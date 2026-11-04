import sys,math,random
Q={}
for l in open('/Users/tomaspavuk/Desktop/hcsolve/batches/scoring-sol61/german/quadgrams.tsv'):
    k,v=l.split('\t'); Q[k]=float(v)
tot=math.log(sum(math.exp(v) for v in Q.values()))
for k in Q: Q[k]-=tot
floor=min(Q.values())-3
txt=open(sys.argv[1]).read()
merge=dict(a.split('=') for a in sys.argv[2:])
seq=[merge.get(ch,ch) for ch in txt if ch not in ' \n!']
from collections import Counter
syms=[s for s,_ in Counter(seq).most_common()]
letters=list('enisratdhulcgmobwfkzpvjyxq')
idx=[syms.index(s) for s in seq]
def score(perm):
    p=''.join(perm[i] for i in idx)
    return sum(Q.get(p[i:i+4],floor) for i in range(len(p)-3))
best=None
for r in range(int(30)):
    perm=letters[:]; 
    random.shuffle(perm[:]) 
    perm=letters[:len(syms)]+letters[len(syms):] if len(syms)<=26 else None
    perm=letters[:]; random.shuffle(perm)
    sc=score(perm); T=3.0
    for it in range(30000):
        i=random.randrange(len(syms)); j=random.randrange(26)
        perm[i],perm[j]=perm[j],perm[i]
        ns=score(perm)
        if ns>sc or random.random()<math.exp((ns-sc)/T): sc=ns
        else: perm[i],perm[j]=perm[j],perm[i]
        T=max(0.03,T*0.9998)
    k=dict(zip(syms,perm))
    out=' / '.join(''.join(k[merge.get(ch,ch)] if ch not in ' \n!' else ch for ch in line) for line in txt.strip().split('\n'))
    print(round(sc,1), out, flush=True)
