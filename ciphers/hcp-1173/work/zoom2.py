import glob
from PIL import Image, ImageOps
im=Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')
r=im.split()[0]
Z={'e1':(590,2020,1000,2120),'e2':(950,2000,1400,2120),'e3':(1300,1990,1800,2120)}
for k,b in Z.items():
    c=r.crop(b); c=ImageOps.autocontrast(c,cutoff=0.5).resize((c.width*4,c.height*4),Image.LANCZOS); c.save(f'crops/z_{k}.png')
