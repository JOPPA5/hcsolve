import sys
from PIL import Image
base='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1228/'
im=Image.open(base+'work/hires/cpc_1913-09-07_HU__HU_Jasz-Arokszalas_jolanka-42_adr.jpg').convert('RGB')
# usage: name x0 y0 x1 y1 scale
n,x0,y0,x1,y1,s=sys.argv[1:7]
c=im.crop((int(x0),int(y0),int(x1),int(y1)));s=float(s)
c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS).save(base+'review/work/'+n+'.png')
