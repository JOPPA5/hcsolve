# Independent reviewer decoder for hcp-1508: own transcription (from reviewer crops), own key derivation.
import sys, collections, hashlib
LINES = """1.26 18.3.12.4 13.17.4.6
17 11.3.6.8 12.21.11.16.6
8.22.17.10 {morning} 21.22.3.25
17 21.3.25.8 15.25 8.7 11.17.25.18
8.22.12.8 26.7.16 18.17.18
25.7.8 6.7.7.14 7.16.8 8.22.3
21.17.[N].18.7.21 17 4.16.25.13
8.22.3 15.3.6.6 12.6.6 8.22.3
21.12.26 8.7 26.7.16.4
9.6.12.20.3 15.16.8 18.17.18
25.7.8 21.12.25.8 8.7 4.17
25.13 17.8 8.7.7 6.7.16.18
8.7 12.21.12.14.3.25 1.26
18.3.12.4 18.7 26.7.16
21.12.25.8 1.3 8.7 10.8.7.9
{Sat.} 3.[V].3 [?].12.1 [V].3.4.26
10.7.4.4.26 17 {disappointed}
{you} 6.12.10.8 25.17.13.22.8
3.[V].3.4 26.7.16.4 11.4.17.3.25.18
24.24 3.2.4.12""".splitlines()
# key derived by me from cribs: MY(1.26) DEAR(18.3.12.4) GIRL(13.17.4.6) THE(8.22.3) LOOK(6.7.7.14) PLACE(9.6.12.20.3) BUT(15.16.8) XX(24.24) FELT/AWFUL(11, 21)
cribs = [("1.26","MY"),("18.3.12.4","DEAR"),("13.17.4.6","GIRL"),("8.22.3","THE"),("6.7.7.14","LOOK"),
         ("9.6.12.20.3","PLACE"),("15.16.8","BUT"),("24.24","XX"),("11.3.6.8","FELT"),("12.21.11.16.6","AWFUL"),
         ("21.22.3.25","WHEN"),("10.8.7.9","STOP")]
key = {}
for c,p in cribs:
    for n,l in zip(c.split("."),p):
        n=int(n); assert key.get(n,l)==l,(n,l,key.get(n)); key[n]=l
assert len(set(key.values()))==len(key)
print("key:", dict(sorted(key.items())))
cnt=collections.Counter(); unk=[]
for ln in LINES:
    out=[]
    for w in ln.split():
        if w.startswith("{"): out.append(w[1:-1].lower()); continue
        s=""
        for t in w.split("."):
            if t.startswith("["): s+=t[1:-1].lower(); continue
            n=int(t); cnt[n]+=1
            s+=key.get(n,f"<{n}>")
            if n not in key: unk.append(n)
        out.append(s)
    print(" ".join(out))
print("numeral tokens:",sum(cnt.values()),"unmapped:",unk)
print("freq:",sorted(cnt.items()))
