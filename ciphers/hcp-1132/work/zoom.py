# usage: zoom.py x0 y0 x1 y1 scale out  (hires coordinates); draws a y ruler every 100 px
import sys
from PIL import Image, ImageDraw
x0,y0,x1,y1=map(int,sys.argv[1:5]); sc=float(sys.argv[5]); out=sys.argv[6]
im=Image.open('work/hires/cpc_--_HU_Debrecen_HU___adr.jpg').convert('RGB').crop((x0,y0,x1,y1))
im=im.resize((int((x1-x0)*sc),int((y1-y0)*sc)))
d=ImageDraw.Draw(im)
for y in range((y0//100+1)*100,y1,100):
    yy=int((y-y0)*sc); d.line([(0,yy),(12,yy)],fill=(255,0,0),width=2); d.text((14,yy-6),str(y),fill=(255,0,0))
im.save(out)
