import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB')
def c(n,x0,y0,x1,y1,s=6):
    r=im.crop((x0,y0,x1,y1)); r.resize((int(r.width*s),int(r.height*s)),Image.BICUBIC).save('crops/%s.png'%n)
c('E',2770,480,3100,590,5);c('E2',3000,480,3260,590,5);c('Fa',2770,570,3010,650,7);c('Fb',2960,570,3230,650,7);c('Ha',2960,720,3120,800,8)
