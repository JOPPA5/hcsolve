import sys
from PIL import Image, ImageOps
src, out, x0,y0,x1,y1,s = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:8])
im = Image.open(src).rotate(90, expand=True).convert('L')
im = ImageOps.autocontrast(im, cutoff=1)
c = im.crop((x0,y0,x1,y1)); c=c.resize((c.width*s,c.height*s), Image.LANCZOS); c.save(out)
