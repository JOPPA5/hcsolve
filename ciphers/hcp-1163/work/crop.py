import sys
from PIL import Image
im=Image.open('hires/cpc_1916-02-26_HU_Mezokovesd_HU_Szomolya_szomolya-20_adr.jpg').convert('RGB')
s=3468/1800
# name x0 y0 x1 y1 in thumb coordinates, zoom
name,x0,y0,x1,y1,z=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
c=c.resize((int(c.width*z),int(c.height*z)),Image.LANCZOS)
c.save('crops/%s.png'%name);print(c.size)
