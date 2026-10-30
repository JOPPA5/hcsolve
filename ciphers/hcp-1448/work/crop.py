import sys
from PIL import Image, ImageOps, ImageEnhance
src, out, x0,y0,x1,y1, s = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:8])
im = Image.open(src).convert('RGB').crop((x0,y0,x1,y1))
im = im.resize((im.width*s, im.height*s), Image.LANCZOS)
g = ImageOps.autocontrast(im.convert('L'), cutoff=1)
g = ImageEnhance.Contrast(g).enhance(1.8)
g.save(out)
