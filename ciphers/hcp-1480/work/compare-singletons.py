#!/usr/bin/env python3
"""Reproducible source-coordinate atlas; no guessed plaintext mappings."""
from pathlib import Path
import hashlib, json
from PIL import Image, ImageDraw
p=Path(__file__).resolve().parents[1]
for name,digest in json.loads((p/'work/source-sha256.json').read_text()).items():
    assert hashlib.sha256((p/'source'/name).read_bytes()).hexdigest()==digest
im=Image.open(p/'source/address-large.jpg').convert('RGB')
# Source image 1024x674. Rectangles include surrounding ink deliberately.
regions=[
 ('ARCH (unknown)',(52,460,92,499)),
 ('DOTTED_C (unknown)',(88,460,128,501)),
 ('HOOK (unknown)',(299,484,342,517)),
 ('C_SHAPE = O in LOVE',(299,382,338,424)),
 ('UNDER = C in CARD',(322,329,362,369)),
 ('BAR = L before LOVE',(265,381,304,420)),
 ('BAR before HOOK',(269,471,306,513)),
 ('SLANT_BAR final WILL',(337,575,379,610)),
 ('CIRCLE = A, CARD',(357,338,393,380)),
 ('TRI = D, CARD',(410,338,449,383)),
 ('RECT = T, JUST',(178,319,213,365)),
 ('CUP = U, line 5',(118,456,161,505)),
]
canvas=Image.new('RGB',(900,((len(regions)+2)//3)*210),'white')
d=ImageDraw.Draw(canvas)
for n,(label,box) in enumerate(regions):
    tile=im.crop(box)
    factor=min(220/tile.width,150/tile.height)
    tile=tile.resize((round(tile.width*factor),round(tile.height*factor)))
    x=(n%3)*300;y=(n//3)*210
    d.text((x+8,y+5),label,fill='black')
    canvas.paste(tile,(x+8,y+28))
    d.text((x+8,y+183),str(box),fill='black')
canvas.save(p/'work/singletons-atlas.png')
(p/'work/singletons-crops.json').write_text(json.dumps(regions,indent=2)+'\n')
print('Source hashes passed; created 12 labelled source-coordinate crops.')
