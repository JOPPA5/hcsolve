from PIL import Image, ImageEnhance
import glob
def c(card,n,x0,y0,x1,y1,z=2):
    f=glob.glob('../../hcp-%d/work/hires/*adr*'%card)[0]
    im=Image.open(f).convert('RGB'); s=im.size[0]/1024
    r=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
    r=r.resize((int(r.width*z),int(r.height*z)),Image.LANCZOS); r=ImageEnhance.Contrast(r).enhance(1.5); r.save('crops/sib_%s.png'%n); print(n,r.size)
c(1175,'75a',20,95,440,175,1.3)
c(1175,'75b',20,170,440,285,1.3)
c(1179,'79a',15,545,500,605,1.5)
c(1179,'79b',480,545,960,605,1.5)
c(1174,'74a',20,300,470,360,1.3)
c(1174,'74b',20,10,480,50,1.3)
c(1174,'74c',20,540,470,620,1.3)
c(1174,'74d',440,560,640,620,2)
