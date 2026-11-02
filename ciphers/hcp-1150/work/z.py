import sys
from PIL import Image
im=Image.open('work/crops/nopm.png')
o=Image.open('work/hires/cpc_1916-06-12_HU_Mezokovesd_HU_Szomolya_szomolya-40_adr.jpg')
a=sys.argv
box=tuple(map(int,a[2:6]));s=int(a[6]) if len(a)>6 else 3
I=o if len(a)>7 else im
c=I.crop(box);c=c.resize((c.width*s,c.height*s),Image.LANCZOS);c.save('work/crops/%s.png'%a[1])
