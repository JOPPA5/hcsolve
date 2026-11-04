import sys
from PIL import Image
src,out,x0,y0,x1,y1,s=sys.argv[1],sys.argv[2],*map(float,sys.argv[3:8])
im=Image.open(src).crop((int(x0),int(y0),int(x1),int(y1)))
im=im.resize((int(im.width*s),int(im.height*s)),Image.LANCZOS)
im.save(out)
