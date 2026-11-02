import sys
from PIL import Image,ImageChops,ImageOps,ImageFilter
im=Image.open('hires/cpc_1912-04-_HU__HU_Jasz-Arokszalas_jolanka-104_adr.jpg').convert('RGB')
# usage: name x0 y0 x1 y1 scale (hires px)
n,*v=sys.argv[1:]
x0,y0,x1,y1,s=map(float,v)
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
r,g,b=c.split()
W=int(c.width*s);H=int(c.height*s)
def up(i): return i.resize((W,H),Image.LANCZOS)
c1=up(c)
g1=up(ImageOps.autocontrast(g,cutoff=0.5))
d=ImageChops.subtract(r,g,1,0); d=ImageOps.invert(ImageOps.autocontrast(d,cutoff=0.5)); d1=up(d)
# saturated core: green minus blue style
e=ImageOps.autocontrast(ImageChops.subtract(b,g,1,0),cutoff=0.5); e1=up(ImageOps.invert(e))
out=Image.new('RGB',(W,H*4+18),'white')
for i,p in enumerate((c1,g1.convert('RGB'),d1.convert('RGB'),e1.convert('RGB'))): out.paste(p,(0,i*(H+6)))
out.save('rev2/%s.png'%n)
