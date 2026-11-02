import sys
from PIL import Image
im=Image.open('work/hires/cpc_1913-01-_HU__HU_Jasz-Arokszalas_jolanka-113_adr.jpg').convert('RGB')
n,l,t,r,b,s=sys.argv[1],*map(float,sys.argv[2:7])
f=1.72
c=im.crop((int(l*f),int(t*f),int(r*f),int(b*f)));c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS);c.save(f'work/crops/{n}.png')
