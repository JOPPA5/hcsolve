import glob
from PIL import Image,ImageEnhance
im=Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')
def c(n,x0,y0,x1,y1,s=3):
    r=im.crop((x0,y0,x1,y1)); r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r.save('crops/%s.png'%n)
c('y1',1050,480,1650,600); c('y2',1600,480,2200,600); c('y3',2100,470,2600,600)
c('y4',30,550,650,640); c('y5',600,550,1200,640)
c('y6',30,880,420,1040); 
c('y7',30,1000,450,1130)
