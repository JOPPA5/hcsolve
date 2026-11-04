import sys
from PIL import Image, ImageOps
src, out, x0,y0,x1,y1, sc, rot = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:9])
im = Image.open(src).convert('L').crop((x0,y0,x1,y1))
im = ImageOps.autocontrast(im)
im = im.resize((im.width*sc//10, im.height*sc//10))
if rot: im = im.rotate(rot, expand=True)
im.save(out)
