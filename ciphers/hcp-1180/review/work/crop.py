import sys
from PIL import Image
im=Image.open(sys.argv[1]); s=im.size[0]/1024
x0,y0,x1,y1=[float(v) for v in sys.argv[2:6]]; f=float(sys.argv[7]) if len(sys.argv)>7 else 1.0
c=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
if len(sys.argv)>8: c=c.rotate(int(sys.argv[8]),expand=True)
c=c.resize((int(c.size[0]*f),int(c.size[1]*f)))
c.save(sys.argv[6])
