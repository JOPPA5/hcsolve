import numpy as np
from PIL import Image
im=Image.open('hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-65_adr.jpg').convert('RGB')
S=1.7225
a=np.asarray(im).astype(float)
red=np.clip((a[:,:,0]-a[:,:,1]-35)*3.2,0,255)
out=Image.fromarray((255-red).astype('uint8'))
def c(n,x0,y0,x1,y1,z=4):
    b=[int(v*S) for v in (x0,y0,x1,y1)]
    r=out.crop(b); r.resize((r.width*z,r.height*z),Image.LANCZOS).save(f'crops/{n}.png')
for i,(y0,y1) in enumerate(((120,175),(165,225),(215,270),(255,310),(295,350),(335,380),(365,410)),1):
    c(f'sr{i}',1530,y0,1810,y1,3)
