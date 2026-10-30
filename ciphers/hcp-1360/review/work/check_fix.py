# reviewer proposal: re-run the solver's shift over the corrected line 1, no solver file changed
s=lambda w:''.join(chr((ord(c)-97-1)%26+97) if c.islower() else chr((ord(c)-65-1)%26+65) for c in w)
L=["Nz","Pxo","Mpwjoh","Cpz","J","Gffm","wfsz","Ejtbqqpjoufe","up","Ebz","Op","Mfuufs","Zpvs","Hjsm"]
print(' '.join(s(w).upper() for w in L), sum(map(len,L)))
