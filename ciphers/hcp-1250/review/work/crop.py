from PIL import Image, ImageOps
import sys
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1250/work/hires/cpc_1913-06-16_HU__HU_Jasz-Arokszalas_jolanka-38_adr.jpg').convert('RGB')
out='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1250/review/work/crops/'
a=sys.argv[1:]
for i in range(0,len(a),6):
    n,x0,y0,x1,y1,s=a[i],*map(float,a[i+1:i+6])
    c=im.crop((int(x0),int(y0),int(x1),int(y1)))
    c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
    g=ImageOps.autocontrast(c.split()[1],cutoff=1); g.save(out+n+'.png')
