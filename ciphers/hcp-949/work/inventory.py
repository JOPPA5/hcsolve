"""Provisional visual inventory. No solved reading. Coordinates in rotated crop.
Crop = address.jpg (10,12,475,610), then rotate90CCW; size598x465.
A slash-like detached stroke may be its own symbol or modifier: kept separate.
"""
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent
rows=[
 ('upper',[(32,4,'I'),(40,24,'TR.'),(59,24,'BR'),(80,24,'up.'),(102,24,'TL'),(124,24,'TBL.'),(151,3,'I'),(157,24,'up.'),(179,24,'down.'),
 (222,37,'box.'),(244,39,'box.'),(276,40,'TR'),(302,39,'TL.'),(335,39,'up'),(355,40,'TBR.'),(380,41,'box.'),(402,41,'BR.'),(425,42,'up.'),(450,43,'TBR.'),(476,43,'TBR.'),(502,43,'TL'),(524,41,'up'),(545,42,'up.'),(570,42,'TBL')]),
 ('second',[(310,79,'TBL.'),(336,79,'TLR'),(361,79,'box'),(391,79,'TLR.'),(413,60,'I'),(420,79,'up.'),(447,79,'TLR.'),(470,79,'up'),(494,79,'BR.'),(522,79,'TL'),(552,79,'TBL.')]),
 ('margin',[(21,58,'LBR'),(22,88,'TL'),(21,123,'down.'),(22,152,'left.'),(19,184,'TR.')]),
]
records=[]
for row,items in rows:
 for i,(x,y,t) in enumerate(items,1):records.append(dict(id=f'{row}.{i:02}',crop_xy=[x,y],original_xy=[475-y,12+x],shape=t))
print('Provisional graphic units',len(records),'including 3 detached strokes and 2 overprinted boxes')
for row,items in rows:print(row, ' '.join(t for x,y,t in items))
sha={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((P.parent/'source').iterdir()) if p.is_file()}
for n,h in sha.items():print('SHA256',n,h)
if '--write' in __import__('sys').argv:
 (P/'inventory.json').write_text(json.dumps(dict(status='PROVISIONAL; no accepted plaintext',coordinate_system=__doc__,source_sha256=sha,records=records),indent=2)+'\n')
 # Arbitrary labels for unseeded MASC discovery only. Margin held out.
 shapes=list(dict.fromkeys(t for row,items in rows[:2] for x,y,t in items));mapping={s:chr(97+i) for i,s in enumerate(shapes)}
 s=''.join(mapping[t] for row,items in rows[:2] for x,y,t in items)
 (P/'draft-cipher.txt').write_text(s+'\n');(P/'draft-reversed.txt').write_text(s[::-1]+'\n')
 (P/'draft-labels.json').write_text(json.dumps(mapping,indent=2)+'\n')
