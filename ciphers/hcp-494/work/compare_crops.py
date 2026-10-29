"""Reproduce the auxiliary letter crops, without image enhancement (Pillow)."""
from pathlib import Path
import json
from PIL import Image, ImageDraw
ROOT = Path(__file__).resolve().parents[1]
specs = [
    ('lincker1677-p2-cipher.png',2,(400,1950,2540,2950),None),
    ('lincker1677-p3-cipher.png',3,(470,2050,2480,2870),None),
    ('lincker1677-p4-cipher.png',4,(360,880,2390,1710),None),
    ('lincker1677-55.png',3,(500,2460,1110,2670),(1220,420)),
    ('lincker1677-date-5.png',5,(150,3480,1100,3850),None),
    ('lincker1677-date-2.png',2,(0,0,2654,900),None),
]
for name, page, box, size in specs:
    im = Image.open(ROOT/f'source/arcinsys/daenemark145-{page:04}.jpg').crop(box)
    if size: im=im.resize(size)
    im.save(ROOT/'work'/name)
sheet=Image.new('RGB',(1500,520),'white')
draw=ImageDraw.Draw(sheet)
for i in range(1,6):
    im=Image.open(ROOT/f'source/arcinsys/daenemark145-{i:04}.jpg')
    im.thumbnail((290,485)); sheet.paste(im,((i-1)*300,25))
    draw.text(((i-1)*300+5,5),f'Daenemark 145 image {i}',fill='black')
sheet.save(ROOT/'work/daenemark145-contact.jpg')
(ROOT/'work/compare-crops.json').write_text(json.dumps(specs,indent=2)+'\n')
