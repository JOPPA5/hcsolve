import sys
from PIL import Image,ImageOps
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1270/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-72_adr.jpg').convert('RGB')
x0,y0,x1,y1,s=map(float,sys.argv[1:6]); out=sys.argv[6]
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
r,g,b=c.split()
# red channel carries green ink best
c=ImageOps.autocontrast(r,cutoff=1)
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS); c.save(out)
