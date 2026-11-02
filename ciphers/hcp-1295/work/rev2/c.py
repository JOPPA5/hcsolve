import sys
from PIL import Image, ImageOps
src='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1295/work/hires/cpc_1912-06-06_HU__HU_Jasz-Arokszalas_jolanka-24_adr.jpg'
im=Image.open(src).convert('RGB')
O='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1295/work/rev2/'
# spec name,x0,y0,x1,y1,s,mode  mode: c colour+green; g green only; b blue+green ; r red-minus
for spec in sys.argv[1:]:
    p=spec.split(','); n=p[0]; x0,y0,x1,y1,s=map(int,p[1:6]); m=p[6] if len(p)>6 else 'c'
    c=im.crop((x0,y0,x1,y1)); W,H=c.width*s,c.height*s
    g=ImageOps.autocontrast(c.split()[1],cutoff=1).resize((W,H),Image.LANCZOS)
    cc=ImageOps.autocontrast(c,cutoff=1).resize((W,H),Image.LANCZOS)
    if m=='g': g.save(O+n+'.png')
    elif m=='k': cc.save(O+n+'.png')
    else:
        T=Image.new('RGB',(W,H*2+6),'white');T.paste(cc,(0,0));T.paste(g.convert('RGB'),(0,H+6));T.save(O+n+'.png')
