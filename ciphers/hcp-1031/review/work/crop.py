import sys
from PIL import Image, ImageOps
src, out, x0,y0,x1,y1, rot, sc = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:9])
im = Image.open(src).crop((x0,y0,x1,y1))
if rot: im = im.rotate(rot, expand=True)
im = ImageOps.autocontrast(im.convert('L'), cutoff=1)
im = im.resize((im.width*sc//10, im.height*sc//10), Image.LANCZOS)
im.save(out)
