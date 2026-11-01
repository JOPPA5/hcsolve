import sys
from PIL import Image, ImageOps
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1267/work/hires/cpc_1913-07-13_HU__HU_Jasz-Arokszalas_jolanka-39_adr.jpg').convert('RGB')
n,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
if len(sys.argv)>7: c=c.split()[0].convert('RGB')
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
ImageOps.autocontrast(c,cutoff=1).save(f'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1267/review/work/{n}.png')
