#!/usr/bin/env python3
"""Nearest-neighbour source crops for the two remaining numeral questions.

No contrast alteration, masking, or stroke reconstruction. Boxes are measured
in the immutable 1024 by 674 address scan. Labels are hypotheses/controls,
not machine classifications.
"""
from pathlib import Path
from PIL import Image, ImageDraw

base = Path(__file__).resolve().parents[1]
im = Image.open(base / 'source/address-large.jpg')
rows = [
    ('Unmapped B23: full 15.23 group', (224, 110, 322, 145)),
    ('Known 3: DEAR second code', (178, 37, 216, 77)),
    ('Known 3: signature initial code', (171, 573, 209, 606)),
    ('Known 6: MY final digit in 26', (114, 38, 146, 77)),
    ('Known 6: GIRL final code', (384, 37, 417, 76)),
    ('BEL[6|8]: adjacent known 6 and disputed final digit', (238, 224, 315, 258)),
    ('Known 6: FELT third code; known 8 immediately after', (223, 65, 281, 98)),
    ('Known 8: line 4 TO first code', (338, 110, 370, 146)),
    ('Known 8: line 6 NOT final code', (157, 164, 191, 201)),
]
out = Image.new('RGB', (1050, 225 * len(rows)), 'white')
draw = ImageDraw.Draw(out)
for n, (label, box) in enumerate(rows):
    draw.text((10, n * 225 + 5), label, fill='black')
    crop = im.crop(box)
    out.paste(crop.resize((crop.width * 5, crop.height * 5),
                         Image.Resampling.NEAREST), (10, n * 225 + 28))
out.save(base / 'work/continued-controls.png')
