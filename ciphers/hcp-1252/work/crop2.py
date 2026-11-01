import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1252/work/hires/cpc_1913-06-13_HU__HU_Jasz-Arokszalas_jolanka-37_adr.jpg')
out='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1252/work/crops/'
for spec in sys.argv[1:]:
    n,x0,y0,x1,y1,s=spec.split(',')
    x0,y0,x1,y1,s=int(x0),int(y0),int(x1),int(y1),float(s)
    im.crop((x0,y0,x1,y1)).resize((int((x1-x0)*s),int((y1-y0)*s)),Image.LANCZOS).save(out+n+'.png')
