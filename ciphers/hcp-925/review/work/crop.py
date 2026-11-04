import sys
from PIL import Image
src, out, x0, y0, x1, y1, s = sys.argv[1], sys.argv[2], *map(float, sys.argv[3:8])
k = 3410/1600
im = Image.open(src).crop((int(x0*k), int(y0*k), int(x1*k), int(y1*k)))
im = im.resize((int(im.width*s), int(im.height*s)), Image.LANCZOS)
im.save(out)
