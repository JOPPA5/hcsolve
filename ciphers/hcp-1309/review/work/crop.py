import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1309/work/hires/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-99_adr.jpg').convert('RGB')
# usage: name x0 y0 x1 y1 scale (coords in hires px)
a=sys.argv[1:]
for i in range(0,len(a),6):
    n,x0,y0,x1,y1,s=a[i],*map(float,a[i+1:i+6])
    c=im.crop((int(x0),int(y0),int(x1),int(y1)));c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS);c.save('crops/'+n+'.png')
