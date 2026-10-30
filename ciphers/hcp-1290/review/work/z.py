import sys
from PIL import Image, ImageEnhance
im=Image.open(sys.argv[1]).convert('RGB')
x0,y0,x1,y1,s=map(float,sys.argv[2:7])
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
c=ImageEnhance.Contrast(c).enhance(1.6).resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
c.save(sys.argv[7],quality=90)
