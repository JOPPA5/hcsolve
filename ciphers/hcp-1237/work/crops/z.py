import sys
from PIL import Image
sh=Image.open('crops/shear.png')
s=1.72
n,a,b,c,d,z=sys.argv[1],*map(float,sys.argv[2:7])
r=sh.crop((int(a*s),int(b*s),int(c*s),int(d*s))); r=r.resize((int(r.width*z),int(r.height*z)),Image.LANCZOS); r.save(f'crops/{n}.png')
