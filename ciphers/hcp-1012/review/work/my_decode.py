# Independent reviewer decoder for hcp-1012: derive key from cribs, test rule n-6 over J-less alphabet.
import string
alpha=[c for c in string.ascii_uppercase if c!='J']
key={i+7:c for i,c in enumerate(alpha)}
# my own reading of the card (rotated picture side), '+' marks plain Kurrent inside a cipher word
lines=["8 23 15 12 | 11 23 14 7 17 25 11 19 | 8 11 24 25 11 19",
"Dank für | 7 26 +F 16 17 7:umlaut 23 +U 19 13",
"Entschuldigen Diese(n/r) Karte!",
"8 23 15 11 12 | 12 20 17 13 25 | 24 20 +NN 25 7 13",
"[F?] der | 19 15 +CH 25 | 11 +H 11 23 | 31 11 15 25",
"der | 7 17 17 11 | 25 7 13 11 | Stunden! H. Gruss. [monogram]"]
used=set()
for L in lines:
    out=[]
    for w in L.split("|"):
        toks=w.split(); s=""
        for t in toks:
            if t.isdigit(): s+=key[int(t)]; used.add(int(t))
            elif t=="7:umlaut": s+="Ä"; used.add(7)
            elif t.startswith("+"): s+=t[1:]
            else: s+=t+" "
        out.append(s.strip())
    print(" / ".join(out))
print("distinct numbers", sorted(used), "all in 7..31:", all(7<=u<=31 for u in used))
