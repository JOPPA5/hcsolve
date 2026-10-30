import sys
from PIL import Image, ImageDraw, ImageOps
im=Image.open(sys.argv[1]).convert('L')
items=[a.split(':') for a in sys.argv[3:]]
S=8; tiles=[]
for lab,box in items:
    x0,y0,x1,y1=map(int,box.split(','))
    c=ImageOps.autocontrast(im.crop((x0,y0,x1,y1)),cutoff=2).resize(((x1-x0)*S,(y1-y0)*S),Image.LANCZOS)
    t=Image.new('L',(c.width,c.height+30),255); t.paste(c,(0,30)); ImageDraw.Draw(t).text((4,4),lab,fill=0); tiles.append(t)
W=sum(t.width for t in tiles)+10*len(tiles); H=max(t.height for t in tiles)
out=Image.new('L',(W,H),255); x=0
for t in tiles: out.paste(t,(x,0)); x+=t.width+10
out.save(sys.argv[2])
