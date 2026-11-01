import sys
from PIL import Image, ImageEnhance
im=Image.open('../../work/hires/cpc_1914-06-10_HU__HU_Jasz-Arokszalas_jolanka-54_adr.jpg').convert('RGB')
# usage: name x0 y0 x1 y1 scale [rot]
n,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
if len(sys.argv)>7:c=c.rotate(float(sys.argv[7]),expand=True)
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c=ImageEnhance.Contrast(c).enhance(1.4)
c.save('crops/%s.png'%n)
