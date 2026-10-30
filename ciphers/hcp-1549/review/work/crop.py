import sys
from PIL import Image
src, out, x0,y0,x1,y1, sc = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:8])
im = Image.open(src).crop((x0,y0,x1,y1))
im = im.resize((im.width*sc, im.height*sc), Image.LANCZOS)
im.save(out)
print(Image.open(src).size, im.size)
