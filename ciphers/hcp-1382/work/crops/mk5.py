from PIL import Image,ImageOps
import numpy as np
o=Image.open('crops/norm.png')
r=Image.open('crops/rot.png')
def c(name,box,s=5,src=o,g=1.0):
    x=src.crop(box)
    if g!=1.0: x=x.point(lambda v:int(255*(v/255)**g))
    x=x.resize((x.width*s,x.height*s),Image.LANCZOS); x.save('crops/'+name+'.jpg',quality=93)
c('c1',(330,170,640,270),4,g=2.2)
g=ImageOps.autocontrast(r.convert('L'),cutoff=.3)
c('c2',(330,170,640,270),4,src=g,g=2)
# channels
for i,ch in enumerate('RGB'):
    x=r.split()[i]; 
    if ch=='B': c('c3B',(330,170,640,270),4,src=ImageOps.autocontrast(x),g=2)
