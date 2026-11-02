import sys
from PIL import Image, ImageOps
src,out=sys.argv[1:3]; box=tuple(int(x) for x in sys.argv[3:7]); s=float(sys.argv[7])
im=Image.open(src).convert('RGB').crop(box)
r,g,b=im.split()
x=ImageOps.autocontrast(r,cutoff=1)   # blue ink darkest in red channel
x=x.resize((int(x.width*s),int(x.height*s)),Image.BICUBIC)
x.save(out)
