import sys
lines = ["Nz Pxo Efbsftu J bn","hmbe uifsf jt pof","npsf mfuufs gps","nf uijt xffl","gspn zpvs pxo","Hjsm","Ivssbi"]
n=0
for l in lines:
    out=''.join(chr((ord(c.lower())-98)%26+97) if c.isalpha() else c for c in l)
    n+=sum(c.isalpha() for c in l); print(l,'->',out.upper())
print('letters',n)
