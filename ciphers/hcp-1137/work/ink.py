import sys
from PIL import Image, ImageOps, ImageChops
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1137/work/'
im=Image.open(d+'hires/cpc_1916-06-10_HU_Mezokovesd_HU_Szomolya_szomolya-39_adr.jpg').convert('RGB')
n,x0,y0,x1,y1=sys.argv[1],*map(int,sys.argv[2:6]); s=float(sys.argv[6])
c=im.crop((x0,y0,x1,y1))
r,g,b=c.split()
# purple pencil: blue-yellow difference high; brown stamp: not
v=ImageChops.subtract(b,g,1,60)
v=ImageOps.autocontrast(v,cutoff=0.5)
v=ImageOps.invert(v).resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c=c.resize(v.size,Image.LANCZOS)
o=Image.new('RGB',(v.width,v.height*2+6),'white');o.paste(c,(0,0));o.paste(v.convert('RGB'),(0,v.height+6));o.save(d+'crops/'+n+'.png')
