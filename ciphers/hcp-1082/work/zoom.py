import sys
from PIL import Image
src='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1082/work/hires/cpc_1942-08-27_FR_Loiret,-Gare-des-Aubres_FR_Nantes__adr.jpg'
im=Image.open(src)
x0,y0,x1,y1,f=map(int,sys.argv[1:6]); out=sys.argv[6]
c=im.crop((x0,y0,x1,y1)); c=c.resize((c.width*f//2,c.height*f//2),Image.LANCZOS); c.save(out)
