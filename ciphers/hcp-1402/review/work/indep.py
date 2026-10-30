import sys
rows = ["Nz Pxo [NL] Cpz","Mfuufs uijt","npsojoh xbt","GJOF Nboz uibolt","Nz [N&L] gspn","zpvs Pxo [NL]","Hjsm"]
def d(w):
    if w.startswith('['): return w
    return ''.join(chr((ord(c.upper())-65-1)%26+65) for c in w)
n=0
for r in rows:
    print(' '.join(d(w) for w in r.split()))
    n+=sum(len(w) for w in r.split() if not w.startswith('['))
print(n)
