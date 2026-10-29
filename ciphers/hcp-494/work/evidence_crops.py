"""Unretouched crops of newly acquired evidence; Pillow is required."""
from pathlib import Path
from PIL import Image, ImageDraw
import json

ROOT = Path(__file__).resolve().parents[1]
CROPS = {
    'archive-0001-crop.png': ('arcinsys/0001.jpg', (180, 1710, 1900, 2420)),
    'archive-0005-crop.png': ('arcinsys/0005.jpg', (1190, 2600, 2220, 3320)),
    'archive-0004-crop.png': ('arcinsys/0004.jpg', (80, 1650, 2170, 2430)),
    'alliance-codes.png': ('full/0004.jpg', (540, 2590, 2440, 3280)),
    '427-vs-447.png': ('full/0004.jpg', (520, 2780, 2440, 3040)),
    '55-close.png': ('full/0004.jpg', (850, 2390, 1260, 2530)),
}
for name, (source, box) in CROPS.items():
    im = Image.open(ROOT / 'source' / source).crop(box)
    # Enlargement aids viewing and adds no source detail.
    if name == '427-vs-447.png':
        im = im.resize((2880, 390))
    if name == '55-close.png':
        im = im.resize((1230, 420))
    im.save(ROOT / 'work' / name)
(ROOT / 'work/evidence-crops.json').write_text(json.dumps(CROPS, indent=2) + '\n')

contact = Image.new('RGB', (1500, 1530), 'white')
for i, p in enumerate(sorted((ROOT / 'source/arcinsys').glob('000?.jpg'))):
    im = Image.open(p)
    im.thumbnail((490, 720))
    x, y = i % 3 * 500, i // 3 * 765
    contact.paste(im, (x, y + 30))
    ImageDraw.Draw(contact).text((x + 10, y + 8), p.name, fill='black')
contact.save(ROOT / 'work/archive-contact.jpg')
