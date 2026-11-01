import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1282/work/hires/cpc_-04-11_HU__HU_Jasz-Arokszalas_jolanka-94_adr.jpg').convert('RGB')
n,x0,y0,x1,y1=sys.argv[1],*map(int,sys.argv[2:6]); s=float(sys.argv[6]) if len(sys.argv)>6 else 3
c=im.crop((x0,y0,x1,y1)); c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save(f'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1282/review/work/{n}.png')
