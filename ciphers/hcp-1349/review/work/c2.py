from PIL import Image,ImageOps
r=Image.open('rot.png')
s=1.2744034707158352
def c(n,b,z=6):
    b=tuple(int(x*s) for x in b)
    im=r.crop(b); im=im.resize((im.width*z,im.height*z),Image.LANCZOS)
    ImageOps.autocontrast(im.convert('RGB'),cutoff=1).save(n+'.jpg',quality=92)
c('z_stock',(640,1115,840,1185),5)
c('z_nh1',(590,770,700,830),6)
c('z_nh8',(370,1225,560,1295),5)
c('z_stamp',(100,105,335,300),4)
