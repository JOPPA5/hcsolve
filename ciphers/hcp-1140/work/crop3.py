from PIL import Image, ImageEnhance
import glob
im=Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')
s=2.1675
def c(n,x0,y0,x1,y1,z=3,ch=None):
    r=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
    r=ImageEnhance.Contrast(r).enhance(1.6)
    r=r.resize((int(r.width*z),int(r.height*z)),Image.LANCZOS); r.save('crops/%s.png'%n)
c('b1',25,905,420,990,2.5)
c('b2',20,935,330,990,3.5)
c('b3',400,905,790,990,2.5)
c('p1',30,515,420,620,2.3)
c('p2',400,515,790,620,2.3)
