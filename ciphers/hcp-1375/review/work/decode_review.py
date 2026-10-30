# independent: own transcription (typed from review crops), letter arithmetic only
rows=["Nz Pxo Cpz","J xbt pvu gps","b mjuumf tqjo","uijt bgufsoppo","Nz gspn","Zpvs Pxo Hjsm"]
n=0
for r in rows:
    o=''
    for c in r:
        if c.isalpha():
            b=65 if c.isupper() else 97
            o+=chr((ord(c)-b-1)%26+b); n+=1
        else:o+=c
    print(r,'->',o)
print(n)
from collections import Counter
print(Counter(c.lower() for r in rows for c in r if c.isalpha()).most_common())
