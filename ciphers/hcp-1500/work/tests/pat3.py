import math,sys,heapq
voc={}
for l in open('ciphers/hcp-1500/work/tests/vocab.txt'):
    w,c=l.split(); voc[w]=int(c)
voc.setdefault('a',500);voc.setdefault('i',500)
toks=sys.argv[1].split()
def pat(w):
    m={};return tuple(m.setdefault(c,len(m)) for c in w)
byp={}
for w,c in voc.items(): byp.setdefault((len(w),pat(w)),[]).append((math.log(c),w))
cands=[sorted(byp.get((len(t),pat(t)),[]),reverse=True) for t in toks]
def add(m,c,p):
    # involution
    for a,b in ((c,p),(p,c)):
        if a in m:
            if m[a]!=b: return False
        else:
            if b in m.values() and [k for k,v in m.items() if v==b][0]!=a: return False
            m[a]=b
    return True
def fits(t,w,m):
    m2=dict(m)
    for c,p in zip(t,w):
        if not c.isalpha(): return None
        if not add(m2,c,p): return None
    return m2
best=[];cnt=[0]
def dfs(left,m,sc,ch):
    cnt[0]+=1
    if not left:
        heapq.heappush(best,(sc,cnt[0],dict(ch)))
        if len(best)>40: heapq.heappop(best)
        return
    opts=None;bi=None
    for i in left:
        o=[(s,w,nm) for s,w in cands[i] for nm in [fits(toks[i],w,m)] if nm is not None]
        if opts is None or len(o)<len(opts): opts,bi=o,i
        if not o: return
    for s,w,nm in opts:
        ch[bi]=w;dfs([j for j in left if j!=bi],nm,sc+s,ch)
dfs(list(range(len(toks))),{},0,{})
for sc,_,ch in sorted(best,reverse=True):
    print(round(sc,1),' '.join(ch[i] for i in range(len(toks))))
print('nodes',cnt[0])
