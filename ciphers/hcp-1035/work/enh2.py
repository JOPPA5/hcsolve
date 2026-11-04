import sys
from PIL import Image, ImageOps, ImageFilter
src,out,x0,y0,x1,y1,sc=sys.argv[1],sys.argv[2],*map(int,sys.argv[3:7]),float(sys.argv[7])
im=Image.open(src).convert('RGB').crop((x0,y0,x1,y1))
g=im.split()[2]
bg=g.filter(ImageFilter.GaussianBlur(25))
from PIL import ImageChops
d=ImageChops.subtract(bg,g)
d=ImageOps.autocontrast(d,cutoff=0.5)
d=ImageOps.invert(d)
d=d.resize((int(d.width*sc),int(d.height*sc)),Image.LANCZOS)
d.save(out)
