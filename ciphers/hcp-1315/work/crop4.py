import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB')
def c(n,x0,y0,x1,y1,s=6):
    r=im.crop((x0,y0,x1,y1)); r.resize((int(r.width*s),int(r.height*s)),Image.BICUBIC).save('crops/%s.png'%n)
c('F',2760,600,3060,690);c('F2',2960,590,3260,690);c('G2',3000,650,3220,750);c('H',2760,690,3020,800);c('H2',2980,690,3240,800)
c('edge',3180,1700,3345,2110,4)
