import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB')
O='review/work/crops/'
def c(n,x0,y0,x1,y1,s=3.0):
    r=im.crop((x0,y0,x1,y1)); r=r.resize((int(r.width*s),int(r.height*s)),Image.BICUBIC); r.save(O+n+'.png')
c('r14b',700,1270,1560,1400,2)
c('r13',640,1190,1600,1290,1.9)
c('r16end',1100,1440,1600,1560,3)
