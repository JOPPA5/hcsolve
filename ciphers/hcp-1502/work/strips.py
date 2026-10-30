"""Track each Morse row across the scan and save straightened, enlarged strips
(reading aid only; the reading itself is done by eye on these strips and on raw crops)."""
import sys, json
from PIL import Image, ImageDraw
import numpy as np
src, outdir = sys.argv[1], sys.argv[2]
import os
K = int(os.environ.get("K", 4)); SEG = int(os.environ.get("SEG", 250))
starts = json.loads(sys.argv[3])       # list of [x0, y0, x1]
im = Image.open(src).convert('RGB')
a = np.asarray(im.convert('L')).astype(float)
rgb = np.asarray(im)
H, W = a.shape
paths = []
for k, (x0, y0, x1) in enumerate(starts):
    yp = float(y0); slope = float(sys.argv[4]) if len(sys.argv)>4 else 0.0; ys = {}
    for x in range(x0, x1):
        if x % 3 == 0 and x > x0:
            ylo, yhi = int(round(yp)) - 3, int(round(yp)) + 4
            win = a[ylo:yhi, x:x + 10]
            w = np.clip(150 - win, 0, None)
            if w.sum() > 150:
                cy = (w.sum(1) * np.arange(ylo, yhi)).sum() / w.sum(1).sum()
                pred = yp + 3 * slope
                newy = 0.7 * pred + 0.3 * cy
                slope = 0.97 * slope + 0.03 * ((newy - yp) / 3)
                yp = newy
            else:
                yp += 3 * slope
        ys[x] = yp + (x % 3) * slope
    paths.append(ys)
    # straightened strip, 9 px above / below centre
    cols = []
    for x in range(x0, x1):
        yc = int(round(ys[x]))
        cols.append(rgb[yc - 9:yc + 10, x])
    strip = np.stack(cols, 1)
    img = Image.fromarray(strip).resize((strip.shape[1] * K, strip.shape[0] * K), Image.LANCZOS)
    seg = SEG * K
    n = (img.width + seg - 1) // seg
    canvas = Image.new('RGB', (seg, n * (img.height + 18)), 'white')
    d = ImageDraw.Draw(canvas)
    for i in range(n):
        piece = img.crop((i * seg, 0, min((i + 1) * seg, img.width), img.height))
        y = i * (img.height + 18)
        d.text((2, y), 'row %d  x=%d..%d' % (k + 1, x0 + i * SEG, min(x0 + (i + 1) * SEG, x1)), fill='red')
        for t in range(0, SEG, 5):
            d.line(((t * K, y + (12 if t % 10 else 6)), (t * K, y + 17)), fill="blue" if t % 50 else "red")
        canvas.paste(piece, (0, y + 18))
    canvas.save('%s/row%02d.png' % (outdir, k + 1))
# overlay of tracked paths on the scan
ov = im.copy(); d = ImageDraw.Draw(ov)
for k, ys in enumerate(paths):
    pts = [(x, ys[x]) for x in sorted(ys)]
    d.line(pts, fill=(255, 0, 0), width=1)
    d.text((pts[0][0] - 25, pts[0][1] - 5), str(k + 1), fill=(255, 0, 0))
ov.resize((W * 2, H * 2)).save(outdir + '/overlay.png')
