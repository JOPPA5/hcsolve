#!/usr/bin/env python3
"""Evidence crops for review round 1 (Claude Opus 5.5, 2026-10-30).
Usage (from repo root): <python-with-PIL> -I ciphers/hcp-899/work/crop_evidence.py
Writes enlarged, contrast-boosted crops of source/picture.jpg to work/crops/."""
import sys
from pathlib import Path
from PIL import Image, ImageEnhance
root = Path(__file__).resolve().parents[1]
src = Image.open(root/'source/picture.jpg').convert('RGB')
BOXES = {  # name: (x0, y0, x1, y1, scale)
 'L4_word3_LIEBES': (500, 455, 675, 492, 8),
 'L4_full': (330, 440, 1010, 505, 3),
}
extra = sys.argv[1:]
for a in extra:  # ad-hoc: name,x0,y0,x1,y1,s
    n, *v = a.split(','); BOXES[n] = tuple(map(int, v))
out = root/'work/crops'; out.mkdir(exist_ok=True)
for n, (x0, y0, x1, y1, s) in BOXES.items():
    im = src.crop((x0, y0, x1, y1)).resize(((x1-x0)*s, (y1-y0)*s), Image.LANCZOS)
    ImageEnhance.Contrast(im).enhance(1.8).save(out/f'{n}.png')
    print(n)
