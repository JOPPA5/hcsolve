import sys
from PIL import Image
# usage: crop.py name x0 y0 x1 y1 scale [red]
src='work/hires/cpc_1915-12-14_HU_Mezokovesd_HU_Szomolya_szomolya-11_%s.jpg'
a=sys.argv
side=a[1]; n=a[2]; x0,y0,x1,y1=map(int,a[3:7]); s=float(a[7])
im=Image.open(src%side).convert('RGB').crop((x0,y0,x1,y1))
if len(a)>8: im=im.split()[0].convert('RGB')
im=im.resize((int(im.width*s),int(im.height*s)),Image.LANCZOS); im.save('review/work/%s.png'%n)
