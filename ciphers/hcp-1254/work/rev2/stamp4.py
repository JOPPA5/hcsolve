from PIL import Image, ImageFilter as F
import numpy as np
im=Image.open('work/hires/cpc_1912-03-27_HU__HU_Jasz-Arokszalas_jolanka-13_adr.jpg')
print(im.layers if hasattr(im,'layers') else '', getattr(im,'layer',None))
im=im.convert('RGB')
box=(2830,280,3270,560)
c=im.crop(box)
yc=np.asarray(c.convert('YCbCr')).astype(float)
Y,Cb,Cr=yc[...,0],yc[...,1],yc[...,2]
def norm(x,lo=1,hi=99.7):
    l,h=np.percentile(x,[lo,hi]); return np.clip((x-l)/(h-l),0,1)
S=5
def up(x,blur=2.0,bgr=70):
    g=Image.fromarray(np.clip(x,0,255).astype('uint8')).resize((c.width*S,c.height*S),Image.BICUBIC).filter(F.GaussianBlur(blur))
    u=np.asarray(g).astype(float)
    bg=np.asarray(g.filter(F.GaussianBlur(bgr))).astype(float)
    return u-bg
cr=up(Cr,blur=5,bgr=60)
out=Image.fromarray((255*(1-norm(cr,2,99.8))).astype('uint8'))
out.save('work/rev2/cr_hp.png')
cb=up(Cb*2-128,blur=5,bgr=60)
Image.fromarray((255*(1-norm(cb,2,99.8))).astype('uint8')).save('work/rev2/cb_hp.png')
crf=up(Cr,blur=4,bgr=500)
Image.fromarray((255*(1-norm(crf,1,99.8))).astype('uint8')).save('work/rev2/cr_flat.png')
