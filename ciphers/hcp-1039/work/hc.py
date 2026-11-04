import sys,math,random
Q={}
for l in open('/Users/tomaspavuk/Desktop/hcsolve/batches/scoring-sol61/german/quadgrams.tsv'):
    k,v=l.split('\t'); Q[k]=float(v)
tot=math.log(sum(math.exp(v) for v in Q.values()))
for k in Q: Q[k]-=tot
floor=min(Q.values())-3
txt=open(sys.argv[1]).read()
merge=dict(a.split('=') for a in sys.argv[2:]) if len(sys.argv)>2 else {}
seq=[merge.get(ch,ch) for ch in txt if ch not in ' \n!']
syms=sorted(set(seq))
letters='etaonisrhdulcgmobwfkzpvjyxq'
def dec(k): return ''.join(k[s] for s in seq)
def score(p): return sum(Q.get(p[i:i+4],floor) for i in range(len(p)-3))
best=None
for r in range(40):
    k={s:random.choice(letters[:22]) for s in syms}
    sc=score(dec(k)); 
    T=2.0
    for it in range(20000):
        s=random.choice(syms); old=k[s]
        k[s]=random.choice(letters)
        ns=score(dec(k))
        if ns>sc or random.random()<math.exp((ns-sc)/T): sc=ns
        else: k[s]=old
        T=max(0.05,T*0.9997)
    if best is None or sc>best[0]: best=(sc,dict(k))
    print(round(sc,1), ' '.join(''.join(k[merge.get(ch,ch)] if ch not in ' \n!' else ch for ch in line) for line in txt.split('\n')))
print(best)
