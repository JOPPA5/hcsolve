import sys
from PIL import Image, ImageEnhance
src='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1258/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-70_adr.jpg'
im=Image.open(src).convert('RGB')
# args: name x0 y0 x1 y1 scale [mode]
for spec in sys.argv[1:]:
    p=spec.split(',')
    n=p[0];x0,y0,x1,y1=map(int,p[1:5]);s=float(p[5]);m=p[6] if len(p)>6 else 'c'
    c=im.crop((x0,y0,x1,y1))
    if m=='r':
        c=c.split()[0]
        from PIL import ImageOps
        c=ImageOps.autocontrast(c,cutoff=1)
    else:
        c=ImageEnhance.Contrast(c).enhance(1.6)
    c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
    c.save('c/'+n+'.png')
