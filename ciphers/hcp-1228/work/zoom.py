import sys
from PIL import Image,ImageOps
p='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1228/work/'
im=Image.open(p+'hires/cpc_1913-09-07_HU__HU_Jasz-Arokszalas_jolanka-42_adr.jpg').convert('RGB')
# name x0 y0 x1 y1 (display coords)
for s in sys.argv[1:]:
    n,x0,y0,x1,y1=s.split(','); x0,y0,x1,y1=[int(int(v)*1.72) for v in (x0,y0,x1,y1)]
    c=im.crop((x0,y0,x1,y1)); k=min(1900/c.width,1000/c.height,6)
    c=c.resize((int(c.width*k),int(c.height*k)),Image.LANCZOS); c=ImageOps.autocontrast(c,cutoff=1); c.save(p+f'crops/z_{n}.png')
