import sys
from PIL import Image, ImageOps, ImageEnhance
src, x0,y0,x1,y1, scale, out = sys.argv[1], *map(int, sys.argv[2:6]), int(sys.argv[6]), sys.argv[7]
im = Image.open(src).convert('RGB').crop((x0,y0,x1,y1))
im = im.resize((im.width*scale, im.height*scale), Image.LANCZOS)
if len(sys.argv) > 8:
    g = ImageOps.grayscale(im); g = ImageOps.autocontrast(g, cutoff=2); im = g
im.save(out)
