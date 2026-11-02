import sys
from PIL import Image, ImageOps
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1137/work/'
im=Image.open(d+'hires/cpc_1916-06-10_HU_Mezokovesd_HU_Szomolya_szomolya-39_adr.jpg').convert('RGB')
n,x0,y0,x1,y1=sys.argv[1],*map(int,sys.argv[2:6]); s=float(sys.argv[6]) if len(sys.argv)>6 else 2.5
c=im.crop((x0,y0,x1,y1)); c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c=ImageOps.autocontrast(c,cutoff=1); c.save(d+'crops/'+n+'.png')
