import sys
from PIL import Image
im=Image.open(sys.argv[1]); s=im.size[0]/1400
x0,y0,x1,y1=[int(float(v)*s) for v in sys.argv[2:6]]; f=float(sys.argv[6])
c=im.crop((x0,y0,x1,y1)); c=c.resize((int(c.size[0]*f),int(c.size[1]*f)),Image.LANCZOS); c.save(sys.argv[7])
