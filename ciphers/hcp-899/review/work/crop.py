import sys
from PIL import Image, ImageEnhance
src, out, x0, y0, x1, y1, s = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:8])
im = Image.open(src).convert('RGB').crop((x0, y0, x1, y1))
im = im.resize(((x1-x0)*s, (y1-y0)*s), Image.LANCZOS)
im = ImageEnhance.Contrast(im).enhance(1.8)
im.save(out)
