"""Generate indexed manual-reading aids from unchanged source pixels."""
from pathlib import Path
import json
from PIL import Image,ImageDraw,ImageFont,ImageOps
r=Path(__file__).resolve().parents[1]; d=json.loads((r/'work/transcript.json').read_text()); p=Image.open(r/'source/picture.jpg')
font=ImageFont.truetype('/System/Library/Fonts/Monaco.ttf',20)
for row in d['rows']:
 gs=[g for w in row['words'] for g in w['glyphs']];left=max(0,min(g['center'][0] for g in gs)-22);right=min(1024,max(g['center'][0] for g in gs)+23)
 y=row['y'];box=(left,max(0,y-28),right,min(680,y+27));s=p.crop(box).resize(((right-left)*3,(box[3]-box[1])*3))
 q=Image.new('RGB',(s.width,s.height+65),'white');q.paste(s,(0,65));draw=ImageDraw.Draw(q)
 for g in gs:
  x=(g['center'][0]-left)*3;char='X' if g['shape'] is None else d['key'][g['shape']]
  draw.text((x-18,0),str(g['id']),font=font,fill='blue');draw.text((x-5,25),char,font=font,fill='blue');draw.line((x,50,x,65),fill='blue',width=1)
 q.save(r/'work'/f"indexed-{row['row']:02}.png")
for name,box in {'l9dots':(844,406,947,451),'l14s':(815,609,871,649),'l14kuss':(925,609,1013,649),'l14l':(244,603,282,648),'l12s':(212,527,272,572),'filial':(793,570,966,614),'canceled':(613,276,646,323),'muhs':(440,525,570,573),'dass':(738,447,870,493),'etwas':(790,360,890,405),'posttnisse':(290,601,440,646),'jede':(710,527,834,573),'sonnen':(27,447,330,492),'ver':(855,527,962,575)}.items():
 q=p.crop(box);q.resize((q.width*10,q.height*10)).save(r/'work'/f'{name}.png')
 ImageOps.grayscale(q).point(lambda x:0 if x<100 else 255).resize((q.width*10,q.height*10)).save(r/'work'/f'{name}-mask.png')
