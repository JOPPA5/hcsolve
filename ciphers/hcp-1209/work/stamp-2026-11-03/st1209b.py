import sys
from PIL import Image, ImageOps, ImageFilter
src,out=sys.argv[1],sys.argv[2]
im=Image.open(src).convert('RGB')
box=(2780,490,3140,620)
c=im.crop(box); w,h=c.size; c=c.resize((w*4,h*4),Image.LANCZOS)
r,g,b=c.split()
from PIL import ImageChops
d=ImageChops.subtract(g,r,1,128)
ImageOps.autocontrast(d,cutoff=1).save(f'{out}/row5_gr.png')
c.save(f'{out}/row5w.png')
ImageOps.autocontrast(b,cutoff=2).save(f'{out}/row5_b.png')
