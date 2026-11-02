import sys
from PIL import Image
i=Image.open('hires/cpc_1916-04-22_HU_Mezokovesd_HU_Szomolya_szomolya-30_adr.jpg').convert('RGB')
# name x0 y0 x1 y1 in overview px; scale
n,a,b,c,d=sys.argv[1],*map(float,sys.argv[2:6]); s=float(sys.argv[6]) if len(sys.argv)>6 else 1.3
f=3468/1500
j=i.crop(tuple(int(v*f) for v in (a,b,c,d)))
j=j.resize((int(j.width*s),int(j.height*s)),Image.LANCZOS); j.save('crops/%s.png'%n); print(j.size)
