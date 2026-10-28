#!/usr/bin/env python3
"""Mutating, explicit generation of image controls and row panels."""
import json,hashlib
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
p=Path(__file__).resolve().parents[1];w=p/'work';im=Image.open(p/'source/picture.jpg').transpose(Image.Transpose.ROTATE_90)
im.save(w/'upright.png')
fontpath='/System/Library/Fonts/Supplemental/Arial.ttf'
f=ImageFont.truetype(fontpath,18);small=ImageFont.truetype(fontpath,16)
record=json.loads((w/'transcription.json').read_text())
for k in range(0,16,4):
 rows=record['rows'][k:k+4];out=Image.new('RGB',(1250,4*175),'white');d=ImageDraw.Draw(out)
 for j,r in enumerate(rows):
  y=j*175;d.text((8,y+1),r['id']+' '+r['plaintext'],font=f,fill='black');d.text((8,y+25),r['cipher'],font=small,fill='black')
  crop=im.crop(r['bbox']);crop=crop.resize((crop.width*2,crop.height*2));out.paste(crop,(8,y+53))
 out.save(w/f'indexed-rows-{k+1:02}-{k+4:02}.png')
controls=[
 ('R01: q/Z in ZLATO and ZA; g/K in LISTEK',[225,495,636,546]),
 ('R04: shallow v/F in DOUFAM; no tall f/V descender',[385,591,535,643]),
 ('R05: tall f/V in VZPOMINAM and VSAK',[343,620,633,665]),
 ('R07: capped CH in NACHLADILA and BEZPOCHYBY',[305,683,635,741]),
 ('R08: uncapped r/H in BEHEM; no CH cap',[25,709,160,752]),
 ('R11: q/Z in TAZE and ZDA',[24,800,235,845]),
 ('R11: g/K and q/Z in KDYZ',[541,801,635,846]),
 ('R09: M/N distinction in MNE and ANDULICKA',[319,739,633,783]),
]
out=Image.new('RGB',(1250,sum(36+(b[3]-b[1])*3 for _,b in controls)),'white');d=ImageDraw.Draw(out);y=0
for title,b in controls:
 d.text((8,y+3),title,font=f,fill='black');y+=32
 c=im.crop(b);c=c.resize((c.width*3,c.height*3),Image.Resampling.NEAREST);out.paste(c,(8,y));y+=c.height+4
out.save(w/'source-controls.png')
(w/'source-controls.json').write_text(json.dumps({'source_sha256':hashlib.sha256((p/'source/picture.jpg').read_bytes()).hexdigest(),'transform':'PIL.Image.Transpose.ROTATE_90 counterclockwise lossless; crops enlarged nearest-neighbor','coordinates':'[left,top,right,bottom] in upright 674x1024 picture','controls':[{'description':a,'bbox':b} for a,b in controls]},indent=2)+'\n')
sezona=[('R03 VANOCNI, s/C',[25,558,163,598]),('R03 c5s3m6 disputed unit',[180,560,289,605]),('R06 CRDECKO, first/fifth s/C',[175,648,300,693]),('R01 ZLATO, q/Z',[228,496,296,541]),('R04 JESTE, c/S',[25,591,150,631]),('R15 VELICE, s/C',[532,926,636,970])]
out=Image.new('RGB',(1100,6*185),'white');d=ImageDraw.Draw(out)
for i,(title,b) in enumerate(sezona):
 d.text((8,i*185),title,font=f,fill='black');c=im.crop(b);out.paste(c.resize((c.width*3,c.height*3),Image.Resampling.NEAREST),(8,i*185+30))
out.save(w/'sezona-controls.png')
(w/'sezona-controls.json').write_text(json.dumps({'source_sha256':hashlib.sha256((p/'source/picture.jpg').read_bytes()).hexdigest(),'transform':'Lossless ROTATE_90, nearest-neighbor enlargement 3x','coordinates':'[left,top,right,bottom] in upright 674x1024 picture','controls':[{'description':a,'bbox':b} for a,b in sezona]},indent=2)+'\n')
