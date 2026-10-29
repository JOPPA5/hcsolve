"""Connected-component and stave analysis inside a window of a BMP crop.
usage: cc.py file.bmp thr x0 y0 x1 y1
Prints ink components (8-connected, >= 40 px) with bbox/size, and the two
heaviest staves (columns) with their ink row extents inside the window."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(sys.argv[0])))
from inkgap import read_bmp
path, thr, x0, y0, x1, y1 = sys.argv[1], int(sys.argv[2]), *map(int, sys.argv[3:7])
w, h, g = read_bmp(path)
ink = {(x, y) for y in range(y0, y1) for x in range(x0, x1) if g[y][x] < thr}
seen = set(); comps = []
for p in ink:
    if p in seen: continue
    stack = [p]; seen.add(p); comp = []
    while stack:
        x, y = stack.pop(); comp.append((x, y))
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                q = (x+dx, y+dy)
                if q in ink and q not in seen: seen.add(q); stack.append(q)
    comps.append(comp)
comps = [c for c in comps if len(c) >= 40]
comps.sort(key=lambda c: min(p[0] for p in c))
print(os.path.basename(path), f'thr={thr} window x{x0}-{x1} y{y0}-{y1}: {len(comps)} components >=40px')
for c in comps:
    xs = [p[0] for p in c]; ys = [p[1] for p in c]
    print(f'  size {len(c):5d}  x {min(xs)}-{max(xs)}  y {min(ys)}-{max(ys)}')
col = {x: sum(1 for y in range(y0, y1) if (x, y) in ink) for x in range(x0, x1)}
mx = max(col.values()); runs = []; cur = None
for x in range(x0, x1):
    if col[x] >= 0.55*mx: cur = [x, x] if cur is None else [cur[0], x]
    elif cur: runs.append(tuple(cur)); cur = None
if cur: runs.append(tuple(cur))
runs = sorted(runs, key=lambda r: -sum(col[x] for x in range(r[0], r[1]+1)))[:2]; runs.sort()
info = []
for a, b in runs:
    rows = [y for y in range(y0, y1) if any((x, y) in ink for x in range(a, b+1))]
    info.append((a, b, min(rows), max(rows)))
    print(f'  stave cols {a}-{b} (w {b-a+1}) rows {min(rows)}-{max(rows)} height {max(rows)-min(rows)+1}')
if len(info) == 2:
    hgt = max(i[3]-i[2]+1 for i in info); gap = info[1][0]-info[0][1]-1
    print(f'  clear gap between staves {gap}px = {gap/hgt:.2f} of stave height')
