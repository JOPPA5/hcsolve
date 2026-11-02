import sys
from PIL import Image, ImageOps
src='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1292/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-75_adr.jpg'
im=Image.open(src).convert('RGB')
print(im.size)
sc=im.size[0]/1024
# args: name x0 y0 x1 y1 (in 1024-preview coords) zoom
n,x0,y0,x1,y1,z=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0*sc),int(y0*sc),int(x1*sc),int(y1*sc))).split()[0]
c=ImageOps.autocontrast(c,cutoff=1)
c=c.resize((int(c.width*z),int(c.height*z)),Image.LANCZOS)
c.save(n+'.png');print(c.size)
