import sys
from PIL import Image
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1148/'
im=Image.open(d+'work/hires/cpc_1916-05-09_HU_Mezokovesd_HU_Szomolya_szomolya-34_adr.jpg')
n,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0),int(y0),int(x1),int(y1)));c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save(d+'review/work/c/%s.png'%n);print(c.size)
