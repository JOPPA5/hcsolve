# Independent decode: table built by hand-free arithmetic; tokens re-keyed by the reviewer from own crops.
rows=["Nz Pxo Cpz","Tdippm usfbu","Jo Qbsl up","Ebz","zpvs Pxo","Hjsm"]
d=lambda c: chr((ord(c.lower())-97-1)%26+97)
n=0
for r in rows:
    w=[''.join(d(c) for c in t) for t in r.split()]; n+=sum(map(len,w)); print(' '.join(w))
print(n,'letters')
