#!/usr/bin/env python3
"""Independent Caesar -1 check of the reviewer's own transcription of hcp-1366 (typed from crops, not from transcription.json)."""
rows=["Nz Pxo Mpwfs Cpz","Op ujnf up","Tfoe Mfuufs","Mpwf & Lt..","Gspn Zpvs Pxo","N. h. Hjsm"]
def d(c): 
    if c.isalpha():
        b=65 if c.isupper() else 97
        return chr((ord(c)-b-1)%26+b)
    return c
n=0
for r in rows:
    print(r,'->',''.join(d(c) for c in r).upper()); n+=sum(c.isalpha() for c in r)
lit=4
print('letters',n,'of which kept-literal groups',lit,'decoded',n-lit)
# shift sweep on the secure body, showing -1 is the unique English shift
body="Op ujnf up Tfoe Mfuufs Gspn Zpvs Pxo Hjsm"
for k in range(26):
    print(k,''.join(chr((ord(c.lower())-97-k)%26+97) if c.isalpha() else c for c in body))
