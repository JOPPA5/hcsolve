import sys
from PIL import Image
im=Image.open('hires/cpc_1915-12-14_HU_Mezokovesd_HU_Szomolya_szomolya-11_adr.jpg')
# name x0 y0 x1 y1 scale
for a in sys.argv[1:]:
    n,x0,y0,x1,y1,s=a.split(',');x0,y0,x1,y1=map(int,(x0,y0,x1,y1));s=float(s)
    c=im.crop((x0,y0,x1,y1));c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS);c.save('crops/%s.png'%n)
