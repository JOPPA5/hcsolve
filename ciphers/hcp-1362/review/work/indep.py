# independent decoder: reviewer's own transcription, typed from review crops (not read from work/transcription.json)
T="Nz Efbsftu J ibwf / pof Mjlf uijt / Mpwf boe Ljttft / gspn Zpvs pxo / Hjsm"
def sh(c,k):
    if c.isupper(): return chr((ord(c)-65-k)%26+65)
    if c.islower(): return chr((ord(c)-97-k)%26+65)
    return c
print(''.join(sh(c,1) for c in T))
print('letters',sum(c.isalpha() for c in T), 'distinct cipher', len(set(T.lower())-set(' /')))
for k in range(26):
    print(k,''.join(sh(c,k) for c in T))
import datetime
for y in (1906,1907,1908,1909): print(y,datetime.date(y,4,10).strftime('%A'))
