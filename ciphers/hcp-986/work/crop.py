import sys
from PIL import Image
src,out,x0,y0,x1,y1=sys.argv[1],sys.argv[2],*map(int,sys.argv[3:7])
s=3469/1024
im=Image.open(src).crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
im.save(out)
print(im.size)
