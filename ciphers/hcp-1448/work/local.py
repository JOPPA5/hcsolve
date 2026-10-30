import sys
from PIL import Image, ImageOps, ImageFilter, ImageChops
src, out = sys.argv[1], sys.argv[2]
x0,y0,x1,y1,s = map(int, sys.argv[3:8])
im = Image.open(src).convert('L').crop((x0,y0,x1,y1))
im = im.resize((im.width*s, im.height*s), Image.BICUBIC)
bg = im.filter(ImageFilter.GaussianBlur(6*s))
d = ImageChops.subtract(bg, im, scale=1, offset=0)  # ink darker than local bg
d = d.filter(ImageFilter.GaussianBlur(s*0.4))
d = ImageOps.autocontrast(d, cutoff=1)
ImageOps.invert(d).save(out)
