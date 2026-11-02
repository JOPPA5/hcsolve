import sys
from PIL import Image
base='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1135/work/hires/cpc_1916-04-22_HU_Mezokovesd_HU_Szomolya_szomolya-30_%s.jpg'
# usage: crop.py name side x0 y0 x1 y1 scale (native px)
n,side=sys.argv[1:3]; a,b,c,d=map(int,sys.argv[3:7]); s=float(sys.argv[7])
i=Image.open(base%side).convert('RGB').crop((a,b,c,d))
i=i.resize((int(i.width*s),int(i.height*s)),Image.LANCZOS); i.save('crops/%s.png'%n); print(i.size)
