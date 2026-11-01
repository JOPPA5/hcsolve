import sys
from PIL import Image, ImageOps
src='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1271/work/hires/cpc_1912-03-16_HU__HU_Jasz-Arokszalas_jolanka-10_adr.jpg'
im=Image.open(src).convert('RGB')
# args: name x0 y0 x1 y1 scale
n,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1271/work/crops/%s.png'%n)
