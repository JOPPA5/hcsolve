import json,re,sys
rows=["Nz Pxo Efbsftu","J bn bcpvu uif","Foe pg uijt","tupdl","Gspn Zpvs Pxo","Hjsm"]
for r in rows:
    print(r,'=>',''.join(chr((ord(c.upper())-65-1)%26+65) if c.isalpha() else c for c in r))
print(sum(c.isalpha() for r in rows for c in r))
