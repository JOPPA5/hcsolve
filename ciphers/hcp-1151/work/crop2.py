import glob
from PIL import Image,ImageEnhance
im=Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')
def c(n,x0,y0,x1,y1,s=4):
    r=im.crop((x0,y0,x1,y1)); r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r=ImageEnhance.Contrast(r).enhance(1.5); r.save('crops/%s.png'%n)
c('z_a1',30,1760,450,1910); c('z_a2',430,1760,850,1910); c('z_a3',830,1760,1250,1910); c('z_a4',1230,1760,1650,1910)
c('z_c1',30,1850,450,2040); c('z_c2',430,1850,850,2040); c('z_c3',830,1850,1250,2040); c('z_c4',1230,1850,1650,2040)
c('z_5e',1100,620,1640,760,3); c('z_6a',30,640,560,770,3); c('z_6b',540,640,1100,770,3);c('z_7a',30,690,600,850,3);c('z_7b',550,690,1100,850,3)
c('z_8b',1050,690,1600,850,3); c('z_end',1100,1610,1640,1780,3)
