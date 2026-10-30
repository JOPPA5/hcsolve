import sys
from PIL import Image
src, out, x0,y0,x1,y1, sc = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:8])
rot = int(sys.argv[8]) if len(sys.argv)>8 else 0
im = Image.open(src).crop((x0,y0,x1,y1))
if rot: im = im.rotate(rot, expand=True)
im = im.resize((im.width*sc, im.height*sc), Image.LANCZOS)
im.save(out)
