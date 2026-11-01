import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1253/work/hires/cpc_1913-02-22_HU__HU_Jasz-Arokszalas_jolanka-33_adr.jpg')
# args: name x0 y0 x1 y1 (display coords 2000-wide) scale
n,x0,y0,x1,y1=sys.argv[1],*map(float,sys.argv[2:6]); s=float(sys.argv[6]) if len(sys.argv)>6 else 2.5
f=1.7225
c=im.crop((int(x0*f),int(y0*f),int(x1*f),int(y1*f)))
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS).convert('L')
c.save(f'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1253/work/crops/{n}.png')
