import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB')
def c(n,x0,y0,x1,y1,s=2.5):
    r=im.crop((x0,y0,x1,y1)); r=r.resize((int(r.width*s),int(r.height*s)),Image.LANCZOS); r.save('crops/%s.png'%n)
ys=[(60,300),(280,520),(500,740),(720,960),(940,1180),(1160,1400),(1380,1620),(1600,1840),(1800,2090)]
for i,(a,b) in enumerate(ys):
    c('L%d'%i,60,a,830,b); c('R%d'%i,780,a,1620,b)
c('B1',1400,1800,2500,2100,1.8);c('B2',2400,1800,3300,2100,2)
c('stamp',2700,180,3250,780,3)
