import sys
from PIL import Image, ImageOps
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1288/work/hires/cpc_1913--13_HU__HU_Jasz-Arokszalas_jolanka-112_adr.jpg').convert('RGB')
name,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
c=ImageOps.autocontrast(c,cutoff=1)
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save('crops/'+name+'.png')
