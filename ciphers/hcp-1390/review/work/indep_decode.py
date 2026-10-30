# Independent Caesar -1 decoder over the reviewer's own transcription of source/address.jpg (rotated 90 deg CCW).
import string, sys
lines = [
 "Nz. Pxo Efbsftu",
 "Nboz. uibolt Gps",
 "hsboe. Mfuufs.",
 "up ebz. [M] . [y?] [y?]",
 "Gspn zpvs. pxo",
 "[M+raised h/k/b-like sign]. Hjsm",
]
def dec(s):
    out=[];inb=False
    for ch in s:
        if ch=='[': inb=True
        if ch==']': inb=False; out.append(ch); continue
        if inb or not ch.isalpha(): out.append(ch); continue
        base='A' if ch.isupper() else 'a'
        out.append(chr((ord(ch)-ord(base)-1)%26+ord(base)))
    return ''.join(out)
n=0
for l in lines:
    print(f"{l:40s} -> {dec(l)}")
# frequency of shifts check: try all 26 on bracket-free text
txt=''.join(c for l in lines for c in l.split('[')[0] if c.isalpha()).lower()
print('letters (outside brackets, line-prefix only):',len(txt))
