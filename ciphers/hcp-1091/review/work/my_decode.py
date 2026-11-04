#!/usr/bin/env python3
# Reviewer's independent decode of hcp-1091, from my own reading of the
# rotated hires crops (review/work/*.png). Signs separated by spaces, words by '/'.
# R = r-sign (open 4 / S-like variant, same in B3 and B4), Y = closed 4 (s-homophone),
# T = o, T: = o-umlaut, U = n+breve/bar (u), N: = n+dots (ue), A: = dash+dots (ae),
# ? marks my reading uncertain, [x] = hidden under stamp/picture
LINES = [
 "0 ... 6 .. R", "J - 5 - 7 / 6 U - / !", "1 U / 6 . 7 1", "- 0 7 T / x . R 5 0 . + 8",
 ".. R 2 7 1 0 . + [8]", "6 T: 7 .. / ?", "8 - 6 / . + 8", "1 . + 8 / 1 .. 2", "Y T / 1 ... 9",
 "5 .. 5 R A: 2 5 1",
 "1 - 7 / 1 U", "3 .? R / 2 ...", "9 .. R + ... 2", "x . R 7 1 / .. 7", ". 7 1 / R .. 1? 8 1",
 "8 - R 1 / 9 T 2", "1 . R", "0 .. 6 .. / x 7? 0", "0 ... 6 .. R", "J - 5 - / x .. 2", "1 U / 3 . R",
 "7 + 8 T 2 / 2 . + 8 1", "9 .. R + ... 2", "5 - 2 7 1",
 "7 .. 2 1 .. / 1 . R / - 6 .. [R]", "1 T + 8 / 2 T + 8 / 1 .. [2]", "Y N: 7 .. 2 / 5 U 7",
]
K = {"0":"l","1":"t","2":"n","3":"m","R":"r","5":"k","6":"b","7":"s","8":"h","9":"v","x":"w",
     "+":"c","J":"j","Y":"s","T":"o","T:":"ö",".":"i","..":"e","...":"ie","-":"a","A:":"ä",
     "U":"u","N:":"ü","!":"!","?":"?"}
n=0; unk=[]
for i,l in enumerate(LINES):
    out=[]
    for w in l.split(" / "):
        s=""
        for t in w.split():
            core=t.strip("[]").rstrip("?") if t not in ("?",) else t
            if core not in K: unk.append(t); s+="#"; continue
            s+=K[core]+("?" if t.endswith("?") and t!="?" else "")
            n+=1
        out.append(s)
    print(i+1, " ".join(out))
print("signs", n, "unknown", unk)
