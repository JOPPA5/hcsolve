import sys
from PIL import Image,ImageChops,ImageOps
im=Image.open('hires/cpc_1912-04-_HU__HU_Jasz-Arokszalas_jolanka-104_adr.jpg').convert('RGB')
n,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
b=[int(v*1.72) for v in (x0,y0,x1,y1)]
c=im.crop(b); r,g,bb=c.split()
d=ImageChops.subtract(r,g,1,0)   # red minus green: ink, ignores brown spots
d=ImageOps.autocontrast(d,cutoff=1); d=ImageOps.invert(d)
d=d.resize((int(d.width*s),int(d.height*s)),Image.LANCZOS); d.save('crops/%s.png'%n)
