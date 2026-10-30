import sys
from PIL import Image, ImageOps, ImageFilter, ImageChops
src, out = sys.argv[1], sys.argv[2]
x0,y0,x1,y1,s = map(int, sys.argv[3:8])
im = Image.open(src).convert('RGB').crop((x0,y0,x1,y1))
r,g,b = im.split()
# ink relatively bluer than sepia photo: b - r
d = ImageChops.subtract(b, r, scale=1, offset=128)
d = d.filter(ImageFilter.GaussianBlur(0.7))
d = ImageOps.autocontrast(d, cutoff=1)
d = ImageOps.invert(d)
d = d.resize((d.width*s, d.height*s), Image.BICUBIC)
d.save(out)
