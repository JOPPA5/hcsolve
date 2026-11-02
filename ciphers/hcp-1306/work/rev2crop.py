import sys
from PIL import Image, ImageEnhance, ImageOps
P='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1306/work/'
im=Image.open(P+'hires/cpc_1914-03-05_HU__HU_Jasz-Arokszalas_jolanka-49_adr.jpg').convert('RGB')
# usage: x0 y0 x1 y1 scale name [mode] [rot]
a=sys.argv[1:]
x0,y0,x1,y1=map(int,a[:4]); s=float(a[4]); name=a[5]; mode=a[6] if len(a)>6 else 'rgb'; rot=int(a[7]) if len(a)>7 else 0
c=im.crop((x0,y0,x1,y1))
if rot: c=c.rotate(rot,expand=True)
if mode=='r': c=ImageOps.autocontrast(c.split()[0],cutoff=1)
elif mode=='b': c=ImageOps.autocontrast(c.split()[2],cutoff=1)
elif mode=='g': c=ImageOps.autocontrast(c.split()[1],cutoff=1)
elif mode=='sat':
    # ink greener than postmark grey: R-B difference suppressed
    r,g,b=c.split()
    from PIL import ImageChops
    d=ImageChops.subtract(b,r,1,128)
    c=ImageOps.autocontrast(d,cutoff=1)
else: c=ImageEnhance.Contrast(c).enhance(1.6)
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save(P+'rev2/'+name+'.png')
