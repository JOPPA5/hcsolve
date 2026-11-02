import sys
from PIL import Image, ImageOps
im=Image.open('hires/cpc_1913-12-_HU__HU_Jasz-Arokszalas_jolanka-116_adr.jpg').convert('L')
# name x0 y0 x1 y1 scale
a=sys.argv[1:]
for i in range(0,len(a),6):
    n,x0,y0,x1,y1,s=a[i],*map(int,a[i+1:i+6])
    c=ImageOps.autocontrast(im.crop((x0,y0,x1,y1)),cutoff=0.5).resize(((x1-x0)*s,(y1-y0)*s),Image.BICUBIC)
    c.save(f'crops/{n}.png')
