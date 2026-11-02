import sys
from PIL import Image
# usage: rcrop.py out x0 y0 x1 y1 scale [rot]
src='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1149/work/hires/cpc_1916-04-26_HU_Mezokovesd_HU_Szomolya_szomolya-32_adr.jpg'
a=sys.argv
im=Image.open(src).convert('RGB')
x0,y0,x1,y1=map(int,a[2:6]); s=float(a[6])
c=im.crop((x0,y0,x1,y1))
if len(a)>7: c=c.rotate(int(a[7]),expand=True)
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save('crops/'+a[1]+'.png')
