import sys
from PIL import Image, ImageOps
src,out,x0,y0,x1,y1,sc=sys.argv[1],sys.argv[2],*map(int,sys.argv[3:8])
im=Image.open(src).convert('L').crop((x0,y0,x1,y1)).rotate(90,expand=True)
im=ImageOps.autocontrast(im,cutoff=1)
im=im.point(lambda v: max(0,min(255,(v-150)*3+128)))
im=im.resize((im.width*sc,im.height*sc),Image.LANCZOS); im.save(out)
