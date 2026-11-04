import sys
from PIL import Image
src,out,x0,y0,x1,y1,rot,scale=sys.argv[1:9]
im=Image.open(src).crop((int(x0),int(y0),int(x1),int(y1))).rotate(int(rot),expand=True)
s=float(scale); im=im.resize((int(im.width*s),int(im.height*s)),Image.LANCZOS)
im.save(out)
