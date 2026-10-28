#!/usr/bin/env python3
"""Initial authored manual records; does not perform OCR or discover the key."""
from pathlib import Path
import json, hashlib
W=Path(__file__).resolve().parent
key={'1':'y','2':'u','3':'o','4':'i','5':'e','6':'a','8':'l','b':'p','c':'s','d':'t','f':'v','g':'k','h':'r','m':'n','n':'m','p':'b','q':'z','r':'h','s':'c','t':'d','y':'j','H':'ch','F':'f'}
rows=[
('cht5sm1 t4g q6 th6r1','srdecny dik za drahy'),
('84cd5g. n1c848 yc5n','listek. myslil jsem'),
('y4q, q5 yc4 2b8m5','jiz, ze jsi uplne'),
('m6 nm5 q6b3nm586.','na mne zapomnela.'),
('gt1 q6s4m684 ycd5','kdy zacinali jste'),
('m3f1 cg38m4 h3g?','novy skolni rok?'),
('f g86cd5h5 q6s4m68 h3g 6c4','v klastere zacinal rok asi'),
('tm5c. m5bh4yt5-84 m4s m53s5-','dnes. neprijde-li nic neoce-'),
('g6f6m5r3 t3 d3r3, b3y5t2 6c4 g3m-','kavaneho do toho, pojedu asi kon-'),
('s5n bh4cd4r3 d1tm5 m6 t3f385m32.','cem pristiho tydne na dovolenou.'),
('2s4mg3f6m4 bh4 f5s4hg2 f5 f6np5hs5 yc5n','ucinkovani pri vecirku ve vamberce jsem'),
('y4q t5F4m4d4fm5 3th5g8. d4c4s b2c b3c486','jiz definitivne odrekl. tisic pus posila'),
('d4 df2y b5b32c 6 d5c4 c5 3b5d m6 phqg1 84cd5g.','ti tvuj pepous a tesi se opet na brzky listek.')]
ys=[(555,594),(589,628),(621,658),(654,693),(686,730),(718,757),(752,794),(783,828),(815,862),(852,893),(865,918),(900,947),(931,982)]
records=[]
for n,((cipher,plain),(y0,y1)) in enumerate(zip(rows,ys),1):
 records.append({'row':n,'cipher':cipher,'expected_plain':plain,'crop_box_upright':[25,y0,648,y1],'crop':f'row-{n:02}.png','orientation':'source picture.jpg rotated clockwise 90 degrees; PIL rotate(-90,expand=True)','uncertainty':[]})
(W/'key.json').write_text(json.dumps(key,ensure_ascii=False,indent=2)+'\n')
(W/'manual-records.json').write_text(json.dumps({'method':'Manual visual reading, known family key transfer; no OCR. ASCII labels describe shapes, not their ordinary values. F = shallow-v-shaped family f; y = j-shaped family J.','rows':records},ensure_ascii=False,indent=2)+'\n')
manifest={name:hashlib.sha256((W.parent/'source'/name).read_bytes()).hexdigest() for name in ['picture.jpg','address.jpg','metadata.md']}
(W/'source-sha256.json').write_text(json.dumps(manifest,indent=2)+'\n')
lines=['row\tglyph_index\tword_index\tshape\tplain_base']
for row in records:
 i=0
 for word,part in enumerate(row['cipher'].split(' '),1):
  for ch in part:
   if ch in key:
    i+=1; lines.append(f"{row['row']}\t{i}\t{word}\t{ch}\t{key[ch]}")
(W/'indexed-transcription.tsv').write_text('\n'.join(lines)+'\n')
