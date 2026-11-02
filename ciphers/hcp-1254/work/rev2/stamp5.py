from PIL import Image, ImageFilter as F
import numpy as np
im=Image.open('work/hires/cpc_1912-03-27_HU__HU_Jasz-Arokszalas_jolanka-13_adr.jpg').convert('RGB')
box=(2830,270,3270,570)
S=5
c=im.crop(box); c=c.resize((c.width*S,c.height*S),Image.BICUBIC).filter(F.GaussianBlur(2.2))
a=np.asarray(c).astype(float)+1
paper=np.array([215.,190.,150.])
# estimate paper from bright percentile of blurred image
paper=np.percentile(a.reshape(-1,3),92,axis=0); print(paper)
od=-np.log(a/paper)
# vectors from pixel sets
ink=np.median(od[(od[...,1]>0.5)&(od[...,0]<0.15)],axis=0)
teal=np.median(od[(od[...,0]>0.6)],axis=0)
print('ink',ink,'teal',teal)
M=np.stack([ink,teal,np.array([1,1,1.])],1)
Mi=np.linalg.pinv(M)
con=od@Mi.T
I=con[...,0]; Tl=con[...,1]
def norm(x,lo,hi):
    l,h=np.percentile(x,[lo,hi]); return np.clip((x-l)/(h-l),0,1)
Image.fromarray((255*(1-norm(I,1,99.7))).astype('uint8')).save('work/rev2/dec_ink.png')
g=Image.fromarray((255*norm(I,0,99.9)).astype('uint8'))
u=np.asarray(g).astype(float)
bg=np.asarray(g.filter(F.GaussianBlur(35))).astype(float)
hp=u-bg
v=Image.fromarray((255*(1-norm(hp,3,99.7))).astype('uint8')); v.save('work/rev2/dec_hp.png')
W,H=v.size
for i,(y0,y1) in enumerate([(120,560),(440,880),(780,1250)]):
    v.crop((0,y0,W,y1)).save(f'work/rev2/hp_l{i}.png')
