"""Suppress the later brown strike-outs: keep the red channel, stretched so that violet/blue pencil stays dark."""
import sys
from PIL import Image
im=Image.open('hires/cpc_1915-12-14_HU_Mezokovesd_HU_Szomolya_szomolya-11_adr.jpg').convert('RGB')
r,g,b=im.split()
# ink darkness in R; brown strike has R ~ 150-190, blue ink R < 130
for a in sys.argv[1:]:
    n,x0,y0,x1,y1,s=a.split(',');x0,y0,x1,y1=map(int,(x0,y0,x1,y1));s=float(s)
    c=r.crop((x0,y0,x1,y1)).point(lambda v: max(0,min(255,int((v-90)*255/90))))
    c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS);c.save('crops/%s.png'%n)
    c2=im.crop((x0,y0,x1,y1));c2=c2.resize((int(c2.width*s),int(c2.height*s)),Image.LANCZOS);c2.save('crops/%s_c.png'%n)
