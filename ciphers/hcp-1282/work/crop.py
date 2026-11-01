import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1282/work/hires/cpc_-04-11_HU__HU_Jasz-Arokszalas_jolanka-94_adr.jpg')
# args: name x0 y0 x1 y1 scale (coords in display 2000-wide units)
n,x0,y0,x1,y1=sys.argv[1],*map(float,sys.argv[2:6]); s=float(sys.argv[6]) if len(sys.argv)>6 else 2.2
b=[int(v*1.7225) for v in (x0,y0,x1,y1)]
c=im.crop(b); c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save(f'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1282/work/crops/{n}.png')
