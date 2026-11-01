from PIL import Image, ImageEnhance, ImageChops
import numpy as np
im=Image.open('hires/cpc_1915--_HU_Mezokovesd_HU_Szomolya_szomolya-43_adr.jpg').convert('RGB')
s=im.size[0]/1024
def c(n,x0,y0,x1,y1,z=2,sep=False):
    r=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
    r=r.resize((r.width*z,r.height*z),Image.LANCZOS)
    if sep:
        a=np.asarray(r).astype(float)
        d=a[...,2]-a[...,0]  # purple positive, brown negative
        o=np.clip(255-(d+25)*4,0,255).astype('uint8')
        Image.fromarray(o).save('crops/%s_sep.png'%n)
    r=ImageEnhance.Contrast(r).enhance(1.5); r.save('crops/%s.png'%n)
c('b1',110,590,380,622,3,True)
c('b2',370,590,620,622,3,True)
c('b3',600,585,960,622,2,True)
c('t1',495,12,730,50,3,True)
c('t2',720,12,960,50,3,True)
c('m1',20,420,470,470,2,True)
c('m2',20,520,470,580,2,True)
c('m3',20,170,470,230,2,True)
c('m4',20,100,470,150,2,True)
