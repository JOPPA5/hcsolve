import sys
from PIL import Image
f='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1317/work/hires/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-110_adr.jpg'
im=Image.open(f).convert('RGB')
x0,y0,x1,y1,s,out=sys.argv[1:7]
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
s=float(s); c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS); c.save(out)
