import sys
from PIL import Image
src=sys.argv[1]; out=sys.argv[2]
im=Image.open(src).rotate(-90,expand=True)  # clockwise 90
x0,y0,x1,y1,s=map(int,sys.argv[3:8])
c=im.crop((x0,y0,x1,y1)); c=c.resize((c.width*s,c.height*s),Image.LANCZOS); c.save(out)
print(im.size)
