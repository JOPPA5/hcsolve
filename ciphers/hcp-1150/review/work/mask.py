import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1150/work/hires/cpc_1916-06-12_HU_Mezokovesd_HU_Szomolya_szomolya-40_adr.jpg').convert('RGB')
a=sys.argv;b=tuple(map(int,a[2:6]));s=int(a[6])
c=im.crop(b);p=c.load()
for y in range(c.height):
  for x in range(c.width):
    r,g,bb=p[x,y]
    if bb-g<12 and r<160: p[x,y]=(232,222,215)
c.resize((c.width*s,c.height*s),Image.LANCZOS).save(a[1]+'.png')
