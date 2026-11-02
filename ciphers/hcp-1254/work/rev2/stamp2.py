from PIL import Image, ImageOps, ImageFilter
import numpy as np
im=Image.open('work/hires/cpc_1912-03-27_HU__HU_Jasz-Arokszalas_jolanka-13_adr.jpg').convert('RGB')
box=(2830,290,3270,540)
r=im.crop(box); S=4
r=r.resize((r.width*S,r.height*S),Image.BICUBIC)
a=np.asarray(r).astype(float)
R,G,B=a[...,0],a[...,1],a[...,2]
# ink density, wreath suppressed: G-channel darkness, minus wreath via R
ink=(R-G)
ink2=(B-G)   # pink ink: B>G; paper: B<G
def norm(x,lo=1,hi=99.7):
    l,h=np.percentile(x,[lo,hi]); return np.clip((x-l)/(h-l),0,1)
Image.fromarray((255*(1-norm(ink))).astype('uint8')).save('work/rev2/ink_RG.png')
Image.fromarray((255*(1-norm(ink2))).astype('uint8')).save('work/rev2/ink_BG.png')
# local high-pass of ink
from PIL import ImageFilter as F
g=Image.fromarray((255*norm(ink2)).astype('uint8'))
bl=np.asarray(g.filter(F.GaussianBlur(40))).astype(float)
hp=np.asarray(g).astype(float)-bl
Image.fromarray((255*(1-norm(hp,2,99.5))).astype('uint8')).save('work/rev2/ink_hp.png')
# vertical-only high pass (smear is horizontal): strokes' residual
bl2=np.asarray(g.filter(F.BoxBlur(0))).astype(float)
import numpy as np
k=81
c=np.cumsum(np.pad(np.asarray(g).astype(float),((0,0),(k,k)),mode='edge'),axis=1)
ma=(c[:,2*k:]-c[:,:-2*k])/(2*k)
hp2=np.asarray(g).astype(float)-ma[:,:g.size[0]]
Image.fromarray((255*(1-norm(hp2,2,99.5))).astype('uint8')).save('work/rev2/ink_hp2.png')
