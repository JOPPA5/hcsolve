import sys
from PIL import Image, ImageOps, ImageEnhance
src,out,x0,y0,x1,y1,s=sys.argv[1],sys.argv[2],*map(int,sys.argv[3:8])
im=Image.open(src).convert('RGB').crop((x0,y0,x1,y1))
# use green-ish channel contrast: ink appears greyish-green; take R channel maybe
r,g,b=im.split()
gray=Image.merge('RGB',(r,g,b)).convert('L')
gray=ImageOps.autocontrast(gray,cutoff=1)
gray=ImageEnhance.Contrast(gray).enhance(1.8)
gray=gray.resize(((x1-x0)*s,(y1-y0)*s),Image.LANCZOS)
gray.save(out)
