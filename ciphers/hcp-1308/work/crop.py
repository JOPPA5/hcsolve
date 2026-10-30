import sys
from PIL import Image, ImageOps
im=Image.open(sys.argv[1]); x0,y0,x1,y1=map(int,sys.argv[2:6]); s=float(sys.argv[6]); o=sys.argv[7]
r=int(sys.argv[8]) if len(sys.argv)>8 else 0
c=im.crop((x0,y0,x1,y1))
if r: c=c.rotate(r,expand=True)
c=ImageOps.autocontrast(c.convert('L'),cutoff=1).resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save(o)
