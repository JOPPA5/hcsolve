# Independent reviewer decoder: Caesar -1 over reviewer's own transcription.
rows = ["Nz. Efbsftu.", "J bn. kvtu", "Hpjoh up qptu", "M. & L. gspn.", "Zpvs. pxo", "Hjsm"]
alt  = ["N. & L. gspn."]  # alternative reading of first closing initial
def d(s): return "".join(chr((ord(c.upper())-65-1)%26+65) if c.isalpha() else c for c in s)
n=0
for r in rows: n+=sum(c.isalpha() for c in r); print(f"{r:16} -> {d(r)}")
print("letters:",n)
for r in alt: print("ALT", r, "->", d(r))
