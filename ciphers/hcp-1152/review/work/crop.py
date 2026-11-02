import sys
from PIL import Image
a=Image.open('../../work/hires/cpc_1915-12-05_HU_Mezokovesd_HU_Szomolya_szomolya-09_adr.jpg').convert('RGB')
n,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
c=a.crop((int(x0),int(y0),int(x1),int(y1)))
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS); c.save(n); print(n,c.size)
