# Independent decoder: key rebuilt from the alphabetical rule, not from key.json
import sys, re, collections
cons = [c for c in "BCDFGHJKLMNPQRSTVW"]
key = {}; i = 0
for side in "lrx":
    for pos in "tb":
        for n in "123":
            pass
for side in "lrx":
    for tok in ["1t","2t","3t","1b","2b","3b"]:
        key[side+tok] = cons[i]; i += 1
key.update(OD="A",TRI="E",TRIS="I",SQ="O",SQU="U",SQY="Y")
freq = collections.Counter(); out=[]
for line in open(sys.argv[1], encoding="utf-8"):
    if line.startswith("#") or not line.strip(): continue
    lab, body = line.split(":",1)
    body = re.sub(r"<[^>]*>", " ", body)
    s=""; prev=""
    for t in body.split():
        if t in key: prev=key[t]; s+=prev; freq[t]+=1
        elif t.startswith("ins:"): prev=key[t[4:]]; s+=prev; freq[t[4:]]+=1
        elif t=="x2": s+=prev
        elif t=="/": s+=" "
        elif t=="?x3": s+="?"
        else: s+=t
    out.append(f"{lab:4} {s}")
print("\n".join(out)); print(sorted(freq.items(), key=lambda x:-x[1]))
print("unused tokens:", [k for k in key if k not in freq])
