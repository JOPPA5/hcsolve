import sys
from PIL import Image
f='work/hires/cpc_1915-12-03_HU_Mezokovesd_HU_Szomolya_szomolya-08_adr.jpg'
im=Image.open(f)
a=sys.argv[1:]
n=a[0];x0,y0,x1,y1=map(int,a[1:5]);s=float(a[5]) if len(a)>5 else 2
c=im.crop((x0,y0,x1,y1));c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS);c.save('work/crops/%s.png'%n)
