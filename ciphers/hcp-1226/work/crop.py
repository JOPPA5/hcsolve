import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1226/work/hires/cpc_--17_HU__HU_Jasz-Arokszalas_jolanka-85_adr.jpg')
out='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1226/work/crops/'
# name x0 y0 x1 y1 scale
a=sys.argv[1:]
for i in range(0,len(a),6):
    n=a[i];x0,y0,x1,y1=map(int,a[i+1:i+5]);s=float(a[i+5])
    c=im.crop((x0,y0,x1,y1));c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS);c.save(out+n+'.png')
