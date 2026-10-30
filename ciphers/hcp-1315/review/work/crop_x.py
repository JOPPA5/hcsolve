import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB')
O='review/work/crops/'
def c(n,x0,y0,x1,y1,s=3.0):
    r=im.crop((x0,y0,x1,y1)); r=r.resize((int(r.width*s),int(r.height*s)),Image.BICUBIC); r.save(O+n+'.png')
c('r7j',60,580,330,690,4)
c('r1k',1250,70,1500,160,4)
c('r2l',560,170,860,260,4)
c('r11tt',1000,1090,1300,1190,4)
c('r12g',60,1110,720,1220,2.4)
c('s12',2760,240,3220,380,3.5)
im2=Image.open(sys.argv[2]).convert('RGB'); im2.resize((im2.width//3,im2.height//3)).save(O+'pic.png')
