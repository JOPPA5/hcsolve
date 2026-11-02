import sys
from PIL import Image
im=Image.open('ciphers/hcp-1162/work/hires/cpc_1916-03-28_HU_Mezokovesd_HU_Szomolya_szomolya-25_adr.jpg').convert('RGB')
# usage: name x0 y0 x1 y1 scale
n,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save(f'ciphers/hcp-1162/work/crops/{n}.png')
