import sys
from PIL import Image, ImageFilter, ImageChops, ImageOps
im=Image.open(sys.argv[1]).convert('L')
x0,y0,x1,y1=map(int,sys.argv[2].split(',')); s=int(sys.argv[3])
c=im.crop((x0,y0,x1,y1))
bg=c.filter(ImageFilter.GaussianBlur(6))
# divide-normalise: ink darker than local background
import array
px=c.load(); pb=bg.load(); out=Image.new('L',c.size)
po=out.load()
for y in range(c.height):
    for x in range(c.width):
        v=px[x,y]/max(pb[x,y],1)
        po[x,y]=max(0,min(255,int(255*(v-0.55)/0.5)))
out=out.resize((out.width*s,out.height*s),Image.LANCZOS)
out.save(sys.argv[4])
