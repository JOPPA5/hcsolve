import sys
from PIL import Image, ImageEnhance
import glob
im=Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')
# args: name x0 y0 x1 y1 scale
n,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:6]),float(sys.argv[6])
c=im.crop((x0,y0,x1,y1)); c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c=ImageEnhance.Contrast(c).enhance(1.5)
c.save('crops/%s.png'%n)
