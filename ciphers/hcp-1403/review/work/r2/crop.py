import sys
from PIL import Image, ImageOps
im=Image.open(sys.argv[1]).convert('L')
for spec in sys.argv[2:]:
    name,x0,y0,x1,y1,s=spec.split(',')
    c=im.crop((int(x0),int(y0),int(x1),int(y1)))
    c=ImageOps.autocontrast(c,cutoff=1)
    c=c.resize((c.width*int(s),c.height*int(s)),Image.LANCZOS)
    c.save(name)
