import sys
from PIL import Image
im=Image.open(sys.argv[1]); s=3468/1024
x0,y0,x1,y1=map(float,sys.argv[3:7]); f=float(sys.argv[7]) if len(sys.argv)>7 else 1
c=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
c=c.resize((int(c.width*f),int(c.height*f))); c.save(sys.argv[2])
