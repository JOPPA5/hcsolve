import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1221/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-66_adr.jpg').convert('RGB')
O='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1221/work/crops/'
# name x0 y0 x1 y1 scale
a=sys.argv[1:]
for i in range(0,len(a),6):
    n,x0,y0,x1,y1,s=a[i],*map(float,a[i+1:i+6])
    c=im.crop((int(x0),int(y0),int(x1),int(y1)))
    c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS).save(O+n+'.png')
