# independent: my own reading typed from my crops, not imported from solver files
rows=["Nz Pxo Cpz","J bn hpjoh up","uif Njotufs","Tvoebz Ojhiu","Opu bmpof","Zpvs Pxo Hjsm"]
def sh(t,k): return ''.join(chr((ord(c.upper())-65-k)%26+65) if c.isalpha() else c for c in t)
for k in range(26):
    print(k,' / '.join(sh(r,k) for r in rows))
import datetime;print(datetime.date(1907,8,9).strftime('%A'), datetime.date(1907,8,11).strftime('%A'))
t=''.join(rows).replace(' ','');print(len(t))
