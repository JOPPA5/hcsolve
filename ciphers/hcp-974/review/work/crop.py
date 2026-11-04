import sys
from PIL import Image
src, out, x0,y0,x1,y1, rot, scale = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:7]), int(sys.argv[7]), float(sys.argv[8])
im = Image.open(src).crop((x0,y0,x1,y1))
if rot: im = im.rotate(-rot, expand=True)
im = im.resize((int(im.width*scale), int(im.height*scale)), Image.LANCZOS)
im.save(out)
