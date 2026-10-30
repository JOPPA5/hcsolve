"""List ink components of the rotated cipher area (reading orientation) per line.
Usage: python3 -I work/components.py <full-res address JPG> <out.png>"""
import sys
from collections import deque
from PIL import Image, ImageDraw
import numpy as np
im = Image.open(sys.argv[1]).convert('L')
r = im.crop((60, 120, 840, 1150)).rotate(90, expand=True)
a = np.array(r)
ink = a < 115
H, W = ink.shape
lab = np.zeros((H, W), int)
comps = []
n = 0
for y in range(H):
    for x in range(W):
        if ink[y, x] and not lab[y, x]:
            n += 1
            q = deque([(y, x)]); lab[y, x] = n; pts = []
            while q:
                cy, cx = q.popleft(); pts.append((cy, cx))
                for dy in (-2, -1, 0, 1, 2):
                    for dx in (-2, -1, 0, 1, 2):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < H and 0 <= nx < W and ink[ny, nx] and not lab[ny, nx]:
                            lab[ny, nx] = n; q.append((ny, nx))
            ys = [p[0] for p in pts]; xs = [p[1] for p in pts]
            comps.append((n, min(xs), min(ys), max(xs), max(ys), len(pts)))
lines = [70, 140, 205, 280, 350, 428, 505, 580, 655, 735]
out = Image.fromarray(np.where(ink, 0, 255).astype('uint8')).convert('RGB')
out = out.resize((W * 3, H * 3))
d = ImageDraw.Draw(out)
for li, ly in enumerate(lines):
    row = [c for c in comps if c[5] >= 6 and abs((c[2] + c[4]) / 2 - ly) < 34]
    row.sort(key=lambda c: c[1])
    print('LINE', li + 1)
    for k, c in enumerate(row):
        cy = (c[2] + c[4]) / 2 - ly
        print(f'  {k:2d} x={c[1]:4d}-{c[3]:4d} y={c[2]-ly:+4d}..{c[4]-ly:+4d} w={c[3]-c[1]+1:3d} h={c[4]-c[2]+1:3d} n={c[5]}')
        d.rectangle([c[1] * 3, c[2] * 3, c[3] * 3, c[4] * 3], outline=(255, 0, 0))
        d.text((c[1] * 3, c[4] * 3 + 2), f'{li+1}.{k}', fill=(0, 0, 255))
out.save(sys.argv[2])
