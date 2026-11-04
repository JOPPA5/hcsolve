# Independent reviewer decoder for hcp-1050: reviewer's own transcription (read from hires scan), key A=2..Z=26 without J.
import re, collections
T = """12.10.6.3.6.18 7.18.10.20.26
6.14.5.12.10.4.9 6.10.14
12.6.3.6.14.19 26.6.10.4.9.6.14
22.15.10.14 5.10.18 21.14.5
7.18.6.21.6 13.10.4.9 19.6.9.18
5.2.19 6.19 19.4.9.15.14
3.6.19.19.6.18 8.6.9.20 22.10.6=
12.6.10.4.9.20 11.15u.14.20.6.14
23.10.6.18 19.15.14.20.2.8
23.10.6.5.6.18 26.21.19.2.13b.6.14
19.6.10.14 23.2.19 10.19.20
5.6.14.14 19.15 16.12.15u.20.26=
12.10.4.9 21u.3.6.18 5.10.4.9
8.6.11.15.13b.6.14? 8.21.20.6 3.6.19.19.6=
18.21.14.8 3.2.12.5.10.8.6.14 23.10.6=
5.6.18.19.6.9.14 8.18.21.19.26 11.21.19.26
13.10.14.14.2"""
A = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
out=[]; cnt=collections.Counter()
for line in T.split("\n"):
    ws=[]
    for w in line.split():
        s=""; q=w.endswith("?"); w=w.rstrip("?")
        h=w.endswith("="); w=w.rstrip("=")
        for n in w.split("."):
            m=re.fullmatch(r"(\d+)([ub]?)",n); v=int(m.group(1)); cnt[v]+=1
            c=A[v-2]
            if m.group(2)=="u": c={"A":"Ä","O":"Ö","U":"Ü"}[c]
            if m.group(2)=="b": c*=2
            s+=c
        ws.append(s+("?" if q else "")+("-" if h else ""))
    out.append(" ".join(ws))
txt=" ".join(out).replace("- ","")
print(txt); print(sorted(cnt.items())); print("numbers:",sum(cnt.values()))
