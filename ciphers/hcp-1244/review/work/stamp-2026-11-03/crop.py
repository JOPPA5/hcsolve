import sys
from PIL import Image, ImageOps
src, out, x0,y0,x1,y1, scale = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:7]), float(sys.argv[7])
mode = sys.argv[8] if len(sys.argv)>8 else 'rgb'
im = Image.open(src).convert('RGB').crop((x0,y0,x1,y1))
if mode=='g': im = ImageOps.autocontrast(im.split()[1], cutoff=1)
elif mode=='b': im = ImageOps.autocontrast(im.split()[2], cutoff=1)
elif mode=='ac': im = ImageOps.autocontrast(im, cutoff=1)
im = im.resize((int(im.width*scale), int(im.height*scale)), Image.LANCZOS)
im.save(out)
