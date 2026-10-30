"""Extract dark ink components from the address side (helper for manual reading)."""
import sys
from PIL import Image
import numpy as np
from collections import deque
src = sys.argv[1]
thr = int(sys.argv[2]) if len(sys.argv) > 2 else 135
a = np.asarray(Image.open(src).convert('RGB')).astype(int)
g = a.sum(2) / 3
m = g < thr
H, W = m.shape
lab = np.zeros((H, W), int)
comps = []
n = 0
for y in range(H):
    for x in range(W):
        if m[y, x] and not lab[y, x]:
            n += 1
            q = deque([(y, x)]); lab[y, x] = n; pts = []
            while q:
                cy, cx = q.popleft(); pts.append((cy, cx))
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        yy, xx = cy + dy, cx + dx
                        if 0 <= yy < H and 0 <= xx < W and m[yy, xx] and not lab[yy, xx]:
                            lab[yy, xx] = n; q.append((yy, xx))
            ys = [p[0] for p in pts]; xs = [p[1] for p in pts]
            vals = [g[p] for p in pts]
            comps.append(dict(id=n, x0=min(xs), x1=max(xs), y0=min(ys), y1=max(ys),
                              cx=sum(xs)/len(xs), cy=sum(ys)/len(ys), area=len(pts), dark=min(vals)))
import json
json.dump(comps, sys.stdout)
