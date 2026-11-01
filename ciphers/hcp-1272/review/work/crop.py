import sys
from PIL import Image
im=Image.open('../../work/hires/cpc_1912-04-30_HU__HU_Jasz-Arokszalas_jolanka-17_adr.jpg').convert('RGB')
# usage: name x0 y0 x1 y1 z
a=sys.argv[1:]
for i in range(0,len(a),6):
    n,x0,y0,x1,y1,z=a[i],*map(int,a[i+1:i+6])
    r=im.crop((x0,y0,x1,y1)); r=r.resize((r.width*z,r.height*z),Image.LANCZOS); r.save('crops/%s.png'%n)
