import sys
from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1916-04-20_HU_Mezokovesd_HU_Szomolya_szomolya-29_adr.jpg').convert('RGB')
# name x0 y0 x1 y1 scale (coords on hires)
name,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c=ImageEnhance.Contrast(c).enhance(1.6)
c.save('crops/'+name+'.jpg',quality=90)
