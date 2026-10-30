import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1307/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-79_adr.jpg')
out='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1307/work/crops/'
# name x0 y0 x1 y1 scale
n,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0),int(y0),int(x1),int(y1)));c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS);c.save(out+n+'.png')
