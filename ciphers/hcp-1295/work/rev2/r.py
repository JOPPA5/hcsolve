import sys
from PIL import Image, ImageOps
im=Image.open('desk.png')
# args name,x0,y0,x1,y1,s[,g]
for spec in sys.argv[1:]:
    p=spec.split(','); n=p[0]; x0,y0,x1,y1,s=map(int,p[1:6])
    c=im.crop((x0,y0,x1,y1))
    c=ImageOps.autocontrast(c.split()[1],cutoff=1).convert('RGB') if len(p)>6 else ImageOps.autocontrast(c,cutoff=.5)
    c.resize((c.width*s,c.height*s),Image.LANCZOS).save(n+'.png')
