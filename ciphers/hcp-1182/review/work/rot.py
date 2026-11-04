import sys
from PIL import Image, ImageOps, ImageEnhance
src,out,x0,y0,x1,y1,s=sys.argv[1],sys.argv[2],*map(int,sys.argv[3:7]),float(sys.argv[7])
im=Image.open(src).crop((x0,y0,x1,y1)).convert("L")
im=ImageOps.autocontrast(im,cutoff=1)
im=im.rotate(90,expand=True)  # vertical text -> horizontal (reading bottom-to-top)
im=im.resize((int(im.width*s),int(im.height*s)),Image.LANCZOS)
im.save(out)
