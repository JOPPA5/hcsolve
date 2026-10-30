import sys
from PIL import Image, ImageOps
im = Image.open(sys.argv[1]).convert('L')
out = sys.argv[2]
x0,y0,x1,y1,s = map(int, sys.argv[3:8])
c = ImageOps.autocontrast(im.crop((x0,y0,x1,y1)), cutoff=1)
c = c.resize(((x1-x0)*s,(y1-y0)*s), Image.LANCZOS)
c.save(out)
