#!/usr/bin/env python3
"""Make reading aids from unchanged scans. Requires Pillow; no image recognition."""
import json
from pathlib import Path
from PIL import Image, ImageDraw
HERE=Path(__file__).resolve().parent
p=Image.open(HERE.parent/'source/picture.jpg')
regions={'initials':(110,565,300,604),'ending':(745,615,1010,658),
 'karte':(743,575,892,620),'prose':(400,86,1007,586),'bottom':(0,555,1024,666),
 'left':(35,17,126,475)}
for name,b in regions.items():
 q=p.crop(b)
 if name=='left':q=q.rotate(270,expand=True)
 q.resize((q.width*3,q.height*3)).save(HERE/(name+'-audit.png'))
records=json.loads((HERE/'transcript.json').read_text())['records']
# Narrow source panels with identity labels above; labels are manual transcript hypotheses.
for prefix,y1,y2,x1,x2 in [('embedded initials',563,605,108,283),('main 1',571,631,398,999),('main 2',607,656,20,975)]:
 q=p.crop((x1,y1,x2,y2)).resize(((x2-x1)*3,(y2-y1)*3))
 out=Image.new('RGB',(q.width,q.height+42),'white');out.paste(q,(0,42));d=ImageDraw.Draw(out)
 for r in records:
  if not r['id'].startswith(prefix+'.'):continue
  x=(r['xy'][0]-x1)*3
  i=r['id'].split('.')[-1]
  d.text((x-5,0),i,fill='red');d.text((x-5,17),r['reading'],fill='red')
  d.line((x,32,x,42),fill='red')
 out.save(HERE/(prefix.replace(' ','-')+'-indexed.png'))
