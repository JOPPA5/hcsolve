"""Machine aid: follow each Morse row (tracked centre line) and list ink runs
(start x, end x, length, max thickness). Used only to help the eye; the final
transcription is manual (work/transcription.txt)."""
import sys, json
from PIL import Image
import numpy as np
src = sys.argv[1]
starts = json.loads(sys.argv[2])
a = np.asarray(Image.open(src).convert('L')).astype(float)
for k, (x0, y0, x1, slope0) in enumerate(starts):
    yp = float(y0); slope = slope0; ys = {}
    for x in range(x0, x1):
        if x % 3 == 0 and x > x0:
            ylo, yhi = int(round(yp)) - 3, int(round(yp)) + 4
            w = np.clip(150 - a[ylo:yhi, x:x + 10], 0, None)
            if w.sum() > 150:
                cy = (w.sum(1) * np.arange(ylo, yhi)).sum() / w.sum(1).sum()
                pred = yp + 3 * slope; newy = 0.7 * pred + 0.3 * cy
                slope = 0.97 * slope + 0.03 * ((newy - yp) / 3); yp = newy
            else:
                yp += 3 * slope
        ys[x] = yp
    col = []
    for x in range(x0, x1):
        yc = int(round(ys[x])); c = a[yc - 4:yc + 5, x]
        col.append(((c < 125).sum(), c.min()))
    runs = []; inrun = False
    for i, (n, mn) in enumerate(col):
        if n > 0 and not inrun: s = i; inrun = True; th = 0
        if inrun:
            th = max(th, n)
            if n == 0:
                runs.append((x0 + s, x0 + i - 1, th)); inrun = False
    if inrun: runs.append((x0 + s, x1, th))
    out = []
    for s, e, th in runs:
        L = e - s + 1
        sym = 'B' if th >= 6 and L <= 14 else ('.' if L <= 4 else ('-' if L <= 14 else '='))
        out.append('%s%d' % (sym, L))
    print('R%02d y%d:' % (k + 1, y0), ' '.join(out))
