import sys
from PIL import Image
im=Image.open('hires/cpc_1916-05-19_HU_Mezokovesd_HU_Szomolya_szomolya-36_adr.jpg').convert('RGB')
# name x0 y0 x1 y1 scale
def c(n,x0,y0,x1,y1,s=1.0):
    r=im.crop((x0,y0,x1,y1)); r=r.resize((int(r.width*s),int(r.height*s)),Image.LANCZOS); r.save('crops/%s.png'%n)
for a in sys.argv[1:]:
    p=a.split(','); c(p[0],*map(int,p[1:5]),float(p[5]) if len(p)>5 else 1.0)
