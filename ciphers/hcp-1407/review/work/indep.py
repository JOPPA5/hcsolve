import datetime
# reviewer's own transcription from enlarged crops (review/work/r*.png, z_*.png)
lines=["Nz Pxo Efbsftu","Nboz uibolt gps","dbse up-Ebz","gspn zpvs","Pxo Hjsm"]
dec=lambda s:''.join(chr((ord(c.upper())-65-1)%26+65) if c.isalpha() else c for c in s)
n=0
for l in lines:
    n+=sum(c.isalpha() for c in l); print(l,'->',dec(l))
print('letters',n)
print('1907-05-14 weekday',datetime.date(1907,5,14).strftime('%A'))
for s in ["M & L","N 1","M 1"]: print(s,'-> shifted',dec(s))
