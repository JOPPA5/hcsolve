"""Original-sign comparisons; ordinary crops only, with no ink removal or OCR."""
from pathlib import Path
from PIL import Image, ImageDraw
import json

ROOT = Path(__file__).resolve().parents[1]
SPECS = {
    'initial-pair': ('full/0004.jpg', (930, 2390, 1100, 2520)),
    'key-g-h': ('full/key255.jpg', (710, 400, 950, 960)),
    'inverse-II-g': ('full/key254.jpg', (1810, 3490, 2170, 3620)),
    'five-in-75': ('full/0004.jpg', (2015, 2370, 2200, 2495)),
    'five-in-85': ('full/0004.jpg', (1350, 1900, 1570, 2035)),
    'five-in-625': ('full/0004.jpg', (1000, 900, 1260, 1030)),
    'BB-pair': ('full/0004.jpg', (2070, 2010, 2240, 2130)),
    'key-BB-z': ('full/key255.jpg', (2350, 390, 2495, 920)),
    'key-PP-n': ('full/key255.jpg', (1305, 390, 1420, 950)),
}
for name, (source, box) in SPECS.items():
    Image.open(ROOT/'source'/source).crop(box).save(ROOT/f'work/glyph-first-{name}.png')

sheet = Image.new('RGB', (1320, 920), 'white')
draw = ImageDraw.Draw(sheet)
def paste(name, xy, label, scale=1):
    im = Image.open(ROOT/f'work/glyph-first-{name}.png')
    if scale != 1:
        im = im.resize((round(im.width*scale), round(im.height*scale)))
    x, y = xy
    draw.text((x, y), label, fill='black')
    sheet.paste(im, (x, y+25))
paste('initial-pair', (15, 10), 'Disputed pair: 55 or doubled I/J?', 2)
paste('key-g-h', (440, 10), 'Key 255: G and H columns', 1)
paste('inverse-II-g', (15, 340), 'Inverse key 254: doubled I/J = g', 1)
paste('five-in-75', (780, 10), 'Same writer: 5 in 75', 2)
paste('five-in-85', (780, 300), 'Same writer: 5 in 85', 2)
paste('five-in-625', (780, 610), 'Same writer: 5 in 625', 1.8)
draw.text((15, 670), 'A plausible alternative glyph reading, not a proven correction.', fill='black')
draw.text((15, 700), 'No source pixels or black annotations were removed.', fill='black')
sheet.save(ROOT/'work/glyph-first-initial-comparison.png')
(ROOT/'work/glyph-first-crops.json').write_text(json.dumps(SPECS, indent=2)+'\n')
print('Crops and comparison sheet written.')
