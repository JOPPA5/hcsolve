"""reviewer crops: name x0 y0 x1 y1 scale [v]  (run from cipher dir)"""
import sys
from PIL import Image, ImageOps
im=Image.open('work/hires/cpc_1913-12-_HU__HU_Jasz-Arokszalas_jolanka-116_adr.jpg').convert('RGB')
a=sys.argv[1:]
for i in range(0,len(a),6):
    n,x0,y0,x1,y1,s=a[i],*map(int,a[i+1:i+6])
    c=im.crop((x0,y0,x1,y1)).resize(((x1-x0)*s,(y1-y0)*s),Image.LANCZOS)
    c=ImageOps.autocontrast(c,cutoff=0.3)
    c.save(f'review/work/crops/{n}.png')
