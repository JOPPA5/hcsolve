import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB')
O='review/work/crops/'
def c(n,x0,y0,x1,y1,s=2.0):
    r=im.crop((x0,y0,x1,y1)); r=r.resize((int(r.width*s),int(r.height*s)),Image.LANCZOS); r.save(O+n+'.png')
c('all',0,0,3445,2210,0.45)
for i,(a,b) in enumerate([(60,620),(560,1120),(1060,1620),(1560,2120)]):
    c('LL%d'%i,40,a,860,b,1.6); c('LR%d'%i,800,a,1650,b,1.6)
c('BM',1400,1750,2600,2150,1.5); c('BR',2400,1750,3400,2150,1.8)
c('ST',2700,150,3300,820,2.8)
