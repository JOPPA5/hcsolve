import sys
from PIL import Image
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1309/work/'
im=Image.open(d+'hires/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-99_adr.jpg').convert('RGB')
name,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save(d+'crops/'+name+'.png')
