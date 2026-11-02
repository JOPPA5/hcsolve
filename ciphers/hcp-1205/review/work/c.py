import sys,os
from PIL import Image,ImageOps
D='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1205/'
im=Image.open(D+'work/hires/cpc_--_HU__HU_Rakos-Palota-Ujfalu_jolanka-60_adr.jpg').convert('RGB')
a=sys.argv
if a[1]=='r': im=im.rotate(180); a=a[1:]
b=tuple(map(int,a[2:6])); s=float(a[6])
x=im.crop(b); x=x.resize((int(x.width*s),int(x.height*s)),Image.LANCZOS); x.save(D+'review/work/crops/'+a[1]+'.png')
