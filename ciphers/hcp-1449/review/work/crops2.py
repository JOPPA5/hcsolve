import sys
from PIL import Image, ImageOps
out=sys.argv[1]
msg=Image.open(out+'/msg.png').convert('L')
g=ImageOps.autocontrast(msg,cutoff=1)
L=[(0,55),(35,95),(75,140),(140,225)]
for i,(y0,y1) in enumerate(L):
    for j,(x0,x1) in enumerate([(0,180),(160,330),(300,470)]):
        c=g.crop((x0,y0,x1,y1)); c=c.resize((c.width*5,c.height*5),Image.LANCZOS); c.save(f'{out}/r{i+1}_{j+1}.png')
