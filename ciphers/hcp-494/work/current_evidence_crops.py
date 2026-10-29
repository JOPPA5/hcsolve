"""Plain pixel crops and a labelled comparison sheet; no enhancement."""
from pathlib import Path
from PIL import Image, ImageDraw
import json
ROOT=Path(__file__).resolve().parents[1]
specs={
 'p2-ll':('full/0004.jpg',(2180,2350,2360,2500)),
 'p2-au':('full/0004.jpg',(1300,2445,1490,2630)),
 'p2-ff':('full/0004.jpg',(1480,2450,1770,2630)),
 'key-ll':('full/key255.jpg',(1118,905,1218,1210)),
 'key-mm':('full/key255.jpg',(1218,905,1320,1210)),
 'key-au':('full/key255.jpg',(145,905,260,1210)),
 'key-ff':('full/key255.jpg',(1018,905,1118,1210)),
 'p1-XX-control':('full/0004.jpg',(1650,1890,1940,2050)),
 '447-602':('full/0004.jpg',(1410,2770,2020,3030)),
 '625':('full/0003.jpg',(180,1090,750,1390)),
}
for name,(src,box) in specs.items():
 Image.open(ROOT/'source'/src).crop(box).save(ROOT/f'work/current-{name}.png')
sheet=Image.new('RGB',(1300,1060),'white');draw=ImageDraw.Draw(sheet)
for row,(name,kn) in enumerate([('p2-ll','key-ll'),('p2-au','key-au'),('p2-ff','key-ff')]):
 y=350*row;draw.text((10,y+5),f'{name}: target (left), key 255 (middle)',fill='black')
 for x,n in [(10,name),(600,kn)]:
  im=Image.open(ROOT/f'work/current-{n}.png');sheet.paste(im,(x,y+30))
 if row==0:
  draw.text((800,y+5),'mm control',fill='black')
  sheet.paste(Image.open(ROOT/'work/current-key-mm.png'),(800,y+30))
 if row==2:
  draw.text((800,y+5),'XX=u in passage 1',fill='black')
  sheet.paste(Image.open(ROOT/'work/current-p1-XX-control.png'),(800,y+30))
sheet.save(ROOT/'work/syllable-evidence-sheet.png')
(ROOT/'work/current-evidence-crops.json').write_text(json.dumps(specs,indent=2)+'\n')
