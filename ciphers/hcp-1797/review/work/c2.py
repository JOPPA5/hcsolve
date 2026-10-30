import sys
from PIL import Image
im=Image.open('rot.png')
# args: name x0 y0 x1 y1 scale
n,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:7])
c=im.crop((x0,y0,x1,y1)); c=c.resize((c.width*s,c.height*s),Image.LANCZOS); c.save(n+'.png'); print(c.size)
