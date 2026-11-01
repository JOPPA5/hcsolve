import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1257/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-69_adr.jpg').convert('RGB')
out='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1257/review/work/crops/'
for a in sys.argv[1:]:
    n,x0,y0,x1,y1,s=a.split(',');c=im.crop((int(x0),int(y0),int(x1),int(y1)));s=float(s)
    c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS).save(out+n+'.jpg',quality=88)
