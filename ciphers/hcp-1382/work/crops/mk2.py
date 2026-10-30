from PIL import Image,ImageOps,ImageEnhance
r=Image.open('crops/rot.png')
import sys
def c(name,box,s=3):
    x=r.crop(box).convert('L')
    x=ImageOps.autocontrast(x,cutoff=0.5)
    x=x.point(lambda v:int(255*(v/255)**1.6))
    x=x.resize((x.width*s,x.height*s),Image.LANCZOS); x.save('crops/'+name+'.jpg',quality=93)
c('l1a',(60,10,440,180)); c('l1b',(400,10,800,180))
c('l3a',(0,180,420,350)); c('l3b',(380,180,800,350))
c('l5a',(0,320,420,500)); c('l5b',(380,320,800,500))
c('l6a',(0,480,420,640)); c('l6b',(380,480,800,640))
c('l7',(60,600,700,720),2)
