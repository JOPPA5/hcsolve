from pathlib import Path
from PIL import Image
import json,hashlib
W=Path(__file__).resolve().parent;R=W.parents[2];C=W.parent
key={'1':'y','2':'u','3':'o','4':'i','5':'e','6':'a','8':'l','b':'p','c':'s','d':'t','f':'v','g':'k','h':'r','m':'n','n':'m','p':'b','q':'z','r':'h','s':'c','t':'d','y':'j','7':'j','H':'ch'}
# Entirely manual visual classification. U+FFFC is an unknown-length obscured span,
# never one inferred glyph; marks and punctuation are separately typed tokens.
rows=[
('B01','cht5sm1 t4g q6 fqb3n4mg2 q s4qg3f6. bh6f4c q5',(40,682,641,722)),
('B02','s581 d4t5m n6hm5 s5g6c m6 n27 84cd5g. 3t5c868',(40,714,641,749)),
('B03','7c5n f 2d5h1 (I.) ￼m5t b3 m6fh6d2 cf3n q 2cd4',(40,743,641,781)),
('B04','84cd5g 2cd5sg1 6 f5 cdh5t2 (II.) 84cd5g qf￼d4-',(40,773,641,810)),
('B05','m3f1. cb4c5 c5 n4 qt6, q5 6m2mg2 f bh6qtm4-',(40,805,641,842)),
('B06','m6H m6 nm5 q6b3n4m6. d5c48 7c5n c5, q5 t3-',(40,836,641,873)),
('B07','cd6m2 f bh6qtm4m6r 6cb3m y5tm3 bc6m4s3.',(40,866,641,904)),
('B08','gt1 m6cd32b4n t3f385m32, t3c2t m5n3r2 h4s4,',(40,897,641,936)),
('B09','m5ycb4c5 rm5t b3 m6fh6d2 fhHm4r3 cbh6fs5.',(40,928,641,964)),
('B10','￼5sm1 b3qth6f 6 2bh4nm32 b2c2 q6c486 b5b32c.',(40,958,641,992)),
('M01','y6g cd3y4 df3y5 q685q4d3cd 3r85tm5 n4cd6',(30,43,647,125)),
('M02','b3 bh6qtm4m6H? 9./IX.1903.',(30,43,647,125)),
]
records=[]
for rid,raw,box in rows:
 ts=[];i=0;slot=0
 while i<len(raw):
  ch=raw[i]
  if ch.isspace():ts.append({'type':'space','text':ch});i+=1;continue
  if raw[i:i+4]=='(II)':raise Exception('unexpected')
  if raw.startswith('(I.)',i) or raw.startswith('(II.)',i):
   v='(II.)' if raw.startswith('(II.)',i) else '(I.)';ts.append({'type':'literal','text':v});i+=len(v);continue
  if rid=='M02' and raw[i:].startswith('9./IX.1903.'):
   ts.append({'type':'literal','text':'9./IX.1903.'});break
  slot+=1;p=f'{rid}.{slot:03d}'
  if ch=='￼':ts.append({'type':'unknown_span','id':p,'length':None,'text':'⟦unknown length⟧','reason':'heavy superposed/overwritten ink; no glyph count inferred'})
  elif ch in key:ts.append({'type':'glyph','id':p,'glyph':ch,'plain':key[ch]})
  else:ts.append({'type':'punctuation','id':p,'text':ch})
  i+=1
 records.append({'id':rid,'manual_glyphs':raw.replace('￼','⟦unknown length⟧'),'crop_upright_xyxy':box,'tokens':ts})
address=[('A01','Velectěná Slečna',(224,285,573,344)),('A02','slečna Anna Tichá',(254,350,725,421)),('A03','učitelka t. č.',(438,418,631,452)),('A04','v Pelhřimově.',(482,452,870,518)),('A05','Vlastnoručně',(93,473,323,520)),('A06','dodati.',(105,516,295,565))]
for rid,text,box in address:
 ts=[{'type':'plain_handwriting','id':f'{rid}.{i:03d}','text':ch} for i,ch in enumerate(text,1)]
 records.append({'id':rid,'manual_glyphs':text,'crop_address_xyxy':box,'tokens':ts})
source={}
for p in [C/'source/picture.jpg',C/'source/address.jpg',C/'source/metadata.md',R/'batches/easy-2026-10-28/published-anna-ticha-key.txt',R/'batches/easy-2026-10-28/public-reference-199/picture.jpg',R/'batches/easy-2026-10-28/public-reference-199/provenance.json']:
 source[str(p.relative_to(R))]=hashlib.sha256(p.read_bytes()).hexdigest()
rec={'status':'partial manual known-key transfer; no independent review','key':key,'hashes':source,'unknown_length_spans':3,'rows':records,'overlay_marks':[{'id':'OVAL','scope':'B03-B10','description':'large thick oval/loop superposed across text; not a cipher glyph, possible annotation/cancellation intention unknown'},{'id':'ARROW','scope':'right of B10','description':'arrow points from body toward inverted margin continuation; ordinary graphic mark'}],'canceled_cipher_units':[],'cancellation_note':'No legible canceled cipher sequence confidently separable from overlay; obscured extents remain unknown.'}
(W/'record.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
(W/'key.json').write_text(json.dumps(key,indent=2)+'\n')
print('record created')
