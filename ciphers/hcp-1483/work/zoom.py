# zoom.py y0 y1 x0 x1 out [scale]: enlarged crop of work/upright.jpg with x ticks every 5px
import sys
from PIL import Image, ImageOps, ImageDraw
y0,y1,x0,x1=map(int,sys.argv[1:5]); out=sys.argv[5]; S=int(sys.argv[6]) if len(sys.argv)>6 else 12
im=Image.open('work/upright.jpg').convert('L')
c=ImageOps.autocontrast(im.crop((x0,y0,x1,y1)),cutoff=1).resize(((x1-x0)*S,(y1-y0)*S),Image.LANCZOS)
sh=Image.new('L',(c.width,c.height+20),255); sh.paste(c,(0,20)); d=ImageDraw.Draw(sh)
for x in range(x0,x1):
    if x%5==0:
        d.line(((x-x0)*S,0,(x-x0)*S,12 if x%10==0 else 6),fill=0)
        if x%10==0: d.text(((x-x0)*S+2,2),str(x),fill=0)
sh.save(out)
