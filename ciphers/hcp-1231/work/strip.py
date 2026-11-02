import sys,glob
from PIL import Image,ImageOps
f=glob.glob('hires/*adr.jpg')[0]
im=Image.open(f).convert('L')
# strip.py name x0 x1 yc halfh seglen scale
name=sys.argv[1]; x0,x1,yc,hh,seg,s=[int(v) for v in sys.argv[2:8]]
segs=[]
x=x0
while x<x1:
    c=im.crop((x,yc-hh,min(x+seg+30,x1),yc+hh)); c=ImageOps.autocontrast(c,cutoff=0.5)
    segs.append(c.resize((c.width*s,c.height*s),Image.LANCZOS)); x+=seg
W=max(c.width for c in segs);H=sum(c.height+8 for c in segs)
o=Image.new('L',(W,H),255);y=0
for c in segs:o.paste(c,(0,y));y+=c.height+8
o.save(f'crops/{name}.png')
