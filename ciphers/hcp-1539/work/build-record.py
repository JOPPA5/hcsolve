#!/usr/bin/env python3
"""Rebuild derived solver working records from explicit manual row transcription."""
import hashlib,json,re
from pathlib import Path
from PIL import Image
W=Path(__file__).resolve().parent; C=W.parent; R=C.parent.parent
key=json.loads((R/'ciphers/hcp-1520/work/key.json').read_text())
rows=[
('P01',(35,40,652,80),'cht5sm1 t4g q6 tm5cm4 84cd5g, y5mq gh4q3f68'),
('P02',(35,70,652,108),'c n1n. qdh6d481 c3 3bh6ft2 3p6 n5 84cdg1 q5'),
('P03',(35,100,652,138),'tm5 th2r5r3 6 dh5d4r3 d3r3d3 n5c4s5?'),
('P04',(35,130,652,170),'p18 yc5n f1qf6m, 6p1H cb3822s4mg3f68 m6 r32c85'),
('P05',(35,160,652,202),'bh4cd4 n5c4s f5 f6np5hg2, gt5 p2t5 2cb3h6t6m6'),
('P06',(35,190,652,232),'6g6t5n45 m6 b6n6dg2 q5nh585r3 g6b58m4g6'),
('P07',(35,220,652,262),'f1cg3s486, bh4 m4q n6 2s4mg3f6d4 d5q'),
('P08',(35,250,652,293),'b6m4 n6d2h3f6 6 b46m4cdg6 8{3|5}86 p5h6m3f6'),
('P09',(35,280,652,322),'6 ph6dh6m5s f1cg3s48. m5n3r8 yc5n fc6g m4s'),
('P10',(35,310,652,350),'2hs4d5r3 c84p4d4 6 m5ycb4c5,'),
('P11',(35,340,652,380),'q5 c5 m5c2s6cdm4n.'),
('P12',(133,858,649,901),'d4c4s b2c q6c486 d4 b5b32c. f1h4t'),
('P13',(130,889,650,936),'bh3c4n c85sm5 y6mg3f5 n5 b3h2s5m4.'),
]
# A token is one observed cipher glyph or one separator. Alternatives occupy one
# explicit glyph position because the image shows a single bounded character.
# The distinction is never used for an illegible span of unknown length.
pat=re.compile(r'\{[^}]+\}|.')
allglyphs=[]; record=[]
for rid,box,raw in rows:
 glyphs=[]; tokens=[]; plaintext=[]; offset=0
 for ti,m in enumerate(pat.finditer(raw),1):
  token=m.group(); start=m.start()
  if token.startswith('{'):
   choices=token[1:-1].split('|'); decoded='{'+ '|'.join(key[c] for c in choices)+'}'
   glyph={'index':len(allglyphs)+1,'row':rid,'row_glyph':len(glyphs)+1,'token_index':ti,'raw_char_offset':start,'cipher':token,'choices':choices,'plaintext':decoded,'status':'bounded_alternative','image_note':'Second glyph of the four-glyph, tree-overlapped given name 8?86: closed loop read 3/O (preferred, LOLA) or 5/E (LELA). Corrected after review 1.'}
  elif token in key:
   decoded=key[token];glyph={'index':len(allglyphs)+1,'row':rid,'row_glyph':len(glyphs)+1,'token_index':ti,'raw_char_offset':start,'cipher':token,'plaintext':decoded,'status':'read'}
  else:
   assert token in ' .,!?-';decoded=token;glyph=None
  tokens.append({'index':ti,'raw_start':start,'raw_end':m.end(),'cipher':token,'plaintext':decoded,'glyph_index':glyph['index'] if glyph else None})
  plaintext.append(decoded)
  if glyph: glyphs.append(glyph);allglyphs.append(glyph)
 record.append({'id':rid,'source':'picture.jpg','orientation':'90 degrees clockwise from original','upright_bbox':list(box),'crop':f'row{int(rid[1:]):02d}.png','transcription':raw,'literal':''.join(plaintext),'first_glyph':glyphs[0]['index'],'last_glyph':glyphs[-1]['index'],'glyphs':glyphs,'tokens':tokens})
(W/'key.json').write_text(json.dumps(key,ensure_ascii=False,indent=2)+'\n')
(W/'transcription.txt').write_text('\n'.join(r[2] for r in rows)+'\n')
inv={'description':'Manual visual record; no OCR. Row bounds are crop bounds, not per-glyph coordinates. Indices are explicit positions in the manual transcription. One bounded ambiguous glyph (second sign of the given name, row P08); transcription corrected after review 1, no unknown-length spans, no canceled writing identified.','rows':record,'glyphs':allglyphs,'canceled_ink':[],'unknown_length_spans':[]}
(W/'inventory.json').write_text(json.dumps(inv,ensure_ascii=False,indent=2)+'\n')
(W/'literal-czech.txt').write_text('\n'.join(r['literal'] for r in record)+'\n')
im=Image.open(C/'source/picture.jpg').rotate(-90,expand=True)
for row in record:
 box=row['upright_bbox'];a=im.crop(box);a.resize((a.width*3,a.height*3)).save(W/row['crop'])
# Full image and address controls include every border and both sides.
im.save(W/'upright.png')
Image.open(C/'source/address.jpg').resize((2048,1348)).save(W/'address-control.png')
refs=['batches/easy-2026-10-28/published-anna-ticha-key.txt','batches/easy-2026-10-28/public-reference-199/picture.jpg','batches/easy-2026-10-28/public-reference-199/provenance.json','ciphers/hcp-1520/work/key.json']
hashes={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [*sorted((C/'source').iterdir()),*[R/x for x in refs],W/'key.json',W/'transcription.txt',W/'inventory.json',W/'literal-czech.txt'] if p.is_file()}
(W/'audit-sha256.json').write_text(json.dumps(hashes,indent=2)+'\n')
print(len(allglyphs),'glyphs;',len(record),'rows')
print((W/'literal-czech.txt').read_text())
