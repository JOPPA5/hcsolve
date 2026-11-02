import sys
from PIL import Image, ImageOps, ImageChops
src='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1292/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-75_adr.jpg'
im=Image.open(src).convert('RGB')
def crop(name,x0,y0,x1,y1,s=4,mode='ink'):
    c=im.crop((x0,y0,x1,y1))
    if mode=='ink':
        r,g,b=c.split()
        # green ink: low red; use red channel contrast
        o=ImageOps.autocontrast(r,cutoff=1)
    else: o=c
    o=o.resize((o.width*s,o.height*s),Image.LANCZOS)
    o.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1292/work/rev2/'+name+'.png')
a=sys.argv
crop(a[1],*map(int,a[2:6]),s=int(a[6]) if len(a)>6 else 4,mode=a[7] if len(a)>7 else 'ink')
