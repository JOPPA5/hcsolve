"""Reading aid: straightened, enlarged strip of one row along a fitted centre line.
usage: rowstrip.py address.jpg rows.json row_no x0 x1 out.png [K]"""
import sys, json
from PIL import Image, ImageDraw
import numpy as np
src, rj, k, x0, x1, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
K = int(sys.argv[7]) if len(sys.argv) > 7 else 6
coef = json.load(open(rj))[k - 1]['coef']
rgb = np.asarray(Image.open(src).convert('RGB'))
cols = []
for x in range(x0, x1):
    yc = int(round(np.polyval(coef, x)))
    cols.append(rgb[yc - 8:yc + 9, x])
strip = Image.fromarray(np.stack(cols, 1)).resize(((x1 - x0) * K, 17 * K), Image.LANCZOS)
c = Image.new('RGB', (strip.width, strip.height + 14), 'white'); c.paste(strip, (0, 14))
d = ImageDraw.Draw(c)
for x in range(x0 - x0 % 5 + 5, x1, 5):
    X = (x - x0) * K
    d.line(((X, 8 if x % 10 else 0), (X, 14)), fill='red' if x % 50 == 0 else 'blue')
    if x % 10 == 0: d.text((X + 2, 0), str(x), fill='red')
c.save(out)
