import sys
from PIL import Image
# usage: crop.py name x0 y0 x1 y1 scale  (full hires pixels)
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1245/work/hires/cpc_1912-03-20_HU__HU_Jasz-Arokszalas_jolanka-11_adr.jpg')
a=sys.argv
for i in range(1,len(a),6):
    n=a[i];x0,y0,x1,y1=map(int,a[i+1:i+5]);s=float(a[i+5])
    c=im.crop((x0,y0,x1,y1));c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS);c.save(n+'.png')
im2=im.copy();im2.thumbnail((1700,1100));im2.save('full.png')
