import math,sys,heapq
voc={}
for l in open('ciphers/hcp-1500/work/tests/vocab.txt'):
    w,c=l.split(); voc[w]=int(c)
voc.setdefault('a',500);voc.setdefault('i',500)
toks=sys.argv[1].split()
inj = not (len(sys.argv)>2 and sys.argv[2]=='homo')
def pat(w):
    m={};return tuple(m.setdefault(c,len(m)) for c in w)
byp={}
for w,c in voc.items(): byp.setdefault((len(w),pat(w)),[]).append((math.log(c),w))
cands=[sorted(byp.get((len(t),pat(t)),[]),reverse=True) for t in toks]
def fits(t,w,m,inv):
    nm={}
    for c,p in zip(t,w):
        q=m.get(c) or nm.get(c)
        if q:
            if q!=p: return None
        else:
            if inj:
                r=inv.get(p)
                if r and r!=c: return None
                if p in nm.values(): return None
            nm[c]=p
    return nm
best=[];cnt=[0]
def dfs(left,m,inv,sc,ch):
    cnt[0]+=1
    if not left:
        heapq.heappush(best,(sc,cnt[0],dict(ch)))
        if len(best)>40: heapq.heappop(best)
        return
    opts=None;bi=None
    for i in left:
        o=[(s,w,nm) for s,w in cands[i] for nm in [fits(toks[i],w,m,inv)] if nm is not None]
        if opts is None or len(o)<len(opts): opts,bi=o,i
        if not o: return
    for s,w,nm in opts:
        m2=dict(m);m2.update(nm);i2=dict(inv);i2.update({p:c for c,p in nm.items()})
        ch[bi]=w;dfs([j for j in left if j!=bi],m2,i2,sc+s,ch)
dfs(list(range(len(toks))),{},{},0,{})
for sc,_,ch in sorted(best,reverse=True):
    print(round(sc,1),' '.join(ch[i] for i in range(len(toks))))
print('nodes',cnt[0])
