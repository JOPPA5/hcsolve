import sys,glob
from PIL import Image, ImageOps
im=Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')
r,g,b=im.split()
# strips: each ~300 px tall of original
y=30;i=0
while y<2150:
    box=(30,y,1800,y+310)
    c=im.crop(box); c=c.resize((c.width*1,c.height*1)); 
    rr=ImageOps.autocontrast(r.crop(box),cutoff=1)
    W=Image.new('RGB',(c.width,c.height*2+6),'white'); W.paste(c,(0,0)); W.paste(rr.convert('RGB'),(0,c.height+6))
    W.save(f'crops/s{i:02d}.png'); i+=1; y+=270
print(i)
