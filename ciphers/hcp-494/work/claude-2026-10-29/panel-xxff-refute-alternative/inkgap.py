"""Plain-Python BMP reader + ink-gap analysis (no numpy/Pillow).
For each crop: threshold to ink, find column ink-profile, locate the two heaviest
near-vertical staves, then report whether any row carries continuous ink across
the gap between the staves (a shared crossbar / connector would).
"""
import struct, sys

def read_bmp(path):
    with open(path, 'rb') as f:
        data = f.read()
    off = struct.unpack_from('<I', data, 10)[0]
    w, h = struct.unpack_from('<ii', data, 18)
    bpp = struct.unpack_from('<H', data, 28)[0]
    assert bpp in (24, 32), bpp
    bypp = bpp // 8
    rowsize = ((w * bypp + 3) // 4) * 4
    flip = h > 0
    h = abs(h)
    gray = []
    for r in range(h):
        rr = (h - 1 - r) if flip else r
        base = off + rr * rowsize
        row = []
        for c in range(w):
            b, g, rch = data[base + c*bypp: base + c*bypp + 3]
            row.append((rch*299 + g*587 + b*114)//1000)
        gray.append(row)
    return w, h, gray

def analyse(path, thr, stave_min_frac=0.55):
    w, h, g = read_bmp(path)
    ink = [[g[y][x] < thr for x in range(w)] for y in range(h)]
    col = [sum(ink[y][x] for y in range(h)) for x in range(w)]
    mx = max(col)
    # staves = runs of columns with ink count >= stave_min_frac*max
    runs, cur = [], None
    for x in range(w):
        if col[x] >= stave_min_frac*mx:
            cur = [x, x] if cur is None else [cur[0], x]
        else:
            if cur: runs.append(tuple(cur)); cur = None
    if cur: runs.append(tuple(cur))
    print(f"{path.split('/')[-1]}: {w}x{h} thr={thr} max_col_ink={mx} staves(cols)={runs}")
    # for each row report longest horizontal ink run and whether it spans the gap between staves 1 and 2
    if len(runs) >= 2:
        # take the two heaviest runs
        runs2 = sorted(runs, key=lambda r: -sum(col[r[0]:r[1]+1]))[:2]
        runs2.sort()
        a, b = runs2[0][1], runs2[1][0]
        print(f"  two heaviest staves: {runs2}, gap columns {a+1}..{b-1} (width {b-a-1})")
        span_rows = []
        for y in range(h):
            if all(ink[y][x] for x in range(a+1, b)):
                span_rows.append(y)
        print(f"  rows with continuous ink across the gap: {span_rows if span_rows else 'NONE'}")
        # per-row ink fraction in gap
        best = max(range(h), key=lambda y: sum(ink[y][x] for x in range(a+1, b)))
        frac = sum(ink[best][x] for x in range(a+1, b))/(b-a-1)
        print(f"  best row {best}: {frac:.2f} of gap columns inked")
    # heavy stroke angle: principal axis of pixels darker than a stronger threshold
    pts = [(x, y) for y in range(h) for x in range(w) if g[y][x] < thr - 40]
    if pts:
        import math
        n = len(pts); mx_ = sum(p[0] for p in pts)/n; my_ = sum(p[1] for p in pts)/n
        sxx = sum((p[0]-mx_)**2 for p in pts)/n; syy = sum((p[1]-my_)**2 for p in pts)/n
        sxy = sum((p[0]-mx_)*(p[1]-my_) for p in pts)/n
        ang = 0.5*math.atan2(2*sxy, sxx-syy)
        print(f"  heavy-ink pixels (g<{thr-40}): {n}, principal axis angle from horizontal = {math.degrees(ang):.1f} deg")

if __name__ == '__main__':
    for p in sys.argv[2:]:
        analyse(p, int(sys.argv[1]))
