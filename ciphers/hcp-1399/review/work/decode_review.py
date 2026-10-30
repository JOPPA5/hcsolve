# Independent reviewer decoder for HCP1399 (own transcription from review/work/r_*.png)
lines = ["Nz Pxo", "Nboz uibolt", "gps Txffut", "uijt npsojoh", "gspn", "Zpvs Pxo"]
def sh(s, k): return ''.join(chr((ord(c.upper())-65+k)%26+65) if c.isalpha() else c for c in s)
n = sum(c.isalpha() for l in lines for c in l)
for k in range(26):
    out = ' / '.join(sh(l, -k) for l in lines)
    if k in (1,) or 'THE' in out: print(k, out)
print('letters', n)
for g in ["E.h.", "N & Lt", "N. & L."]: print(g, '->', sh(g, -1))
import datetime; print(datetime.date(1908,2,2).strftime('%A'))
