from PIL import Image, ImageEnhance
import glob
im=Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')
s=2.1675
def c(n,x0,y0,x1,y1,z=3):
    r=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
    r=ImageEnhance.Contrast(r).enhance(1.6)
    r=r.resize((int(r.width*z),int(r.height*z)),Image.LANCZOS); r.save('crops/%s.png'%n)
c('sz',270,850,600,920,2.5)
c('pm',1150,20,1420,230,1.6)
c('yr',440,930,780,995,2.5)
c('top3',395,25,520,85,5)
