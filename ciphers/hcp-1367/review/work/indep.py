#!/usr/bin/env python3
# Independent reviewer decode: own table, own retyped transcription (from review crops), not reading solver files.
import string
A=string.ascii_uppercase; T=str.maketrans(A,A[-1]+A[:-1])
rows=["NZ PXO MPWJOH CPZ","WFSZ NBOZ","IBOOZ SFUVFSOT","PG UIF EBZ","ZPVS PXO","HJSM"]
n=0
for r in rows:
    print(r,'->',r.translate(T)); n+=sum(c.isalpha() for c in r)
print(n)
for s in ("IBQQZ","SFUVSOT","SFUVFSOT"): print(s,s.translate(T))
# all 25 shifts of the whole text: only one gives English
txt=" ".join(rows)
for k in range(26):
    print(k," ".join(rows).translate(str.maketrans(A,A[k:]+A[:k]))[:50])
import datetime; print(datetime.date(1907,7,25).strftime('%A'))
