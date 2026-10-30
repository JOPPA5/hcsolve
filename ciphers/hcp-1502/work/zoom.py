"""Save an enlarged crop with a pixel ruler (reading aid). usage: zoom.py src out x0 y0 x1 y1 scale"""
import sys
from PIL import Image, ImageDraw
src, out = sys.argv[1], sys.argv[2]
x0, y0, x1, y1, k = map(int, sys.argv[3:8])
im = Image.open(src).convert('RGB').crop((x0, y0, x1, y1))
im = im.resize(((x1 - x0) * k, (y1 - y0) * k), Image.LANCZOS)
c = Image.new('RGB', (im.width, im.height + 14), 'white'); c.paste(im, (0, 14))
d = ImageDraw.Draw(c)
for x in range(x0 - x0 % 5 + 5, x1, 5):
    X = (x - x0) * k
    d.line(((X, 8 if x % 10 else 0), (X, 14)), fill='red' if x % 50 == 0 else 'blue')
    if x % 10 == 0: d.text((X + 2, 0), str(x), fill='red')
for y in range(y0 - y0 % 5 + 5, y1, 5):
    Y = (y - y0) * k + 14
    d.line(((0, Y), (6, Y)), fill='red'); d.text((8, Y - 5), str(y), fill='red')
c.save(out)
