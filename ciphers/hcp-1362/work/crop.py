from PIL import Image, ImageOps
im=Image.open('hires/pc_hcp_43_adr.JPG').convert('RGB')
def c(name,box,z=3):
    r=im.crop(box).rotate(90,expand=True)
    r=r.resize((r.width*z,r.height*z),Image.LANCZOS)
    r=ImageOps.autocontrast(r,cutoff=1); r.save('crops/%s.png'%name); print(name,r.size)
# box in hires coords: x columns = lines on the rotated card
c('all',(140,300,800,1075),2)
c('L1',(660,300,800,720)); c('L1b',(660,680,800,1075))
c('L2',(530,300,680,720)); c('L2b',(530,680,680,1075))
c('L3',(350,300,550,720)); c('L3b',(350,680,550,1075))
c('L4',(140,300,380,720)); c('L4b',(140,680,380,1075))
def d(name,box,z=5):
    # box in rotated 'all'-frame /2 coordinates (x,y)-> hires
    x0,y0,x1,y1=box
    # rotated by +90: rotated x = orig y-300 ; rotated y = 800-orig x
    r=im.crop((800-y1,300+x0,800-y0,300+x1)).rotate(90,expand=True)
    r=r.resize((r.width*z,r.height*z),Image.LANCZOS); r=ImageOps.autocontrast(r,cutoff=0.5); r.save('crops/%s.png'%name); print(name,r.size)
d('a1',(20,25,270,160))
d('a2',(230,20,500,190))
d('a3',(540,20,775,170))
d('b1',(20,130,260,260))
d('b2',(240,140,520,270))
d('b3',(500,120,775,260))
d('c1',(10,220,300,370))
d('c2',(320,240,520,340))
d('c3',(480,230,775,370))
d('stamp',(0,0,1,1),1) if 0 else None
s=im.crop((1380,80,1720,400)); s=s.resize((s.width*4,s.height*4),Image.LANCZOS); s.save('crops/stamp.png')
