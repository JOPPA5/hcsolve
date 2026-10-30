# independent: my own transcription typed from flat.png, byte-wise Caesar, compared with solver's
import json,re
mine="Nz Efbsftu J bn wfsz Tpssz bcpvu ofxt Jo dpef & ipqf Zpv xjmm ublf hsfbu dbsf Cz wfsz tqfdjbm Sfrvftu Zpvs pxo mpwjoh Hjsm"
dec=lambda s:''.join(chr((ord(c.upper())-65-1)%26+65) if c.isalpha() else c for c in s)
print(dec(mine)); print(sum(c.isalpha() for c in mine),'letters')
sol=json.load(open('work/transcription.json'))['lines']
s=re.sub(r'\{.*?\}','&',' '.join(sol)).replace('.','').replace('"','')
a=mine.split();b=s.split();print(len(a),len(b),[(x,y) for x,y in zip(a,b) if x!=y])
from collections import Counter
print(sorted(Counter(c for c in s if c.islower()).items()))
for k in range(26):
    pass
