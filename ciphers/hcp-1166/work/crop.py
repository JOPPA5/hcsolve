import sys
from PIL import Image
im=Image.open([__import__('glob').glob('hires/*_adr.jpg')][0][0])
# args: name x0 y0 x1 y1 scale (hires px)
n,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save('crops/%s.png'%n)
