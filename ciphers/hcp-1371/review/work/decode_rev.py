# independent: own transcription typed from review crops, table-free mod-26 arithmetic
import datetime,sys
lines=["Nz Pxo * Cpz","Mfuufs up-Ebz","tqmfoeje Mpwf","* Gspn Zpvs","Pxo * Hjsm"]
sh=lambda w:''.join(chr((ord(c.upper())-65-1)%26+65) if c.isalpha() else c for c in w)
n=0
for l in lines:
    print(l,'=>',' '.join(sh(w) for w in l.split())); n+=sum(c.isalpha() for c in l)
print('letters',n)
print(datetime.date(1907,7,22).strftime('%A'))
from collections import Counter
s=''.join(lines).replace('*','').replace(' ','').replace('-','').lower()
print({k:sum(sh(s).lower()==x for x in [sh(s).lower()]) for k in []})
for k in range(26):
    d=''.join(chr((ord(c)-97-k)%26+97) for c in s)
    print(k,d[:30])
