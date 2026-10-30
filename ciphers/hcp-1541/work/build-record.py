#!/usr/bin/env python3
"""Mutating working-record builder from explicitly manual transcription; not OCR."""
import hashlib,json,re
from pathlib import Path
from PIL import Image
W=Path(__file__).resolve().parent;C=W.parent;R=C.parent.parent
key=json.loads((R/'ciphers/hcp-1520/work/key.json').read_text())
rows=[
('P01',(40,47,646,87),'fh581 t4g, r382p4sg3 n3y5, q6 th6r1 84cd5g, y5mq'),
('P02',(40,77,646,117),'c5 c m4n gh4q3f68. t3cd686 yc4 y5cd5 n2y 84cd5g'),
('P03',(40,106,646,148),'f rh6ts4? - d5c4 nm5, q5 y5 cht5sg3 n3y5 3b5d qth6-'),
('P04',(40,136,646,178),'f3 y6g3 t4p84g. n58 yc5n f58g32 cd6h3cd. fqb3-'),
('P05',(40,165,646,210),'n4m6n, q86d3 n3y5, cd685. Hd58 yc5n m6cd32b4d4'),
('P06',(40,195,646,239),'t3f385m32 cf3y4 g3ms5n d3r3d3 n5c4s5, 6p1H'),
('P07',(40,225,646,268),'c5 n3r8 b3t4f6d4 y5cd5 t3 2cd5sg5 b6n5dm4'),
('P08',(40,255,646,300),'gm4r1 t5g6mcg5, 6fc6g qr6d48 c5 n2y b86m.'),
('P09',(40,286,646,331),'m6c fhHm4 cbh6f5s, gd5h1 m5Hd58 y4d4 m6 t3f385-'),
('P10',(40,316,646,360),'m32, m6cd32b4 y4 m6c85tg5n H3h3p1 cf5r3'),
('P11',(213,346,646,390),'cf6[U01]h6, gd5h5r3 p2t5 bh3f6q5d4'),
('P12',(213,376,646,420),'t3 86qm4, bh5cd3 q4dh6, m6c85t-'),
('P13',(213,406,646,450),'g5n s5r3q n2c4n 3t83q4d4 y6'),
('P14',(213,436,646,480),'cf3y4 t3f385m32 6q m6 th2r1'),
('P15',(213,466,646,510),'n5c4s. d4c4s t832r1H, fh581H'),
('P16',(213,496,646,541),'b2c b3c486 d4 f5sm[U02]df2y'),
('P17',(213,526,646,571),'b5b32c, gd5h1 c5 [U03] m6'),
('P18',(213,556,646,601),'3b5dm32 phqg32 qbh6f2'),
('P19',(213,586,646,640),'3t cf5r3 cht5sg6.'),
]
unknowns={
'U01':{'kind':'bounded_glyph','normalized_cipher_class':'K','source':'picture.jpg','upright_bbox':[277,347,304,386],'reason':'Distinct k-like class absent from supplied family key. Single visible glyph. G in SVAGRA is linguistic conjecture, not assigned key.','literal':'[U01]'},
'U02':{'kind':'unknown_length_span','source':'picture.jpg','upright_bbox':[431,495,566,542],'reason':'Dark painted tree obscures writing after F5SM and before visible DF2Y. Glyph count unknown.','literal':'[U02]'},
'U03':{'kind':'unknown_length_span','source':'picture.jpg','upright_bbox':[440,528,554,571],'reason':'Dark painted tree obscures writing after C5 and before clear final M6. Glyph count unknown.','literal':'[U03]'},
}
pat=re.compile(r'\[U\d+\]|.')
glyphs=[];record=[];spans=[]
for rid,box,raw in rows:
 rt=[];rg=[];literal=[]
 for ti,m in enumerate(pat.finditer(raw),1):
  c=m.group();uid=c[1:-1] if c.startswith('[U') else None
  if uid: p=c;kind=unknowns[uid]['kind']
  elif c in key:p=key[c];kind='read'
  else:assert c in ' .,!?-';p=c;kind='separator'
  tok={'index':ti,'raw_start':m.start(),'raw_end':m.end(),'cipher':c,'plaintext':p,'kind':kind,'glyph_index':None}
  if kind in ('read','bounded_glyph'):
   g={'index':len(glyphs)+1,'row':rid,'row_glyph':len(rg)+1,'token_index':ti,'raw_char_offset':m.start(),'cipher':c,'plaintext':p,'status':kind}
   if uid:g.update(unknowns[uid]);g['unknown_id']=uid
   glyphs.append(g);rg.append(g);tok['glyph_index']=g['index']
  elif kind=='unknown_length_span':
   span={'id':uid,'row':rid,'token_index':ti,'raw_char_offset':m.start(),'preceding_global_glyph':len(glyphs),**unknowns[uid]};spans.append(span)
  rt.append(tok);literal.append(p)
 record.append({'id':rid,'source':'picture.jpg','orientation':'90 degrees clockwise from original','upright_bbox':list(box),'crop':f'row{int(rid[1:]):02d}.png','transcription':raw,'literal':''.join(literal),'first_glyph':rg[0]['index'],'last_glyph':rg[-1]['index'],'glyphs':rg,'tokens':rt})
inv={'description':'Manual visual record, no OCR. Unknown-length dark spans have no invented glyph count. Glyph indices count 1 visible unassigned glyph U01 but do not count U02/U03 as glyphs. Indexing describes manual record, not automatic pixel segmentation.','rows':record,'glyphs':glyphs,'unknowns':unknowns,'unknown_length_spans':spans,'canceled_ink':[]}
for name,obj in [('key.json',key),('inventory.json',inv)]: (W/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
(W/'transcription.txt').write_text('\n'.join(r[2] for r in rows)+'\n')
(W/'literal-czech.txt').write_text('\n'.join(r['literal'] for r in record)+'\n')
im=Image.open(C/'source/picture.jpg').rotate(-90,expand=True);im.save(W/'upright.png')
for row in record:
 a=im.crop(row['upright_bbox']);a.resize((a.width*3,a.height*3)).save(W/row['crop'])
Image.open(C/'source/address.jpg').resize((2048,1348)).save(W/'address-control.png')
refs=['ciphers/hcp-1520/work/key.json','batches/easy-2026-10-28/published-anna-ticha-key.txt','batches/easy-2026-10-28/public-reference-199/picture.jpg','batches/easy-2026-10-28/public-reference-199/provenance.json']
paths=[*sorted((C/'source').iterdir()),*[R/x for x in refs],*[W/x for x in ['key.json','inventory.json','transcription.txt','literal-czech.txt']]]
hashes={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths if p.is_file()}
(W/'audit-sha256.json').write_text(json.dumps(hashes,indent=2)+'\n')
print(len(glyphs),'visible indexed units; 1unassigned class; 2unknown-length spans')
print((W/'literal-czech.txt').read_text())
