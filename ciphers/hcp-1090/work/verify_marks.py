# Independent check: compare the hand transcription (work/transcription.txt) with ink marks detected
# automatically on the hi-res scan (work/blobs.json from work/blobs.py), column by column.
# Reports: symbol-sequence agreement, the smallest gap at a letter boundary and the largest gap inside a letter.
import json, re, sys
import numpy as np
here = sys.argv[1]
b = [r for r in json.load(open(here + '/blobs.json')) if r['y1'] - r['y0'] >= 7 and r['x'] < 1600]
lines = json.load(open(here + '/lines.json'))           # fitted lines for c01..c15 (index 0 = c01)
lines[0] = [74 - 0.0246 * 100, 0.0246]                  # c01 refitted by hand (drifts right)
spec = {('c%02d' % (i + 1)): tuple(l) for i, l in enumerate(lines)}
spec['c00'] = (54 - 0.043 * 1654, 0.043)
def col_of(r):
    best = None; bd = 1e9
    for c, (a, k) in spec.items():
        if c == 'c00' and r['y'] < 1600: continue
        d = abs(r['x'] - (a + k * r['y']))
        if d < bd: best, bd = c, d
    return best, bd
cols = {c: [] for c in spec}
for r in b:
    c, d = col_of(r)
    if d < 45: cols[c].append(r)
    elif 1370 < r['x'] < 1400 and r['y'] > 2050: cols['c14'].append(r)   # R written left of c14's foot
    else: print('unassigned mark', round(r['x']), round(r['y']), r['y1'] - r['y0'] + 1)
# drop marks that are not Morse: the grey script insertion in c02 (y 1026-1065), the grey loops,
# and the printed publisher logo at the bottom of c02 (y > 1990) -- listed explicitly
def is_excluded(c, r):
    h = r['y1'] - r['y0'] + 1
    if c == 'c02' and 1020 < r['y'] < 1070: return 'script letter'
    if h > 75 and r['x1'] - r['x0'] > 40: return 'loop/logo'
    if c == 'c02' and r['y'] > 1990: return 'logo'
    return None
trans = {}
for line in open(here + '/transcription.txt'):
    m = re.match(r'(c\d\d): (.*)', line)
    if m: trans[m.group(1)] = m.group(2)
ok = True
for c in sorted(trans, reverse=True):
    marks = sorted(cols[c], key=lambda r: r['y'])
    kept = []
    for r in marks:
        e = is_excluded(c, r)
        if e: print('  %s: excluded %s at y=%d (h=%d)' % (c, e, r['y'], r['y1'] - r['y0'] + 1)); continue
        kept.append(r)
    # merge fragments touching (gap <= 4)
    merged = []
    for r in kept:
        if merged and r['y0'] - merged[-1]['y1'] <= 4 and abs(r['x'] - merged[-1]['x']) < 20:
            m = merged[-1]; m['y1'] = max(m['y1'], r['y1'])
        else: merged.append(dict(r))
    sym = ''.join('.' if r['y1'] - r['y0'] + 1 <= 24 else '-' for r in merged)
    letters = [t for t in trans[c].replace('/', ' ').replace('{', '').replace('}', '').split() if t != '[u:]']
    want = ''.join(letters)
    # the c10 insertion loop and c05 insertion loop sit beside the column: sort by y works for them
    status = 'OK' if sym == want else 'DIFF'
    if status == 'DIFF': ok = False
    print(c, status, 'detected', sym, 'transcribed', want)
    if sym == want:
        gaps = [merged[i + 1]['y0'] - merged[i]['y1'] for i in range(len(merged) - 1)]
        pos = 0; inner = []; bound = []
        for li, L in enumerate(letters):
            for j in range(len(L) - 1): inner.append(gaps[pos + j])
            pos += len(L)
            if li < len(letters) - 1: bound.append(gaps[pos - 1])
        print('    max gap inside letters %d, min gap between letters %d' % (max(inner) if inner else 0, min(bound) if bound else 0))
print('ALL OK' if ok else 'MISMATCH')
