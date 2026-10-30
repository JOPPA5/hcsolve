import sys
from PIL import Image, ImageOps
src, out, x0, y0, x1, y1, s = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:8])
im = Image.open(src).convert('RGB').crop((x0, y0, x1, y1))
px=[]
for R,G,B in im.getdata():
    dark = 255-(R+G+B)/3
    viol = (R+B)/2 - G   # violet ink > 0, grey watermark ~0
    px.append(int(max(0,min(255, 255 - max(0,viol)*6*min(1,dark/40)))))
o=Image.new('L',im.size); o.putdata(px)
o=ImageOps.autocontrast(o,cutoff=0.5).resize(((x1-x0)*s,(y1-y0)*s),Image.LANCZOS)
o.save(out)
