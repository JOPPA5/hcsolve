import sys
from PIL import Image
a='../../work/hires/cpc_1916-02-12_HU_Mezokovesd_HU_Szomolya_szomolya-17_adr.jpg'
im=Image.open(a).convert('RGB')
# usage: crop.py name x0 y0 x1 y1 scale [rot]
n,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:7])
c=im
if len(sys.argv)>7: c=c.rotate(int(sys.argv[7]),expand=True)
c=c.crop((x0,y0,x1,y1)); c=c.resize((c.width*s,c.height*s),Image.LANCZOS); c.save(n+'.png')
