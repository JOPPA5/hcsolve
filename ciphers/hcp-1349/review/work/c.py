from PIL import Image,ImageOps
r=Image.open('rot.png')
s=r.size[0]/ Image.open('rot_small.jpg').size[0]
print(s)
def c(n,b,z=4):
    b=tuple(int(x*s) for x in b)
    im=r.crop(b); im=im.resize((im.width*z,im.height*z),Image.LANCZOS)
    im=ImageOps.autocontrast(im.convert('RGB'),cutoff=1); im.save(n+'.jpg',quality=92); print(n,im.size)
c('r_park',(340,965,560,1060))
c('r_place',(540,975,830,1060))
c('r_opp',(340,890,700,985))
c('r_l1',(340,770,830,840),3)
c('r_l2',(340,830,830,920),3)
c('r_l5',(340,1040,860,1125),3)
c('r_l6',(340,1100,840,1185),3)
c('r_l7',(340,1160,840,1230),3)
c('r_l8',(340,1215,840,1295),3)
