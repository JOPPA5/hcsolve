import sys
from PIL import Image, ImageOps, ImageFilter
src, out = sys.argv[1], sys.argv[2]
x0,y0,x1,y1,s = map(int, sys.argv[3:8])
im = Image.open(src).convert('RGB').crop((x0,y0,x1,y1))
r = im.split()[0].filter(ImageFilter.GaussianBlur(0.8))
r = r.resize((r.width*s, r.height*s), Image.BICUBIC)
r = ImageOps.autocontrast(r, cutoff=2)
r.save(out)
