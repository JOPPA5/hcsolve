import sys
from PIL import Image, ImageOps
src, out, x0, y0, x1, y1, s = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:8])
im = Image.open(src).convert('RGB').crop((x0, y0, x1, y1))
r,g,b = im.split()
# ink is bluish/violet: darker in R/G than B; watermark grey: equal
import itertools
px = []
for (R,G,B) in im.getdata():
    v = (R+G)/2 - 0.6*B  # low for bluish dark ink
    px.append(int(max(0,min(255, 255 - ( (B - (R+G)/2) *4 + (255-(R+G+B)/3)*0.5 )))))
o = Image.new('L', im.size); o.putdata(px)
o = ImageOps.autocontrast(o, cutoff=1)
o = o.resize(((x1-x0)*s,(y1-y0)*s), Image.LANCZOS)
o.save(out)
