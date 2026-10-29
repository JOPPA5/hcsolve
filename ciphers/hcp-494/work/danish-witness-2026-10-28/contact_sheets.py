"""Screening sheets: unaltered scan content, downscaled only, numbered by viewer page."""
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFont
ROOT = Path(__file__).parent
(ROOT / 'sheets').mkdir(exist_ok=True)
font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 22)
for start in range(1, 310, 12):
    paths = [ROOT / 'keys' / f'{i:03d}.jpg' for i in range(start, min(start+12,310))]
    if not all(p.exists() for p in paths): continue
    canvas = Image.new('RGB',(1800,1880),'white'); d=ImageDraw.Draw(canvas)
    for j,p in enumerate(paths):
        x=(j%3)*600; y=(j//3)*470
        with Image.open(p) as im: thumb=ImageOps.contain(im.convert('RGB'),(590,430))
        canvas.paste(thumb,(x+(600-thumb.width)//2,y+35))
        d.text((x+10,y+5),f'Page {int(p.stem)}',font=font,fill='black')
    canvas.save(ROOT / 'sheets' / f'{start:03d}-{min(start+11,309):03d}.jpg',quality=92)
