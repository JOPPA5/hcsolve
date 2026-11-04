import sys
from PIL import Image
src, out, x0,y0,x1,y1, scale = sys.argv[1], sys.argv[2], *map(float, sys.argv[3:8])
im = Image.open(src)
c = im.crop((int(x0),int(y0),int(x1),int(y1)))
rot = sys.argv[8] if len(sys.argv)>8 else '0'
if rot!='0': c = c.rotate(int(rot), expand=True)
c = c.resize((int(c.width*scale), int(c.height*scale)), Image.LANCZOS)
c.save(out)
