import sys
from PIL import Image
im=Image.open('../../work/hires/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-110_adr.jpg').convert('RGB')
name,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save(name+'.png'); print(c.size)
