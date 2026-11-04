import sys
from PIL import Image, ImageOps
src,out=sys.argv[1],sys.argv[2]
im=Image.open(src).convert('RGB')
box=(2700,120,3120,580)
c=im.crop(box)
c.resize((c.width*2,c.height*2),Image.LANCZOS).save(out+'/box_2x.png')
b=ImageOps.autocontrast(c.split()[2],cutoff=1)
b.resize((c.width*2,c.height*2),Image.LANCZOS).save(out+'/box_2x_blue.png')
# halves at 4x
for i,(y0,y1) in enumerate([(0,230),(200,460)]):
    h=b.crop((0,y0,420,y1)); h.resize((h.width*4,h.height*4),Image.LANCZOS).save(out+f'/half{i}_4x_blue.png')
