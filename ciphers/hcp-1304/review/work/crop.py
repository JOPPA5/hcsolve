import sys
from PIL import Image, ImageEnhance
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1304/work/hires/cpc_--04_HU__HU_Jasz-Arokszalas_jolanka-82_adr.jpg').convert('RGB')
n,x0,y0,x1,y1=sys.argv[1],*map(int,sys.argv[2:6])
s=float(sys.argv[6]) if len(sys.argv)>6 else 2
r=int(sys.argv[7]) if len(sys.argv)>7 else 0
c=im.crop((x0,y0,x1,y1))
if r: c=c.rotate(r,expand=True)
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c=ImageEnhance.Contrast(c).enhance(1.5)
c.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1304/review/work/'+n)
