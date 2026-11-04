import sys
from PIL import Image, ImageOps, ImageFilter, ImageDraw
src,out=sys.argv[1],sys.argv[2]; y0,y1=int(sys.argv[3]),int(sys.argv[4]); s=int(sys.argv[5]); bl=float(sys.argv[6])
x0,x1=1500,1660
im=Image.open(src).convert("L").crop((x0,y0,x1,y1))
if bl: im=im.filter(ImageFilter.GaussianBlur(bl))
im=ImageOps.autocontrast(im,cutoff=1).rotate(90,expand=True)
im=im.resize((im.width*s,im.height*s),Image.LANCZOS).convert("RGB")
d=ImageDraw.Draw(im)
for t in range(0,y1-y0,10):
    d.line([(t*s,0),(t*s,8 if t%50 else 16)],fill=(255,0,0),width=2)
    if t%50==0: d.text((t*s+2,16),str(y0+t),fill=(255,0,0))
im.save(out)
