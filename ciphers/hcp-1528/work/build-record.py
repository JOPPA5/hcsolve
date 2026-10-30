#!/usr/bin/env python3
"""Build a deliberately partial indexed manual transcription, never OCR or fill."""
from pathlib import Path
import json,hashlib,csv
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1];W=R/'work'
key={'1':'Y','2':'U','3':'O','4':'I','5':'E','6':'A','7':'J','8':'L','b':'P','c':'S','d':'T','f':'V','g':'K','h':'R','m':'N','n':'M','p':'B','q':'Z','r':'H','s':'C','t':'D','ř':'CH'}
# Shape labels follow supplied family key; editorial word spaces and punctuation.
data=[
 ('fh581 t4g q6 th6r1 84cd5g. b3c85ř8 7c5n cf5 cht5sg3 6 q2cd68 7c5n',(39,39,973,80)),
 ('75cd5 t3n6. 75 n4 74q 3 r3tm5 85b5, 6fc6g t3c2t b84s5 6 ghg2 m5-',(39,77,972,112)),
 ('7c32 2b8m5 f b3h6tg2. f b3mt584 q5bd6n c5 85g6h5, qt6 n4 t3f384',(39,107,972,146)),
 ('74q 74d4 t3 2h6t2. 73 n4 m1m4 m5n3s f5h2c5 m5fr3t. 6p1 n5 cht5sg3',(39,138,974,180)),
 ('cd3m683 g5 nm5, p1ř q6 q6tm32 s5m2 m5řd58. {U7} p18 p1ř c4 fc6g bh68',(33,174,973,211)),
 ('gt1q nm5 d6g r86f6 p38586, 6p1 nm5 {U1} n5 cht5sg3 6cb3m',(39,207,973,244)),
 ('m6 řf484 bh4c83, b383q483 cf32 h2sg2',(39,240,621,278)),
 ('m6 r86f2, {U2} 74cd5 p385cd4',(39,274,550,313)),
 ('bh5cd686. {U3}',(39,307,548,347)),
 ('6 {U4}',(39,339,547,380)),
 ('n5 2sd4f5 {U5}',(39,376,522,414)),
 ('n4 fc6g {U8}5 cf1n q86d2sg3f4',(29,409,516,448)),
 ('84cd5g, 76g1 b3c85tm5, gt5 p1 nm5',(29,441,522,479)),
 ('{U6}6hn32d4c. cht5sm1 b3qth6f6',(29,474,512,512)),
 ('d4c4s t832r1ř, f6cm4f1ř b2c',(29,507,421,545)),
 ('b3c486 d4 df37 b5b32c,',(29,538,405,578)),
 ('gd5h1 cd685 fh585',(29,571,320,608)),
 ('fqb3n4m6.',(29,599,292,626)),
]
unknowns={
'U1':{'box':[609,207,712,240],'count':None,'note':'Tree overlaps the beginning of the word before ME. Right-hand run looks 483 (ILO); no complete word asserted.'},
'U2':{'box':[201,274,352,311],'count':None,'note':'Dark roof/background: beginning may resemble 74cd5 p1 nm5, not included in confirmed inventory.'},
'U3':{'box':[181,307,544,346],'count':None,'note':'Dark roof and foliage, several visible strokes but segmentation and letters not established.'},
'U4':{'box':[77,339,543,380],'count':None,'note':'Mostly roof: apparent words and letters not promoted to confirmed plaintext.'},
'U5':{'box':[199,376,519,414],'count':None,'note':'Dark roof, several ink components visible; full segmentation and exact reading not established.'},
'U7':{'box':[641,175,666,212],'count':1,'note':'Isolated glyph before BYL, initially read 4/I but also resembles 7/J; unresolved after same-card controls.'},
'U8':{'box':[143,410,162,445],'count':1,'note':'Initial glyph of ?E after VSAK, g/K versus q/Z; roof print overlaps the lower tail.'},
'U6':{'box':[39,477,63,504],'count':1,'note':'First glyph in ?ARMOUTIS: g/K versus q/Z, unresolved here; no grammar repair.'}}
rows=[];positions=[];total=0
for i,(cipher,box) in enumerate(data,1):
 # Tokenise placeholders atomically, preserving explicit variable-length gaps.
 import re
 tokens=re.findall(r'\{U\d+\}|.',cipher)
 out=[];idx=0
 for token in tokens:
  if token in key:
   total+=1;idx+=1;positions.append([total,f'R{i:02}',idx,token,key[token]]);out.append(key[token])
  elif token.startswith('{U'):
   out.append('['+token[1:-1]+']')
  else:out.append(token)
 rows.append({'id':f'R{i:02}','box':list(box),'cipher':cipher,'plaintext':''.join(out),'confirmed_units':idx})
record={'claim':'PARTIAL','orientation':'Original source picture upright,1024x674. All 18 ink rows inventoried.','manual_transcription':True,'punctuation_spaces':'Editorial layout; diacritics are not part of key.','rows':rows,'unknown_spans':unknowns,'scope':'Address side ordinary cursive, postmarks and ordinary 5/XII/1903 excluded from cipher units.'}
(W/'key.json').write_text(json.dumps(key,indent=2,ensure_ascii=False)+'\n')
(W/'transcription.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
with (W/'positions.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['confirmed_global_index','row','confirmed_index_in_row','shape_label','base_plaintext']);w.writerows(positions)
(W/'plaintext.txt').write_text('\n'.join(r['plaintext'] for r in rows)+'\n')
manifest={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((R/'source').iterdir()) if p.is_file()}
(W/'source-sha256.json').write_text(json.dumps(manifest,indent=2)+'\n')
manifest={str((W/f).relative_to(R)):hashlib.sha256((W/f).read_bytes()).hexdigest() for f in ['key.json','transcription.json','positions.csv']}
(W/'record-sha256.json').write_text(json.dumps(manifest,indent=2)+'\n')
im=Image.open(R/'source/picture.jpg').convert('RGB');draw=ImageDraw.Draw(im)
for row in rows:
 box=row['box'];draw.rectangle(box,outline='red');draw.text((box[2]-30,box[1]),row['id'],fill='red')
for name,obj in unknowns.items():
 draw.rectangle(obj['box'],outline='blue',width=2);draw.text((obj['box'][0],obj['box'][1]),name,fill='blue')
im.save(W/'indexed-rows.png')
print(total,'confirmed units')
print((W/'plaintext.txt').read_text())
