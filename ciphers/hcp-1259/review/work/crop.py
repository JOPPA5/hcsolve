import sys
from PIL import Image
# usage: crop.py name x0 y0 x1 y1 scale [rot]
a=sys.argv
im=Image.open('work/hires/cpc_1912-04-04_HU__HU_Jasz-Arokszalas_jolanka-14_adr.jpg').convert('RGB')
c=im.crop(tuple(int(v) for v in a[2:6]))
s=float(a[6]); c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
if len(a)>7: c=c.rotate(int(a[7]),expand=True)
c.save('review/work/'+a[1]+'.png')
