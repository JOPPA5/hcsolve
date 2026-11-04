import sys
from PIL import Image
src,out,x0,y0,x1,y1,s=sys.argv[1],sys.argv[2],*map(float,sys.argv[3:8])
im=Image.open(src)
# coordinates given in 1600-wide overview scale
f=im.width/1600
c=im.crop((int(x0*f),int(y0*f),int(x1*f),int(y1*f)))
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save(out)
