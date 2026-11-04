import sys
from PIL import Image
src, out, x0,y0,x1,y1 = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:7])
s = float(sys.argv[7]) if len(sys.argv)>7 else 1.0
mode = sys.argv[8] if len(sys.argv)>8 else ''
im = Image.open(src).convert('RGB').crop((x0,y0,x1,y1))
if mode=='blue':
    r,g,b = im.split()
    from PIL import ImageChops, ImageOps
    d = ImageChops.subtract(b, r, scale=1.0, offset=0)
    im = ImageOps.invert(ImageOps.autocontrast(d)).convert('RGB')
im = im.resize((int(im.width*s), int(im.height*s)), Image.LANCZOS)
im.save(out)
