from PIL import Image, ImageEnhance
import sys
im=Image.open('hires/cpc_-02-_HU__HU_Jasz-Arokszalas_jolanka-92_adr.jpg').convert('RGB')
# usage: x0 y0 x1 y1 scale name
x0,y0,x1,y1,s=map(float,sys.argv[1:6]); n=sys.argv[6]
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
c=ImageEnhance.Contrast(c).enhance(1.7).resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save(f'crops/{n}.jpg',quality=88)
