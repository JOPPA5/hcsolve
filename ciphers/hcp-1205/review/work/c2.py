import sys
from PIL import Image
D='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1205/'
a=sys.argv[1:]
f='pic' if a[0]=='p' else 'adr'
im=Image.open(D+'work/hires/cpc_--_HU__HU_Rakos-Palota-Ujfalu_jolanka-60_%s.jpg'%f).convert('RGB')
if a[0]=='p': im=im.rotate(90,expand=True)
if a[0]=='r': im=im.rotate(180)
b=tuple(map(int,a[2:6]));s=float(a[6])
x=im.crop(b);x=x.resize((int(x.width*s),int(x.height*s)),Image.LANCZOS);x.save(D+'review/work/crops2/'+a[1]+'.png');print(im.size,x.size)
