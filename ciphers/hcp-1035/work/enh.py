import sys
from PIL import Image, ImageOps
src,out,x0,y0,x1,y1,sc=sys.argv[1],sys.argv[2],*map(int,sys.argv[3:7]),float(sys.argv[7])
im=Image.open(src).crop((x0,y0,x1,y1))
r,g,b=im.split()
g=ImageOps.autocontrast(b,cutoff=1)
g=g.resize((int(g.width*sc),int(g.height*sc)),Image.LANCZOS)
g.save(out)
