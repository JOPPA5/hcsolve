from PIL import Image, ImageFilter as F
import numpy as np
im=Image.open('work/hires/cpc_1912-03-27_HU__HU_Jasz-Arokszalas_jolanka-13_adr.jpg').convert('RGB')
box=(2830,280,3270,560)
c=im.crop(box)
a=np.asarray(c).astype(float); R,G,B=a[...,0],a[...,1],a[...,2]
Y=np.asarray(c.convert('YCbCr'))[...,0].astype(float)
# 1. flat-field: divide by large-scale background of Y
g=Image.fromarray(Y.astype('uint8'))
S=5
U=g.resize((g.width*S,g.height*S),Image.LANCZOS)
u=np.asarray(U).astype(float)
bg=np.asarray(U.filter(F.GaussianBlur(45))).astype(float)
loc=u-bg
def norm(x,lo=1,hi=99.5):
    l,h=np.percentile(x,[lo,hi]); return np.clip((x-l)/(h-l),0,1)
out=Image.fromarray((255*norm(loc)).astype('uint8'))
out.save('work/rev2/y_hp.png')
for i,(y0,y1) in enumerate([(0,450),(350,800),(700,1250)]):
    out.crop((0,y0,1100,y1)).save(f'work/rev2/y_L{i}.png')
    out.crop((1000,y0,2200,y1)).save(f'work/rev2/y_R{i}.png')
