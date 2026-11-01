import sys
from PIL import Image, ImageOps
# usage: crop.py name x0 y0 x1 y1 scale
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1249/work/hires/cpc_1914-03-25_HU__HU_Jasz-Arokszalas_jolanka-51_adr.jpg').convert('RGB')
n,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:6]),float(sys.argv[6])
c=im.crop((x0,y0,x1,y1));c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c=ImageOps.autocontrast(c,cutoff=1)
c.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1249/work/crops/'+n+'.png')
