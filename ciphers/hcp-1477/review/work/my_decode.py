"""Reviewer's independent decode of HCP 1477 (own sign reading from 5-12x crops of
source/picture-large.jpg, strip rotated 90 deg clockwise). Own notation:
 digits as written; '=' dash+dot below; '%' dash+dots above&below; '-.' dash then dot;
 ':' two dots; '|' three dots; 'X' cross; '*' cross with dot above; 'B' heavy closed 5;
 'q' g-like tall 8/g glyph (reported separately, mapped per hypothesis below)."""
import sys
L = [
 "6aX 3u i:5e: *ä: i *äX3e: 3e: 3u =Xiq= 8a:",
 "9i=a :å 9i=e= ö3%9i5 19iX 3å 6äX3e: -.e: *aX",   # på: only TWO dots seen
 "B9a3 ä:3å. *ä:%qa| 1Xi=e% 1a:3e= 1Xi%=eX 8:i=%",
 "iqe: i:5e: Bi:5 %1ä= -.a: -.i%=eX %o-. e: *ä:.",
]
base = {"1":"b","3":"d","5":"g","6":"h","8":"k","9":"l","B":"g","=":"t","%":"s",
        "-.":"m",":":"n","|":"p","X":"r","*":"v",".":"."}
for hyp in ("k","g"):
    key = dict(base, q=hyp)
    print(f"-- tall g-like glyph = {hyp}")
    n = 0
    for l in L:
        out=[]
        for w in l.split():
            s=""; i=0
            while i < len(w):
                if w[i:i+2] == "-.": s+="m"; i+=2; n+=1; continue
                c=w[i]
                s += c if c in "aeiouåäö" else key[c]; i+=1; n+=1
            out.append(s)
        print(" ".join(out))
    print(f"[{n} signs]")
