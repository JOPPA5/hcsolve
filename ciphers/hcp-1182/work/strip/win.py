import sys
from PIL import Image, ImageOps, ImageFilter, ImageDraw
src,outdir=sys.argv[1],sys.argv[2]
x0,x1=1530,1640; s=4; step=180; w=240
im0=Image.open(src).convert("L")
for y in range(0,1900,step):
    im=im0.crop((x0,y,x1,y+w)).filter(ImageFilter.GaussianBlur(0.9))
    im=ImageOps.autocontrast(im,cutoff=1).rotate(90,expand=True)
    im=im.resize((im.width*s,im.height*s),Image.LANCZOS).convert("RGB")
    d=ImageDraw.Draw(im)
    for t in range(0,w,20):
        d.line([(t*s,0),(t*s,12)],fill=(255,0,0),width=2); d.text((t*s+2,12),str(y+t),fill=(255,0,0))
    im.save(f"{outdir}/w{y:04d}.png")
