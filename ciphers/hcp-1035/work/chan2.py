import sys
from PIL import Image, ImageOps, ImageFilter
src,out,x0,y0,x1,y1,sc=sys.argv[1],sys.argv[2],*map(int,sys.argv[3:7]),float(sys.argv[7])
im=Image.open(src).convert('RGB').crop((x0,y0,x1,y1))
im=im.resize((int(im.width*sc),int(im.height*sc)),Image.BICUBIC).filter(ImageFilter.GaussianBlur(1.5))
px=im.load(); w,h=im.size
o=Image.new('L',(w,h))
op=o.load()
for y in range(h):
  for x in range(w):
    r,g,b=px[x,y]
    op[x,y]=max(0,min(255,255-3*(r-b-20)))
o=ImageOps.autocontrast(o,cutoff=1)
o.save(out)
