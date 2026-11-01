import sys
from PIL import Image, ImageOps
src='hires/cpc_--17_HU__HU_Jasz-Arokszalas_jolanka-86_adr.jpg'
im=Image.open(src).convert('RGB')
# name x0 y0 x1 y1 scale
n,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:6]),float(sys.argv[6])
c=im.crop((x0,y0,x1,y1)); c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c=ImageOps.autocontrast(c,cutoff=1); c.save('crops/%s.png'%n)
