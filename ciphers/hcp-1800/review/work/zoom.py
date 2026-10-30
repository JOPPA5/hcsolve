import sys
from PIL import Image, ImageOps
src, out, x0, x1, y0, y1, s = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:8])
im = Image.open(src).convert("L").crop((840, 25, 925, 610)).rotate(-90, expand=True)
im = ImageOps.autocontrast(im, cutoff=1)
c = im.crop((x0, y0, x1, y1))
c.resize((c.width*s, c.height*s), Image.LANCZOS).save(out)
