# Independent reviewer decoder for hcp-1408: own tokenizer + rule-based role assignment.
import sys
rows = ["OONOO","UOAOOIOU","ONOOOOMETOO","UOAOIDOSO","IONOOIOBUTU"]  # reviewer's own pixel reading
words = ["BUT","TOO","NO","ME","DO","SO","U","I","A","O"]
def tok(s):
    out=[];i=0
    while i<len(s):
        for w in words:
            if s.startswith(w,i) and not (w=="NO" and False):
                out.append(w); i+=len(w); break
    return out
names={"U":"you","I":"I","A":"a","NO":"no","ME":"me","TOO":"too","DO":"do","SO":"so","BUT":"but"}
for r in rows:
    t=tok(r); res=[]
    for k,x in enumerate(t):
        if x!="O": res.append(names[x]); continue
        prev=t[k-1] if k else None; nxt=t[k+1] if k+1<len(t) else None
        if prev in ("A","NO"): res.append("cipher")            # noun after determiner
        elif nxt in ("NO","ME","U","BUT","A") : res.append("sigh-for")  # verb before object
        else: res.append("O")                                  # interjection
    print(f"{r:12s} {sum(len(x) for x in t):2d} {' '.join(t):28s} -> {' '.join(res)}")
print("total signs", sum(map(len,rows)))
