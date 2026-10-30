# Review 2 independent decode: own transcription, typed from r2/ crops, own arithmetic.
rows=["Nz Pxo Mpwjoh Cpz","Op ujnf up","Tfoe Mfuufs","Mpwf","Gspn Zpvs Pxo","Hjsm"]
def sh(s,k): return ''.join(chr((ord(c.lower())-97-k)%26+97) if c.isalpha() else c for c in s)
for k in range(26):
    t=' / '.join(sh(r,k) for r in rows)
    print(k,t)
print('letters',sum(c.isalpha() for r in rows for c in r))
