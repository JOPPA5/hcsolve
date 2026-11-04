import sys
from PIL import Image
im=Image.open(sys.argv[1]); W,H=im.size
x0,y0,x1,y1=[float(v) for v in sys.argv[2:6]]; s=float(sys.argv[7])
c=im.crop((int(x0*W),int(y0*H),int(x1*W),int(y1*H)))
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS); c.save(sys.argv[6])
