#!/usr/bin/env python3
"""Detect ink marks (dots/dashes) per Morse row on the hi-res address side.
Needs PIL. Prints, per row, each mark's x-start, width and gap to previous mark
(hi-res pixels). Ink threshold excludes the lighter grey collector stamp."""
import sys
from pathlib import Path
from PIL import Image
ROOT = Path(__file__).resolve().parents[1]
im = Image.open(ROOT / 'work/hires/cpc_--_USA__USA___adr.jpg').convert('L')
S = 3468 / 1024
ROWS = [(312, 337), (348, 372), (395, 418), (428, 452), (462, 486), (497, 528), (535, 568), (585, 612)]
for n, (a, b) in enumerate(ROWS, 1):
    y0, y1 = int(a * S), int(b * S)
    x0, x1 = int(100 * S), int(985 * S)
    cols = []
    for x in range(x0, x1):
        dark = sum(1 for y in range(y0, y1) if im.getpixel((x, y)) < 120)
        cols.append(dark)
    marks = []; inm = False
    for i, d in enumerate(cols):
        if d >= 2 and not inm:
            inm = True; st = i
        elif d < 2 and inm:
            inm = False
            if i - st >= 5: marks.append((st + x0, i - st))
    out = []; prev = None
    for st, w in marks:
        g = '' if prev is None else st - prev
        out.append(f'{st}:{w}' + (f'(+{g})' if g != '' else ''))
        prev = st + w
    print(f'row {n}: ' + ' '.join(out))
