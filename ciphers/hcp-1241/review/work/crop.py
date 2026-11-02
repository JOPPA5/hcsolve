import sys
from PIL import Image
im=Image.open('../../work/hires/cpc_1912-05-12_HU__HU_Jasz-Arokszalas_jolanka-20_adr.jpg').convert('RGB')
print(im.size)
# usage name x0 y0 x1 y1 scale
a=sys.argv[1:]
for i in range(0,len(a),6):
    n,x0,y0,x1,y1,s=a[i],*map(int,a[i+1:i+6])
    c=im.crop((x0,y0,x1,y1)); c.resize((c.width*s,c.height*s),Image.LANCZOS).save('crops/%s.png'%n)
