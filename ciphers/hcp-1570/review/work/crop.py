import sys
from PIL import Image
im=Image.open(sys.argv[1]).rotate(90,expand=True)
x0,y0,x1,y1,s=map(int,sys.argv[2:7])
c=im.crop((x0,y0,x1,y1)); c=c.resize((c.width*s,c.height*s),Image.LANCZOS); c.save(sys.argv[7])
print(im.size)
