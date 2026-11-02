import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1150/work/hires/cpc_1916-06-12_HU_Mezokovesd_HU_Szomolya_szomolya-40_adr.jpg').convert('RGB')
a=sys.argv
b=tuple(map(int,a[2:6]));s=int(a[6]) if len(a)>6 else 3
c=im.crop(b);c.resize((c.width*s,c.height*s),Image.LANCZOS).save(a[1]+'.png')
