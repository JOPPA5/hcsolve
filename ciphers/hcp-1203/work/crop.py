import sys
from PIL import Image, ImageOps
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1203/work/hires/cpc_--23_HU__HU_Rakos-Palota-Ujfalu_jolanka-88_adr.jpg').convert('RGB')
# usage: name x0 y0 x1 y1 scale [rot]
n,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
if len(sys.argv)>7: c=c.rotate(float(sys.argv[7]),expand=True)
c=ImageOps.autocontrast(c,cutoff=0.5)
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1203/work/crops/%s.png'%n)
