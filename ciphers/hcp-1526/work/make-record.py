#!/usr/bin/env python3
"""Explicitly mutating artifact generator. Not part of read-only reproduction."""
import json,hashlib
from pathlib import Path
p=Path(__file__).resolve().parents[1];w=p/'work'
source_guard=json.loads((w/'source-sha256.json').read_text())
assert set(source_guard)=={'source/picture.jpg','source/address.jpg','source/metadata.md'}
for name,expected in source_guard.items():
 assert hashlib.sha256((p/name).read_bytes()).hexdigest()==expected,(name,'immutable source changed')
key={'1':'Y','2':'U','3':'O','4':'I','5':'E','6':'A','7':'J','8':'L','b':'P','c':'S','d':'T','f':'V','g':'K','h':'R','m':'N','n':'M','p':'B','q':'Z','r':'H','s':'C','t':'D','ř':'CH','v':'F'}
data=[
('fh581 t4g, q86d3 n375, q6 th6r1 84cd5g.',[24,498,635,542]),
('7c5n 3t5 cdh5t1 3b5d f 2h6t5, gt5 75cd',[24,530,635,572]),
('f6m3sm4 c5s3m6 74q f bhm5n bh32t2. n6n',[24,560,635,602]),
('c4s5 75cd5 dh3ř2 h1n2, 6fc6g t32v6n, q5 7c5n',[24,590,635,631]),
('řh4bg2 74q bh5n3r8. fqb3n4m6n fc6g m6',[24,620,635,662]),
('cf5 sht5sg3, gt5h5 m1m4 q6s5 n4cd3',[24,648,635,691]),
('nm5 řh4bg6 dh6b4. m6ř86t486 c5 p5qb3ř1p1',[24,679,635,723]),
('p5r5n 74qt1 b3 th6q5. n2c4 c5 n5 cht5sg3',[24,709,635,753]),
('r3tm5 c5dh4t4, 76g3 nm5 t3 n6 6mt284sg6',[24,739,635,783]),
('c6n6 d6g t2dg84f6 h6t486. bh3c4n 74 3 d3.',[24,770,635,814]),
('d6q5 c5, qt6 7c5n m6 m4 fqb3n4m68, gt1q',[24,800,635,844]),
('nm5 r86f6 p38586. q674cd5, th6r32cg2,',[24,830,635,875]),
('fqt4d 7c5n p18 d5n5h cd685 c6n. fqb3n4m68',[24,865,635,910]),
('7c5n nm3r3 6 fh585. d4c4s t832r1ř, f6cm4f1ř',[24,897,635,939]),
('b2c b3c486 d4 df27 b5b32c, gt5h1 c5 f584s5',[24,927,635,971]),
('d5c4 m6 c84p5m5 bc6mg3.',[24,957,635,989]),
]
# Correct row boxes after measuring source coordinates, see make-controls.py.
rows=[]
for i,(s,box) in enumerate(data,1):
 out=''.join(key.get(c,c) for c in s)
 rows.append(dict(id=f'R{i:02}',bbox=box,cipher=s,plaintext=out,active_units=sum(c in key for c in s)))
(w/'key.json').write_text(json.dumps(key,indent=2,ensure_ascii=False)+'\n')
record={'coordinate_system':'upright.png = source/picture.jpg lossless ROTATE_90 (counterclockwise), 674 by 1024. Row rectangles [left,top,right,bottom] refer to that image. The first six physical rows cross a large blank/illustration gap; read each left fragment then its right continuation, never the whole left column first. Unit indices are row-local, not individual pixel coordinates. Spaces and punctuation manual.','rows':rows,'ordinary_text':'Picture-side handwritten 12./XII.1903. Address-side ordinary cursive to Anna Ticha, teacher in Zirovnice near Pocatky. Neither date nor address is included in cipher count.','excluded_ink':[]}
(w/'transcription.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
(w/'transcription.txt').write_text('\n'.join(r['cipher'] for r in rows)+'\n')
(w/'transcript.txt').write_text('\n'.join(r['plaintext'] for r in rows)+'\n')
positions=[];global_position=0
for r in rows:
 row_index=0
 for column,c in enumerate(r['cipher'],1):
  if c in key:
   global_position+=1;row_index+=1
   positions.append(dict(position=global_position,row=r['id'],index=row_index,column=column,label=c,base=key[c]))
(w/'positions.json').write_text(json.dumps(positions,indent=2,ensure_ascii=False)+'\n')
# Source hash pins are read and checked above, never rebaselined here.
print('\n'.join(r['id']+' '+r['plaintext'] for r in rows));print(len(positions),'units',sum(len(x['base']) for x in positions),'letters')
