import sys
from PIL import Image, ImageOps
im=Image.open(sys.argv[1]).convert("RGB").rotate(90,expand=True)
x0,y0,x1,y1=map(int,sys.argv[2:6]); s=int(sys.argv[6])
c=im.crop((x0,y0,x1,y1))
r,g,b=c.split()
# ink is dark grey, smudge greenish: use red channel autocontrast
c=ImageOps.autocontrast(r,cutoff=2)
c=c.resize((c.width*s,c.height*s),Image.LANCZOS); c.save(sys.argv[7])
