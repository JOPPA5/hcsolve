import sys
from PIL import Image, ImageOps
im=Image.open('hires/cpc_1916-04-20_HU_Mezokovesd_HU_Szomolya_szomolya-29_adr.jpg').convert('RGB')
name,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
px=c.load()
out=Image.new('L',c.size)
o=out.load()
for y in range(c.height):
  for x in range(c.width):
    r,g,b=px[x,y]
    # blue-ness: b-r large for ink; grey print has b-r ~0
    o[x,y]=max(0,min(255,255-int((b-r+25)*3)))
out=ImageOps.autocontrast(out).resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
out.save('crops/'+name+'.jpg',quality=90)
