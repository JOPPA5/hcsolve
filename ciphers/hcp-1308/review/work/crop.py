import sys
from PIL import Image, ImageOps
# usage: x0 y0 x1 y1 scale out [rot]
A='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1308/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-80_adr.jpg'
x0,y0,x1,y1=map(int,sys.argv[1:5]); s=float(sys.argv[5]); o=sys.argv[6]; r=float(sys.argv[7]) if len(sys.argv)>7 else 0
c=Image.open(A).crop((x0,y0,x1,y1))
if r: c=c.rotate(r,expand=True,fillcolor=(255,255,255))
c=ImageOps.autocontrast(c.convert('L'),cutoff=1)
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS); c.save(o)
