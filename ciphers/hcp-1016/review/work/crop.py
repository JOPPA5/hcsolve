import sys
from PIL import Image, ImageOps
src, out, x0,y0,x1,y1, s = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:8])
im = Image.open(src).convert('L').crop((x0,y0,x1,y1))
im = ImageOps.autocontrast(im, cutoff=1)
im = im.resize((im.width*s, im.height*s), Image.LANCZOS)
im.save(out)
