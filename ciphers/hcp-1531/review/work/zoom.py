import sys
from PIL import Image, ImageOps
im=Image.open(sys.argv[1]).convert('L')
x0,y0,x1,y1=map(int,sys.argv[2].split(','))
s=int(sys.argv[3])
c=im.crop((x0,y0,x1,y1)); c=c.resize((c.width*s,c.height*s),Image.LANCZOS)
if len(sys.argv)>5: c=ImageOps.autocontrast(c,cutoff=2)
c.save(sys.argv[4])
