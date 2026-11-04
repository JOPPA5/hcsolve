import sys
from PIL import Image
src, out, rot, x0,y0,x1,y1, sc = sys.argv[1], sys.argv[2], int(sys.argv[3]), *map(int, sys.argv[4:8]), float(sys.argv[8])
im = Image.open(src)
im = im.crop((x0,y0,x1,y1))
if rot: im = im.rotate(rot, expand=True)
im = im.resize((int(im.width*sc), int(im.height*sc)), Image.LANCZOS)
im.save(out)
