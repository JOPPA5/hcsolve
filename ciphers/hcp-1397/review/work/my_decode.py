"""Reviewer's independent check for HCP 1397: my own reading of source/address.jpg
(rotated 90 deg CCW), decoded by shifting each letter back by one (B->A ... A->Z)."""
lines=["Nz. Efbsftu uijt","pof. jt.b. tdpudi","wjfx Mpwf gspn","zpvs. Pxo. Hjsm."]
def shift(s,k):
    return ''.join(chr((ord(c.upper())-65-k)%26+65) if c.isalpha() else c for c in s)
for l in lines: print(f'{l:22s} -> {shift(l,1)}')
print('letters:',sum(c.isalpha() for c in ''.join(lines)))
