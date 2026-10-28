#!/usr/bin/env python3
"""Explicitly regenerate manual record, positional index and source-pixel crops."""
from pathlib import Path
import json,hashlib,csv
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1]; W=R/'work'
key=json.loads((R.parent/'hcp-1527/work/key.json').read_text())
raw=[
('A01',[42,615,250,649],'fh5832 c32cdh6cd,'),
('A02',[42,640,250,680],'t2c4sg3 n375 75t4m6,'),
('A03',[42,667,250,711],'f q6hn2dg2, 75mq'),
('A04',[42,695,250,738],'m6 d5p5 t385r8.'),
('A05',[42,723,250,764],'s4d4n 2bh4nm5'),
('A06',[42,750,250,792],'c5 cht5sg5n cf1n.'),
('A07',[42,780,250,823],'6fc6g p2t, 6m2mg3,'),
('A08',[42,808,250,852],'g84tm6, fqt4d b6m'),
('A09',[42,837,250,881],'ph6dh 75 n86t 6 q6-'),
('A10',[42,865,250,904],'74cd5 ř3h3p2'),
('A11',[42,892,255,930],'f4d5qm5 bh5n2q5.'),
('B01',[437,625,635,669],'gt1 bh475t5'),
('B02',[437,656,635,700],'c85sm6 t3 q4-'),
('B03',[437,685,635,734],'h3fm4s5? d4c4s'),
('B04',[437,716,635,764],'fh581ř 2bh4nm1ř'),
('B05',[437,747,635,794],'b2c 3t b5b32c5,'),
('B06',[437,777,635,823],'gd5h1 f n1c85m-'),
('B07',[437,807,635,853],'g6ř cd685 t84 2'),
('B08',[437,837,635,874],'d5p5.')]
record={'method':'Manual visual transcription from immutable source/picture.jpg, upright lossless ROTATE_270 (90 degrees clockwise), 674x1024 pixels. Known-family key transfer. Whole-row boxes may overlap at ascenders and descenders; ordinal indices do not claim individual character pixel boxes.','rows':[], 'ordinary':['28./X.1903 below right block, ordinary date; date format normalized as 1903-10-28 in portal.','Address side: Velectena Slecna / slecna Anna Ticha / ucitelka v / Zirovnici / u Pocatek. Ordinary cursive, not substitution ciphertext.'],'marks':['Arrow after A11 points up and right toward B01, indicating continuation; not a cipher unit.','A10 special CH glyph and B04 both CH glyphs and B07 CH glyph include a caron-like top mark as part of the neutral shape label ř.','No canceled or isolated marginal cipher unit identified on either side.']}
positions=[];total=0
for rid,box,s in raw:
 text=''.join(key.get(c,c) for c in s);active=sum(c in key for c in s)
 row={'id':rid,'box_upright_xyxy':box,'cipher':s,'plaintext':text,'active_units':active}; record['rows'].append(row)
 idx=0
 for c in s:
  if c in key:
   total+=1;idx+=1;positions.append([total,rid,idx,c,key[c]])
for filename,value in [('key.json',key),('transcription.json',record)]:
 (W/filename).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
with (W/'positions.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['global_position','row','row_position','shape_label','base_plaintext']);w.writerows(positions)
for filename,paths in [('source-sha256.json',sorted((R/'source').iterdir())),('record-sha256.json',[W/'key.json',W/'transcription.json',W/'positions.csv'])]:
 value={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths if p.is_file()}
 (W/filename).write_text(json.dumps(value,indent=2)+'\n')
im=Image.open(R/'source/picture.jpg').transpose(Image.Transpose.ROTATE_270);im.save(W/'upright.png')
indexed=im.copy();d=ImageDraw.Draw(indexed)
for row in record['rows']:
 b=row['box_upright_xyxy'];d.rectangle(b,outline='red',width=1);d.text((max(0,b[0]-28),b[1]),row['id'],fill='red')
 im.crop(b).resize(((b[2]-b[0])*4,(b[3]-b[1])*4)).save(W/(row['id']+'.png'))
indexed.save(W/'indexed.png')
for row in record['rows']:print(row['id'],row['active_units'],row['plaintext'])
print('units',total,'CH',sum(s.count('ř') for _,_,s in raw),'letters',sum(len(key[c]) for _,_,s in raw for c in s if c in key))
