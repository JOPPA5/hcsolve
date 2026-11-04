import sys
from PIL import Image, ImageOps
src,out=sys.argv[1],sys.argv[2]
im=Image.open(src).convert('RGB')
print(im.size)
c=im.crop((2620,190,3080,720))
c.resize((c.width*2,c.height*2),Image.LANCZOS).save(out+'/stamp_color_2x.png')
b=ImageOps.autocontrast(c.split()[2],cutoff=1)
b=b.resize((c.width*4,c.height*4),Image.LANCZOS)
h=b.height
for i in range(3):
    b.crop((0,i*h//3,b.width,(i+1)*h//3)).save(out+f'/stamp_blue_4x_{i}.png')
im.resize((im.width//4,im.height//4)).save(out+'/overview.png')
