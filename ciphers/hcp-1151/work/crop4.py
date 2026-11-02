import glob
from PIL import Image
im=Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')
def c(n,x0,y0,x1,y1,s=4):
    r=im.crop((x0,y0,x1,y1)); r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r.save('crops/%s.png'%n)
c('x1',1360,1930,1760,2030); c('x2',1950,1930,2500,2030,3); c('x3',560,840,1010,950,4); c('x4',1100,1820,1460,1910,4); c('x5',1650,1820,1960,1910,4)
