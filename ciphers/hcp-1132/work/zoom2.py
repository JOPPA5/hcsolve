# zoom with x and y rulers (hires coords). usage: zoom2.py x0 y0 x1 y1 scale out
import sys
from PIL import Image, ImageDraw
x0,y0,x1,y1=map(int,sys.argv[1:5]); sc=float(sys.argv[5]); out=sys.argv[6]
im=Image.open('work/hires/cpc_--_HU_Debrecen_HU___adr.jpg').convert('RGB').crop((x0,y0,x1,y1))
im=im.resize((int((x1-x0)*sc),int((y1-y0)*sc)))
can=Image.new('RGB',(im.width+40,im.height+14),'white'); can.paste(im,(40,14)); d=ImageDraw.Draw(can)
for y in range((y0//50+1)*50,y1,50):
    yy=14+int((y-y0)*sc); d.line([(30,yy),(40,yy)],fill=(255,0,0)); d.text((0,yy-5),str(y),fill=(255,0,0))
for x in range((x0//50+1)*50,x1,50):
    xx=40+int((x-x0)*sc); d.line([(xx,6),(xx,14)],fill=(0,0,255)); d.text((xx+1,0),str(x),fill=(0,0,255))
can.save(out)
