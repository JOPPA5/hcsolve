from PIL import Image, ImageEnhance
import glob
im=Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')
s=2.1675
def c(n,x0,y0,x1,y1,z=4):
    r=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
    r=ImageEnhance.Contrast(r).enhance(1.5)
    r=r.resize((int(r.width*z),int(r.height*z)),Image.LANCZOS); r.save('crops/%s.png'%n)
c('z_h',670,330,790,400)     # hik row6 end
c('z_e',20,385,180,450)      # row7 start
c('z_3',700,170,790,240)     # row3 end
c('z_kd',20,165,240,235,3)
