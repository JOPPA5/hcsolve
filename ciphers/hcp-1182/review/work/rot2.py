import sys
from PIL import Image, ImageOps, ImageFilter
src,out,x0,y0,x1,y1,s=sys.argv[1],sys.argv[2],*map(int,sys.argv[3:7]),float(sys.argv[7])
im=Image.open(src).crop((x0,y0,x1,y1)).convert("L").filter(ImageFilter.GaussianBlur(1.2))
im=ImageOps.autocontrast(im,cutoff=0.5)
im=im.rotate(90,expand=True).resize((int((y1-y0)*s),int((x1-x0)*s)),Image.LANCZOS)
im.save(out)
