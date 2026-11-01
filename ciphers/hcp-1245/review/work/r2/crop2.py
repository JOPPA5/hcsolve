import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1245/work/hires/cpc_1912-03-20_HU__HU_Jasz-Arokszalas_jolanka-11_adr.jpg')
print(im.size)
a=sys.argv
for i in range(1,len(a),6):
    n=a[i];x0,y0,x1,y1=map(int,a[i+1:i+5]);s=float(a[i+5])
    c=im.crop((x0,y0,x1,y1));c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS);c.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1245/review/work/r2/'+n+'.png')
