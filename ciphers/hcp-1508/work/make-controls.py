#!/usr/bin/env python3
"""Pixel crops from the immutable scan. No drawn-in or reconstructed strokes."""
from pathlib import Path
from PIL import Image, ImageDraw

base = Path(__file__).resolve().parents[1]
im = Image.open(base / 'source/address-large.jpg')
rows = [
    ('WHEN: final 25, compare flat-topped 5 below', (330, 88, 475, 118)),
    ('Control MY: 26, 6 has rising stem and lower loop', (70, 38, 148, 77)),
    ('Control NOT: 25', (65, 166, 145, 197)),
    ('Control WENT: 25', (120, 111, 217, 145)),
    ('Unmapped B[23?], then TO FIND', (210, 111, 554, 146)),
    ('LOOK: final 2', (195, 168, 330, 199)),
    ('BELL/BELT: last numeral remains 6|8', (150, 227, 315, 255)),
    ('YOUR: final numeral 4, one numeral not 14', (251, 254, 435, 287)),
    ('Control GIRL: 4 before 6', (350, 37, 417, 73)),
    ('AWAKEN: fourth numeral 2', (102, 380, 341, 414)),
    ('Signature: 3.2.4.12 = EKRA', (172, 575, 294, 605)),
    ('Control closing YOUR: 26.7.16.4', (200, 552, 340, 582)),
]
out = Image.new('RGB', (1500, len(rows) * 180), 'white')
draw = ImageDraw.Draw(out)
for n, (label, box) in enumerate(rows):
    draw.text((10, n * 180 + 4), label, fill='black')
    crop = im.crop(box)
    out.paste(crop.resize((crop.width * 4, crop.height * 4)), (10, n * 180 + 25))
out.save(base / 'work/focused-controls.png')
