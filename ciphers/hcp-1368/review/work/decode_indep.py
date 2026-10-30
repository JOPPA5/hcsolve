# Independent re-keying of the reviewer's own pixel reading; no import of solver files.
import datetime, collections
R="Nz Pxo Cpz qptu dbset up Ebz wfsz ojdf t zpvs Pxo Hjsm".split()
def sh(w,k): return ''.join(chr((ord(c.lower())-97-k)%26+65) for c in w)
print(' '.join(sh(w,1) for w in R), sum(map(len,R)))
V=set("MY OWN BOY POST CARDS CARD TO DAY VERY NICE YOUR GIRL A I S".split())
for k in range(26):
    d=[sh(w,k) for w in R]; print(k,sum(x in V for x in d),' '.join(d))
print(datetime.date(1907,7,26).strftime('%A'))
