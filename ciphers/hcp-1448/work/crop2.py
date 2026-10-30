import sys
from PIL import Image, ImageOps
src, out = sys.argv[1], sys.argv[2]
x0,y0,x1,y1,s = map(int, sys.argv[3:8])
im = Image.open(src).convert('RGB').crop((x0,y0,x1,y1))
im = im.resize((im.width*s, im.height*s), Image.LANCZOS)
# use red channel min style: darkness
r,g,b = im.split()
g2 = ImageOps.autocontrast(r, cutoff=0.5)
g2.save(out)
