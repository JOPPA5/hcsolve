import sys
from PIL import Image, ImageOps
a=sys.argv
im=Image.open('work/hires/cpc_1912-08-11_HU__HU_Jasz-Arokszalas_jolanka-30_adr.jpg').convert('RGB')
x0,y0,x1,y1=map(int,a[2:6]); s=float(a[6]) if len(a)>6 else 1
c=im.crop((x0,y0,x1,y1)); c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS); c.save(a[1])
