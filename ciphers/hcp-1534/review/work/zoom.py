import sys
from PIL import Image
up=Image.open('upright.png')
x0,y0,x1,y1,s=map(int,sys.argv[1:6])
c=up.crop((x0,y0,x1,y1)); c=c.resize((c.width*s,c.height*s),Image.LANCZOS); c.save(sys.argv[6])
