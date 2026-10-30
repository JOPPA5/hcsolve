import sys
toks=['abc','ly','xuder','comde','h','lz','kncv','pne','pnvvx','cn']
words=set(w.strip().lower() for w in open('/usr/share/dict/words') if w.strip().islower())
common2={'am','an','as','at','be','by','do','go','he','if','in','is','it','me','my','no','of','oh','on','or','so','to','up','us','we'}
words={w for w in words if len(w)>2}|common2|{'i','a'}
A='abcdefghijklmnopqrstuvwxyz'
def keyed(k):
    s=''
    for c in k+A:
        if c not in s: s+=c
    return s
seen=set();res=[]
for w in open('/usr/share/dict/words'):
    w=w.strip().lower()
    if not w.isalpha() or len(w)>14: continue
    ka=keyed(w)
    if ka in seen: continue
    seen.add(ka)
    for off in range(26):
        alph=ka[off:]+ka[:off]
        # dir1: plain A[i] -> cipher alph[i]; decrypt maps alph[i]->A[i]
        d1={alph[i]:A[i] for i in range(26)}
        d2={A[i]:alph[i] for i in range(26)}
        for d in (d1,d2):
            pt=[''.join(d[c] for c in t) for t in toks]
            sc=sum(len(p) for p in pt if p in words)
            if sc>=13: res.append((sc,w,off,' '.join(pt)))
res.sort(reverse=True)
for r in res[:40]: print(r)
