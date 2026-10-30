import sys
from PIL import Image, ImageOps, ImageFilter
src, out = sys.argv[1], sys.argv[2]
x0,y0,x1,y1,s = map(int, sys.argv[3:8])
im = Image.open(src).convert('RGB').crop((x0,y0,x1,y1))
r,g,b = im.split()
# ink is dark in all channels; use min channel
from PIL import ImageChops
m = ImageChops.darker(ImageChops.darker(r,g),b)
m = m.resize((m.width*s, m.height*s), Image.BICUBIC)
m = ImageOps.equalize(m)
m.save(out)
