"""Build audit artifacts from the manually read glyph labels, not OCR."""
from pathlib import Path
import json,csv,hashlib,re
from PIL import Image,ImageDraw
W=Path(__file__).resolve().parent; ROOT=W.parents[2]; C=W.parent
key=json.loads((ROOT/'ciphers/hcp-1520/work/key.json').read_text())
(W/'key.json').write_text(json.dumps(key,indent=2)+'\n')
# Four spatial regions. Coordinates are pixels in the indicated cropped upright view.
views={'top':{'source_box':[39,26,978,166],'rotation_clockwise':0},'bottom':{'source_box':[38,507,978,640],'rotation_clockwise':0},'left':{'source_box':[31,167,346,514],'rotation_clockwise':90},'right':{'source_box':[777,208,869,500],'rotation_clockwise':90}}
lines={
'T':[
'y5 n4 m5f1c83fm5 84d3, q5 c5 t3cd683 n5n2 t3b4c2 d6g3f5r3 f1g86t2! Hd58 yc5n t3b4c',
'bh5bc6d4, b3m5f6tq 3p6f68 yc5n c5, q5 p2t5 m5cbh6fm5 4md5hbh5d3f6m. p3r2q58 m5qp1-',
'f683 n4 y4q g d3n2 s6c2. - y5 n4 f6cd5 84d3, q5 6m2mg6 b3g86t6 nm5 q6 cH3bm6,',
'6p1H f5t3n5 2h6q58 t4fg2 f2p5s 6 {U1} t4fg2, gd5h3 c4 m6t5 fc5 f6q4n, gd5h6',
'y5 n4 m6t5 fc5 th6r6 6 gd5h32 qp3qm2y4. bh6f5 bh3d3, b3m5f6tq d5 n6n m5f1c83fm5',
],
'B':[
'h6t 6 b3m5f6tq c5 3 d5p5 p3y4n, bc68 yc5n c83f6 d6 6 d3 cm6t d4n cb4c5, b3m5f6tq',
'qm6n f38m5 m6q3h1 n3t5hm4H b6m2 3 b3n5h2 g t6n6n. {A2}d58 yc5n q6c86d4 m3f1 t3b4c',
'6fc6g n1c84n, y584g3q bc6m5 c83f3 t3b32cd4 d6g h2qm5r3 f1g86t2, q5 p2t5 85b5 b3m5H6d4',
'h3qbh6f2 d2 6q g 3c3pm4n2 c5dg6m4, 6c p2t5-84 c5 Hd4d4 m1m4 6m2mg6 y5cd5',
'c5 nm32 c5y4d4.',
],
'L':[
'q5 2t5868 b6m ph6dh c f1p3h-',
'm1n bh3cb5H5n n6d2h4d2',
'nm5 m5y5m3n p6f483, m1phq',
'4 d5c483. bh5y4 cf5n2 y5t4-',
'm5n2 cht5sg2, 6p1 c3 3',
'b85c2 t3ph5 p6f483. d5c483',
'p1 nm5 f584s5, gt1p1 bh4',
'd3n m5q6b3nm583 2b8m5 m6',
'cf5r3 q6{A1}n32s5m5r3 b.,',
'gd5h1 n2 b3c486 fh5832 2bh4nm32',
'b2c2.',
],
'R':[
'rm5f6c c5 m6 nm5 3bh6ft2',
'6m4sg3 n6? y5 n4 f584s5',
'cn2dm3 f t2c4!',
]}
ys={'T':[(1,31),(24,59),(48,85),(71,113),(96,138)],'B':[(0,33),(24,61),(49,86),(75,114),(101,132)],'L':[(0,34),(29,62),(61,92),(89,124),(119,154),(147,185),(178,215),(206,246),(235,275),(264,303),(286,315)],'R':[(0,36),(26,67),(55,92)]}
region={'T':'top','B':'bottom','L':'left','R':'right'}
unknowns={'U1':{'kind':'unknown_length_region','plain':'[UNK:U1]','description':'Heavily retraced word between A and DIVKU. No exact glyph count or cancellation inferred.'},'A1':{'kind':'bounded_alternative','candidates':['h','r'],'plain':'[R|H]','description':'Third glyph of q6…n32s5m5r3: heavy overink; h/R or r/H.'},'A2':{'kind':'bounded_alternative','candidates':['r','H'],'plain':'[H|CH]','description':'Opening shape of …d58; plain h versus ch, ownership of cap/mark uncertain.'}}
rows=[];source=Image.open(C/'source/picture.jpg')
for p in 'TBLR':
 v=region[p];spec=views[v];im=source.crop(spec['source_box']).rotate(-spec['rotation_clockwise'],expand=True);im.save(W/(v+'-view.png'));canvas=im.copy();d=ImageDraw.Draw(canvas)
 for i,(line,(y0,y1)) in enumerate(zip(lines[p],ys[p]),1):
  row={'id':f'{p}{i:02d}','view':v,'box':[0,y0,im.width,y1],'cipher':line};rows.append(row)
  box=row['box'];im.crop(box).resize((im.width*4,(y1-y0)*4)).save(W/(row['id']+'.png'))
  d.rectangle(box,outline='red');d.text((0,y0),row['id'],fill='blue')
 canvas.resize((canvas.width*3,canvas.height*3)).save(W/(v+'-indexed.png'))
record={'manual':True,'label_convention':'fixed family shapes, not printed ciphertext; braces identify uncertain regions','views':views,'uncertainties':unknowns,'rows':rows}
(W/'transcription.json').write_text(json.dumps(record,indent=2)+'\n')
token=re.compile(r'\{(U1|A1|A2)\}|(.)',re.S)
def dec(s):
 return ''.join(unknowns[m[1]]['plain'] if m[1] else key.get(m[2],m[2]).upper() for m in token.finditer(s))
text='\n'.join(dec(r['cipher']) for r in rows)+'\n';(W/'literal.txt').write_text(text)
with (W/'indexed.csv').open('w') as f:
 out=csv.writer(f);out.writerow(['record_index','row','row_token_position','kind','glyph_or_region','plain']);n=0
 for r in rows:
  j=0
  for m in token.finditer(r['cipher']):
   if m[1] or m[2] in key:
    j+=1;n+=1;label=m[1] or m[2];kind=unknowns[label]['kind'] if m[1] else 'known';out.writerow([n,r['id'],j,kind,label,unknowns[label]['plain'] if m[1] else key[label].upper()])
paths=[C/'source/picture.jpg',C/'source/address.jpg',C/'source/metadata.md',W/'key.json',W/'transcription.json',W/'literal.txt',W/'indexed.csv',ROOT/'ciphers/hcp-1520/work/key.json',ROOT/'batches/easy-2026-10-28/published-anna-ticha-key.txt',ROOT/'batches/easy-2026-10-28/public-reference-199/picture.jpg',ROOT/'batches/easy-2026-10-28/public-reference-199/provenance.json',W/'source-control-boxes.json',W/'A3-A4-source-controls.png',W/'A1-source-controls.png']
(W/'integrity.json').write_text(json.dumps({str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},indent=2)+'\n')
print(text)
