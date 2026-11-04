# Independent reviewer decoder for hcp-945: own sign reading from enlarged crops.
# Sign names: R1=barred I, RX=barred X, R2=barred II, R4=barred IV/A-ligature, R5=barred V,
# R4s=four strokes under bar (u), R4su=same + diaeresis, dot, d1..d8 digits, hook7=?-shaped hook,
# hookl=long ʃ, big7=long 7, smallc=c hook, loop2=filled-loop 2 variant.
lines = [
 "d3 R4 dot d2 R4 | hookl dot R2 d6 R2 | big7 d4 dot R2 R5 R1",
 "d4 R4 dot hook7 R2 | d8 R4 R4s d1 R2 | loop2 RX smallc d8",
 "d2 R2 d8 R4 dot d3 | d8 R4su hook7 d1 R2 d2",
 "R5 R4 dot d2 | R2 R5 R4s RX d4 R5",
]
key = {"d3":"m","R4":"e","R2":"e","dot":"i","d2":"n","loop2":"n","hookl":"l","d6":"b",
       "big7":"f","d4":"r","R5":"d","R1":"a","RX":"a","hook7":"s","d8":"h","R4s":"u",
       "R4su":"ü","d1":"t","smallc":"c"}
from collections import Counter
cnt=Counter()
for l in lines:
    words=[]
    for w in l.split("|"):
        t=w.split(); cnt.update(t)
        words.append("".join(key[x] for x in t))
    print(" ".join(words))
print(len(cnt),"sign types;",sum(cnt.values()),"tokens")
print(sorted(cnt.items(), key=lambda x:-x[1]))
