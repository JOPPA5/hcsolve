#!/usr/bin/env python3
"""Unenhanced same-scale source-pixel comparison; no dot classifier."""
from pathlib import Path
from PIL import Image,ImageDraw
import json,statistics
p=Path(__file__).resolve().parent
im=Image.open(p.parent/'source/picture.jpg').convert('RGB')
items=[
('target KOMME E?',(325,503,355,536),(338,518)),
('target KRAEFTIG E/O',(927,503,959,537),(942,520)),
('secure E: EINEN r3-1',(518,503,547,536),(532,520)),
('secure E: EINEN r3-2',(599,503,628,536),(614,521)),
('secure O: KOMME',(246,501,273,535),(258,518)),
('secure O: THEO',(744,600,780,637),(760,616)),
('secure E: HERZIGEN',(548,469,579,502),(562,487)),
('secure E: GUTENACHT',(181,587,214,626),(197,609)),
]
canvas=Image.new('RGB',(4*270,2*300),'white');d=ImageDraw.Draw(canvas)
records=[]
for i,(name,box,center) in enumerate(items):
 patch=im.crop(box);tile=patch.resize((patch.width*6,patch.height*6),Image.Resampling.NEAREST)
 x=(i%4)*270;y=(i//4)*300
 canvas.paste(tile,(x+8,y+40));d.text((x+8,y+4),name,fill='black');d.text((x+8,y+20),str(box),fill='black')
 cx,cy=center
 vals=list(im.convert('L').crop((cx-2,cy-2,cx+3,cy+3)).getdata())
 rec={'name':name,'box':box,'center_roi':[cx-2,cy-2,cx+3,cy+3],'center_roi_gray_min':min(vals),'center_roi_gray_mean':round(statistics.mean(vals),2)}
 records.append(rec)
canvas.save(p/'box-controls-unenhanced.png')
(p/'box-control-measurements.json').write_text(json.dumps({'note':'Descriptive 5x5 grayscale pixels only, neither ink classification nor independent validation. Coordinate choice matters; no intensity threshold resolves provenance.', 'records':records},indent=2)+'\n')
print(json.dumps(records,indent=2))
