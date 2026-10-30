"""Reading aid: assign ink components to Morse rows by fitting a quadratic
centre line per row, then list marks (type, x0, x1, length) left to right.
usage: rowfit.py address.jpg out.json THR seeds_json
seeds: [[x_start, y_at_x_start, slope, x_end], ...]"""
import sys, json
from collections import deque
from PIL import Image
import numpy as np
src, out, thr = sys.argv[1], sys.argv[2], int(sys.argv[3])
seeds = json.loads(sys.argv[4])
a = np.asarray(Image.open(src).convert('RGB')).astype(int); g = a.sum(2) / 3
m = g < thr; H, W = m.shape
lab = np.zeros((H, W), int); comps = []
for y in range(H):
    for x in range(W):
        if m[y, x] and not lab[y, x]:
            n = len(comps) + 1; q = deque([(y, x)]); lab[y, x] = n; pts = []
            while q:
                cy, cx = q.popleft(); pts.append((cy, cx))
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        yy, xx = cy + dy, cx + dx
                        if 0 <= yy < H and 0 <= xx < W and m[yy, xx] and not lab[yy, xx]:
                            lab[yy, xx] = n; q.append((yy, xx))
            ys = np.array([p[0] for p in pts]); xs = np.array([p[1] for p in pts])
            th = int(max(np.bincount(xs - xs.min())))
            comps.append(dict(x0=int(xs.min()), x1=int(xs.max()), y0=int(ys.min()), y1=int(ys.max()),
                              cx=float(xs.mean()), cy=float(ys.mean()), area=len(pts), th=th,
                              dark=float(g[ys, xs].min())))
comps = [c for c in comps if c['area'] >= 3 and c['dark'] < thr - 20 and c['y1'] - c['y0'] <= 13]
res = []
for (x0, y0, s, xe) in seeds:
    coef = np.array([0.0, s, y0 - s * x0])  # quadratic in x
    band = 4.0
    for it in range(6):
        sel = [c for c in comps if x0 - 5 <= c['cx'] <= xe and abs(c['cy'] - np.polyval(coef, c['cx'])) <= band]
        if len(sel) >= 6:
            X = np.array([c['cx'] for c in sel]); Y = np.array([c['cy'] for c in sel])
            wts = np.array([min(c['x1'] - c['x0'] + 1, 20) for c in sel], float)
            deg = 2 if (X.max() - X.min()) > 200 else 1
            coef = np.polyfit(X, Y, deg, w=wts)
            if deg == 1: coef = np.array([0.0, coef[0], coef[1]])
        band = 3.5
    sel.sort(key=lambda c: c['x0'])
    marks = []
    for c in sel:
        if marks and c['x0'] - marks[-1]['x1'] <= 2 and marks[-1]['th'] < 6 and c['th'] < 6:
            marks[-1]['x1'] = max(marks[-1]['x1'], c['x1']); continue
        marks.append(dict(c))
    res.append(dict(coef=list(coef), marks=[[c['x0'], c['x1'], round(c['cy'], 1), c['th']] for c in marks]))
json.dump(res, open(out, 'w'), indent=0)
