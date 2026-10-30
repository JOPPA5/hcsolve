# Independent decode, typed from the reviewer's own reading of the scan.
ABC="abcdefghijklmnopqrstuvwxyz"
back={ABC[(i+1)%26]:ABC[i] for i in range(26)}
rows=["pomz. Xjti zpv.","Xfsf Ifsf. bt.","Xfmm. [M-L.] Gspn","Zpvs Pxo [E.L.] Hjsm"]
n=0;bad=0
for r in rows:
    o=[]
    for w in r.split():
        if w[0]=="[": o.append(w); continue
        t="".join(back[c.lower()] if c.isalpha() else c for c in w); n+=sum(c.isalpha() for c in w); o.append(t.upper())
    print(" ".join(o))
print("shifted letters",n)
