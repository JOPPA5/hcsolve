import sys
from PIL import Image, ImageOps
im=Image.open(sys.argv[1]).convert('RGB')
x0,y0,x1,y1=map(int,sys.argv[3:7]); s=float(sys.argv[7])
c=im.crop((x0,y0,x1,y1))
mode=sys.argv[8] if len(sys.argv)>8 else 'rgb'
if mode=='r': c=ImageOps.autocontrast(c.split()[0],cutoff=1)
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save(sys.argv[2])
