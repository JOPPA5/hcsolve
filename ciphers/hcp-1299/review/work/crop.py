import sys
from PIL import Image, ImageOps
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1299/work/hires/cpc_-12-03_HU__HU_Jasz-Arokszalas_jolanka-96_adr.jpg')
out,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0),int(y0),int(x1),int(y1))).convert('L')
if len(sys.argv)>7: c=c.rotate(int(sys.argv[7]),expand=True)
c=ImageOps.autocontrast(c,cutoff=1)
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save(out)
