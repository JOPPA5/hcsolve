from PIL import Image
im=Image.open('adr_ccw.png').convert('RGB')
def c(n,b,s=3):
    x=im.crop(b); x=x.resize((x.width*s,x.height*s),Image.LANCZOS); x.save(n+'.png')
c('r_l1',(270,900,1090,1020),2)
c('r_l2',(270,990,1090,1130),2)
c('r_l3',(250,1060,1090,1240),2)
c('r_l4',(250,1160,1090,1300),2)
c('r_all',(250,890,700,1300),3)
c('r_all2',(680,890,1110,1300),3)
