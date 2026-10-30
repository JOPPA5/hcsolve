#!/usr/bin/env python3
"""Pixel-only crops (autocontrast, enlarged) for the 2026-10-29 re-reading."""
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
base = Path(__file__).resolve().parents[1]
im = Image.open(base/'source/address-large.jpg').convert('L')
rows = [
 ('B + 25: 2, flag-less 5 bowl, detached 5-bar, then dash (cf. WENT 25 next)', (180,112,345,145)),
 ('morning g-descender drops onto the 25 from above', (240,85,345,145)),
 ('LOOK: 6.7.7.14 (curved 1 + cursive 4); cf. hcp-1507 LOOK 6.7.7.14', (220,165,320,200)),
 ('AWAKEN: 12.21.12.14.3.25', (100,375,345,415)),
 ('RI|NG: 4.17 (7 has no base stroke; not 12)', (380,318,490,350)),
 ('BELL: 15.3.6.6, last 6 stem visible as single line across watermark', (140,222,320,260)),
 ('DO YOU: 18.7 (8 with top bar as in DID 18)', (200,410,360,450)),
 ('Sat. EVE [I].12.1 [V]: small closed loop on a faint stem (9-like) before 12; box enlarged per review 1', (60,450,360,512)),
 ('WINDOW: 21.17.[N].18.7.21', (60,195,175,228)),
 ('Signature 24.24 3.2.4.12: ordinary 2 (unlike the 14 of LOOK/AWAKEN)', (60,570,300,610)),
]
W, s = 1300, 4
out = Image.new('L', (W, sum((b[3]-b[1])*s+30 for _, b in rows)), 255)
d = ImageDraw.Draw(out); y = 0
for lab, b in rows:
    d.text((5, y+5), lab, fill=0)
    c = ImageOps.autocontrast(im.crop(b), cutoff=1)
    c = c.resize(((b[2]-b[0])*s, (b[3]-b[1])*s), Image.LANCZOS)
    out.paste(c, (5, y+25)); y += c.height+30
out.save(base/'work/controls-v2.png')
