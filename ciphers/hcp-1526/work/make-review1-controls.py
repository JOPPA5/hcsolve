#!/usr/bin/env python3
"""Mutates work/ only: raw native-source nearest-neighbor review controls."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,hashlib
W=Path(__file__).resolve().parent;C=W.parent
expected=json.loads((W/'source-sha256.json').read_text())['source/picture.jpg']
assert hashlib.sha256((C/'source/picture.jpg').read_bytes()).hexdigest()==expected
im=Image.open(C/'source/picture.jpg').transpose(Image.Transpose.ROTATE_90)
controls=[
('R02 STREDY: looped d/T and crossed t/D control',[185,527,293,578]),
('R03 PRNEM and adjacent PROUDU: same tall looped h/R',[350,555,575,610]),
('R06 CRDECKO, KDERE, ZACE: angular s/C and crossed t/D',[165,645,635,699]),
('R08 SRDECKO: contrasting initial round c/S',[475,709,635,756]),
('R09 SETRIDI, DO, ANDULICKA: complete row context',[24,737,635,790]),
('R09 ANDULICKA: 6mt284sg6, including formerly omitted 4s',[440,737,635,790]),
('R10 DUTKLIVA: closed terminal 6/A, not 5/E',[155,768,292,821]),
('R13 VZDIT versus BYL: underbarred 4/I and footed 1/Y',[24,863,286,917]),
('R15 KDERY: crossed t/D, like KDERE',[418,925,541,979]),
('R03 SECONA: angular s/C retained',[180,558,289,608]),
('R04 DOUFAM: shallow v/F remains contextual singleton',[385,590,535,646]),
('R05 VZPOMINAM/VSAK: contrasting tall-looped f/V',[343,619,635,669]),
]
font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',18)
recs=[]
for i,(label,b) in enumerate(controls,1):
 crop=im.crop(b);scale=3;name=f'review1-native-{i:02}.png'
 crop.resize((crop.width*scale,crop.height*scale),Image.Resampling.NEAREST).save(W/name)
 recs.append(dict(id=i,description=label,bbox=b,scale=scale,resampling='nearest',file=name))
for k in range(0,len(recs),4):
 part=recs[k:k+4];h=sum(53+(r['bbox'][3]-r['bbox'][1])*3 for r in part)
 panel=Image.new('RGB',(1900,h),'white');draw=ImageDraw.Draw(panel);y=0
 for rec in part:
  draw.text((8,y+1),rec['description'],font=font,fill='black')
  draw.text((8,y+24),'Native upright box '+str(rec['bbox'])+'; raw nearest-neighbor 3x',font=font,fill='black')
  tile=Image.open(W/rec['file']);panel.paste(tile,(8,y+49));y+=tile.height+53
 panel.save(W/f'review1-panel-{k//4+1}.png')
(W/'review1-controls.json').write_text(json.dumps(dict(source_sha256=expected,transform='Original picture.jpg lossless ROTATE_90 counterclockwise; native upright 674x1024; raw nearest-neighbor only',coordinate_note='Boxes locate word/row context, not individually segmented glyphs. Neighboring ascenders/descenders may be present.',controls=recs),ensure_ascii=False,indent=2)+'\n')
