from PIL import Image, ImageOps, ImageEnhance
im=Image.open('adr_ccw.png').convert('RGB')
def c(n,b,s=6,e=True):
    x=im.crop(b); x=x.resize((x.width*s,x.height*s),Image.BICUBIC)
    if e: x=ImageOps.autocontrast(x,cutoff=1)
    x.save(n+'.png')
# coordinates: r_all origin (250,890) scale3
c('z_uijt',(275,1020,470,1140),5)
c('z_xjmm',(455,1020,690,1130),5)
c('z_album',(650,1125,920,1190),5)
c('z_zpvs',(540,1195,760,1300),6)
c('z_gspn',(290,1190,500,1300),5)
c('z_hjsm',(760,1200,1010,1300),5)
c('z_q',(250,1115,440,1240),5)
