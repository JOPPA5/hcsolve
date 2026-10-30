# Independent decode: arithmetic shift, reviewer's own sign-by-sign reading (not read from transcription.json)
rows=[["Nz","Pxo","Cpz"],["Mfuufs","wfsz"],["ojdf","up","Ebz"],["Zpvs","Pxo"],["Hjsm"]]
def d(w): return ''.join(chr((ord(c.upper())-65-1)%26+65) for c in w)
n=0
for r in rows:
    print([d(w) for w in r]); n+=sum(map(len,r))
print(n,'letters')
for s in range(1,26):
    t=' '.join(''.join(chr((ord(c.upper())-65-s)%26+65) for c in w) for r in rows for w in r)
    if s<4: print(s,t)
