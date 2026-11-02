import sys
from PIL import Image, ImageOps
im=Image.open('hires/cpc_1916-04-20_HU_Mezokovesd_HU_Szomolya_szomolya-29_adr.jpg').convert('RGB')
name,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
r,g,b=c.split()
# blue ink darkens red channel; grey print/brown less separated: use r-b
c2=ImageOps.autocontrast(r)
c2=c2.resize((int(c2.width*s),int(c2.height*s)),Image.LANCZOS)
c2.save('crops/'+name+'.jpg',quality=90)
