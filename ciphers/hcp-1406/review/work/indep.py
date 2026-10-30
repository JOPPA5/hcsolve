import sys
groups = "Nz Pxo Cpz Mfuufs uijt npsojoh wfsz ojdf J bn joeppst bmm up Ebz Nz gspn Pxo Hjsm".split()
d=lambda w:''.join(chr((ord(c.upper())-65-1)%26+65) for c in w)
n=0
for g in groups: n+=len(g); print(g, d(g))
print("letters",n)
for g in ["EL","NL"]: print(g,"->",d(g))
