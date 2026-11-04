import sys
from PIL import Image, ImageOps
src,out,x0,y0,x1,y1,sc,ch=sys.argv[1],sys.argv[2],*map(int,sys.argv[3:7]),float(sys.argv[7]),int(sys.argv[8])
im=Image.open(src).convert('RGB').crop((x0,y0,x1,y1))
r,g,b=im.split()
# brown ink: R-B difference large; grey stamp: R~B
import PIL.ImageChops as C
d=C.subtract(r,b)
d=ImageOps.autocontrast(d,cutoff=1); d=ImageOps.invert(d)
d=d.resize((int(d.width*sc),int(d.height*sc)),Image.LANCZOS)
d.save(out)
