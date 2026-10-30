import sys
from PIL import Image
im=Image.open('hires/cpc_1912-04-_HU__HU_Jasz-Arokszalas_jolanka-104_adr.jpg').convert('RGB')
# name x0 y0 x1 y1 scale (display coords ×1.72)
n,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
b=[int(v*1.72) for v in (x0,y0,x1,y1)]
c=im.crop(b); c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS); c.save('crops/%s.png'%n)
