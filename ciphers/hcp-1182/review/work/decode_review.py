"""Reviewer's independent decoder for hcp-1182 (written without reusing work/decode.py).
Usage: python3 -I review/work/decode_review.py ciphers/hcp-1182/work/transcription.txt"""
import sys, collections
# International Morse (ITU) + German extensions, built from letter -> code
CODE = dict(A=".-",B="-...",C="-.-.",D="-..",E=".",F="..-.",G="--.",H="....",I="..",J=".---",
  K="-.-",L=".-..",M="--",N="-.",O="---",P=".--.",Q="--.-",R=".-.",S="...",T="-",U="..-",V="...-",
  W=".--",X="-..-",Y="-.--",Z="--..")
CODE.update({"Ä":".-.-","Ö":"---.","Ü":"..--","CH":"----"})
INV = {v:k for k,v in CODE.items()}
std_out, var_out, used = [], [], collections.Counter()
for ln in open(sys.argv[1], encoding="utf-8"):
    if not ln.startswith("L"): continue
    a = b = ""
    for t in ln.split(":",1)[1].split():
        if t in ("[u","u]"): continue
        if t == "|": a += " "; b += " "; continue
        if t == "=": continue
        if t == "-dash-": a += "–"; b += "–"; continue
        n = 2 if t.endswith("*2") else 1; t = t.replace("*2","")
        used[t] += n
        s = INV.get(t, "?")
        a += s*n
        b += ({"P":"W","Y":"Z"}.get(s, s))*n
    std_out.append(a); var_out.append(b)
print("Standard ITU reading:\n", " ".join(" ".join(std_out).split()))
print("With writer variants P->W, Y->Z:\n", " ".join(" ".join(var_out).split()))
print("Codes used:", sorted(used.items(), key=lambda x:-x[1]))
print("Unknown codes:", [c for c in used if c not in INV])
print("Std W .-- used:", used.get(".--",0), " Std Z --.. used:", used.get("--..",0))
