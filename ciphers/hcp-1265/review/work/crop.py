import sys
from PIL import Image, ImageOps
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1265/work/hires/cpc_--17_HU__HU_Jasz-Arokszalas_jolanka-86_adr.jpg').convert('RGB')
n,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:6]),float(sys.argv[6])
c=im.crop((x0,y0,x1,y1)); c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
ImageOps.autocontrast(c,cutoff=1).save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1265/review/work/crops/%s.png'%n)
