from PIL import Image, ImageOps
im=Image.open('adr_ccw.png').convert('RGB')
def c(n,b,s=6):
    x=im.crop(b); x=x.resize((x.width*s,x.height*s),Image.LANCZOS); x=ImageOps.autocontrast(x,cutoff=.5); x.save(n+'.png')
c('z_blot',(640,1205,760,1275),9)
c('z_efb',(640,925,860,1010),5)
c('z_mm',(525,1030,700,1095),7)
