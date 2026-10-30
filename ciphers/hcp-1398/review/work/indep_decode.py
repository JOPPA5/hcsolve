# Independent Caesar -1 decode of the reviewer's own transcription (no solver files used).
rows = ["Nz. pxo. efbstu Cpz.",   # reviewer reads 6 letters e-f-b-s-t-u (no second f)
        "J. pomz. ibwf uijt",
        "wjfx Jo. nz bmcvn",
        "Zpvs. hjsm",
        "Mpp"]                    # capital M: three minims / two arches
def dec(s): return ''.join(chr((ord(c.upper())-66)%26+65) if c.isalpha() else c for c in s)
n=0
for r in rows:
    n+=sum(c.isalpha() for c in r); print(f"{r:24s} -> {dec(r)}")
print("letters:",n)
