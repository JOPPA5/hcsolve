import sys
from PIL import Image, ImageOps, ImageFilter
src,out=sys.argv[1],sys.argv[2]
x0,y0,x1,y1=map(int,sys.argv[3:7]); s=float(sys.argv[7]); blur=float(sys.argv[8]) if len(sys.argv)>8 else 0.8
im=Image.open(src).crop((x0,y0,x1,y1)).convert("L")
if blur>0: im=im.filter(ImageFilter.GaussianBlur(blur))
im=ImageOps.autocontrast(im,cutoff=1)
im=im.rotate(90,expand=True)
im=im.resize((int(im.width*s),int(im.height*s)),Image.LANCZOS)
im.save(out)
