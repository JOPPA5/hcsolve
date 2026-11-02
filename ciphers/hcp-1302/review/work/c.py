import sys
from PIL import Image, ImageOps
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1302/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-78_adr.jpg').convert('RGB')
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1302/review/work/'
n=sys.argv[1];box=tuple(map(int,sys.argv[2:6]));z=float(sys.argv[6]) if len(sys.argv)>6 else 3
rot=int(sys.argv[7]) if len(sys.argv)>7 else 0
c=im.crop(box)
if rot:c=c.rotate(rot,expand=True)
c=c.resize((int(c.width*z),int(c.height*z)),Image.LANCZOS)
ImageOps.autocontrast(c,cutoff=0.5).save(d+n+'.png')
