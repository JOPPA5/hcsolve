"""Reading aid: chain ink components into Morse rows and classify each mark
by length/thickness (d = dot, s = short dash, L = long dash, B = blot).
Writes a JSON of marks per row and an annotated image to check by eye.
usage: chain.py address.jpg out_prefix THR seeds_json"""
import sys, json
from collections import deque
from PIL import Image, ImageDraw
import numpy as np
src, out, thr = sys.argv[1], sys.argv[2], int(sys.argv[3])
seeds = json.loads(sys.argv[4])  # [[x,y,slope],...]
im = Image.open(src).convert('RGB')
a = np.asarray(im).astype(int); g = a.sum(2) / 3
m = g < thr
H, W = m.shape
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
            # thickness = max column height
            th = max(np.bincount(xs - xs.min()))
            comps.append(dict(x0=int(xs.min()), x1=int(xs.max()), y0=int(ys.min()), y1=int(ys.max()),
                              cy=float(ys.mean()), area=len(pts), th=int(th),
                              dark=float(g[ys, xs].min())))
DK = int(sys.argv[5]) if len(sys.argv) > 5 else thr - 15
comps = [c for c in comps if c['area'] >= 3 and c['dark'] < DK]
used = set(); rows = []
for (sx, sy, slope) in seeds:
    x, y = sx, float(sy); row = []
    while x < W - 20:
        best = None
        for i, c in enumerate(comps):
            if i in used or c['x0'] < x - 3 or c['x0'] > x + 45: continue
            if c['y1'] - c['y0'] > 14: continue
            py = y + slope * (c['x0'] - x)
            if abs(c['cy'] - py) <= 4.5:
                if best is None or c['x0'] < comps[best]['x0']: best = i
        if best is None: break
        c = comps[best]; used.add(best)
        # merge pieces of the same stroke
        if row and c['x0'] - row[-1]['x1'] <= 2 and row[-1]['th'] < 6 and c['th'] < 6:
            r = row[-1]; r['x1'] = max(r['x1'], c['x1']); r['area'] += c['area']
        else:
            row.append(dict(c))
        newy = c['cy'] + slope * ((c['x1'] - c['x0']) / 2)
        y = 0.5 * (y + slope * (c['x1'] - x)) + 0.5 * newy
        x = c['x1'] + 1
    rows.append(row)
def cls(c):
    L = c['x1'] - c['x0'] + 1
    if c['th'] >= 6 and L <= 15: return 'B'
    if L <= 4: return 'd'
    if L <= 12: return 's'
    return 'L'
res = []
for k, row in enumerate(rows):
    marks = [(cls(c), c['x0'], c['x1'], round(c['cy'], 1)) for c in row]
    res.append(marks)
    print('R%02d' % (k + 1), ''.join(t[0] for t in marks), '| end x=%d' % (row[-1]['x1'] if row else -1))
json.dump(res, open(out + '.json', 'w'))
ov = im.resize((W * 2, H * 2), Image.LANCZOS); d = ImageDraw.Draw(ov)
col = dict(d=(0, 0, 255), s=(0, 160, 0), L=(255, 0, 0), B=(200, 0, 200))
for k, marks in enumerate(res):
    for (t, x0, x1, cy) in marks:
        d.rectangle((x0 * 2 - 1, cy * 2 - 7, x1 * 2 + 1, cy * 2 + 7), outline=col[t])
    if marks: d.text((marks[0][1] * 2 - 22, marks[0][3] * 2 - 6), str(k + 1), fill=(255, 0, 0))
ov.save(out + '.png')
