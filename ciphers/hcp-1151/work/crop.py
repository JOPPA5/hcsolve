import sys,glob
from PIL import Image
im=Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')
# name x0 y0 x1 y1 scale
def c(n,x0,y0,x1,y1,s=2):
    r=im.crop((x0,y0,x1,y1)); r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r.save('crops/%s.png'%n)
rows=[(60,290),(270,500),(460,690),(670,900),(880,1110),(1090,1320),(1300,1530),(1510,1740),(1700,1900)]
for i,(a,b) in enumerate(rows):
    if i<2:
        c('r%dA'%i,30,a,830,b); c('r%dB'%i,800,a,1600,b); c('r%dC'%i,1580,a,2380,b); c('r%dD'%i,2200,a,2800,b)
    else:
        c('r%dA'%i,30,a,830,b); c('r%dB'%i,800,a,1640,b)
c('b0A',30,1730,830,2050); c('b0B',800,1730,1640,2050); c('b0C',1340,1730,2500,2050,2)
