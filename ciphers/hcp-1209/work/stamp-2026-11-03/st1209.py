import sys
from PIL import Image, ImageOps
src,out=sys.argv[1],sys.argv[2]
im=Image.open(src).convert('RGB')
def save(box,name,s):
    c=im.crop(box); w,h=c.size
    c=c.resize((w*s,h*s),Image.LANCZOS)
    r,g,b=c.split()
    # green ink: low red; use red channel inverted contrast
    ImageOps.autocontrast(r,cutoff=1).save(f'{out}/{name}_r.png')
    c.save(f'{out}/{name}.png')
save((2770,330,3150,440),'row3',4)
save((2770,400,3150,510),'row4',4)
save((2770,470,3150,580),'row5',4)
save((2700,150,3200,700),'box',2)
