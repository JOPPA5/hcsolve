import sys
from PIL import Image
im=Image.open('work/hires/cpc_--22_HU__HU_Jasz-Arokszalas_jolanka-87_adr.jpg').convert('RGB')
n,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0),int(y0),int(x1),int(y1)));c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS);c.save(f'review/work/c/{n}.png');print(c.size)
