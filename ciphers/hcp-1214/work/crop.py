from PIL import Image, ImageOps
import sys,glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
s=3445/1024
# overlapping horizontal bands over text column
y=25;i=0
while y<600:
    h=110
    box=(int(15*s),int(y*s),int(510*s),int((y+h)*s))
    c=im.crop(box); c=ImageOps.autocontrast(c.convert('L'),cutoff=1)
    c=c.resize((c.width*5//4,c.height*5//4),Image.LANCZOS)
    c.save(f'crops/band{i}.png'); i+=1; y+=90
print(i)
