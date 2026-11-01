import sys
from PIL import Image, ImageOps
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1282/work/hires/cpc_-04-11_HU__HU_Jasz-Arokszalas_jolanka-94_adr.jpg').convert('RGB')
n,x0,y0,x1,y1=sys.argv[1],*map(int,sys.argv[2:6]); s=float(sys.argv[6]); mode=sys.argv[7] if len(sys.argv)>7 else ''
c=im.crop((x0,y0,x1,y1))
if mode=='g':  # green channel: ink contrast; red channel: suppresses red ink
    c=ImageOps.autocontrast(c.split()[1],cutoff=1).convert('RGB')
if mode=='b':
    c=ImageOps.autocontrast(c.split()[2],cutoff=1).convert('RGB')
if mode=='r':
    c=ImageOps.autocontrast(c.split()[0],cutoff=1).convert('RGB')
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save(n+'.png')
