# Independent reviewer decode of hcp-1047 (own transcription from rotated hi-res crops).
# Key: A=2 ... I=10, K=11 ... Z=26 (no J). u = umlaut mark, m = overbar (double).
rows = """12 10 6 3 6 19 / 12 / 19 2 20 26 4 9 6 14
19 15 12 12 20 6 / 6 19 / 19 4 9 12 10 13m 6 18
8 6 23 15 18 5 6 14 / 19 6 10 14 , 23 2 19
10 4 9 / 14 10 4 9 20 / 9 15 7 7 6
19 15 / 8 6 9 6 / 23 10 6 5 6 18
26 21 13 / 2 18 26 20 ,
6 19 / 8 18 21u 19 26 20 / 21 14 5
11 21u 19 26 20 / 5 10 4 9
5 6 14 6 / 19 21 19 10"""
A = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
used = set()
for r in rows.splitlines():
    out = ""
    for t in r.split():
        if t == "/": out += " "; continue
        if t == ",": out += ", "; continue
        n = int(t.rstrip("um")); used.add(n)
        c = A[n - 2]
        if t.endswith("u"): c = {"U": "Ü", "A": "Ä", "O": "Ö"}[c]
        out += c * (2 if t.endswith("m") else 1)
    print(out)
print("numbers used:", sorted(used))
