import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB')
x0,y0,x1,y1=map(int,sys.argv[2:6])
c=im.crop((x0,y0,x1,y1))
out=Image.new('RGB',c.size,(255,255,255))
for x in range(c.width):
  for y in range(c.height):
    r,g,b=c.getpixel((x,y))
    lum=(r+g+b)/3
    if lum<120 and r-b<30: out.putpixel((x,y),(0,0,0))
    elif r-b>=30 and lum<170: out.putpixel((x,y),(220,60,60))
    elif lum<150: out.putpixel((x,y),(140,140,140))
out=out.resize((c.width*7,c.height*7),Image.NEAREST); out.save(sys.argv[6])
# print dark ink pixel listing compact
for y in range(c.height):
  row=''
  for x in range(c.width):
    r,g,b=c.getpixel((x,y)); lum=(r+g+b)/3
    row+= '#' if (lum<120 and r-b<30) else ('r' if (r-b>=30 and lum<170) else ('+' if lum<150 else '.'))
  print(f'{y0+y:4d} {row}')
