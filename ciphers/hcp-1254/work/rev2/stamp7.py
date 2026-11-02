from PIL import Image, ImageFilter as F
import numpy as np
im=Image.open('work/hires/cpc_1912-03-27_HU__HU_Jasz-Arokszalas_jolanka-13_adr.jpg').convert('RGB')
paper=np.array([216.,185.,155.]); ink=np.array([.0474,.677,.361]); teal=np.array([.790,.635,.490])
Mi=np.linalg.pinv(np.stack([ink,teal,np.ones(3)],1))
S=4; box=(2840,190,3260,730)
c=im.crop(box); c=c.resize((c.width*S,c.height*S),Image.BICUBIC).filter(F.GaussianBlur(1.6))
a=np.asarray(c).astype(float)+1; I=(-np.log(a/paper)@Mi.T)[...,0]
# subtract only blurred smear; divide by local amplitude (local contrast normalisation)
g=Image.fromarray(np.clip(I*200+50,0,255).astype('uint8'))
u=np.asarray(g).astype(float)
m=np.asarray(g.filter(F.GaussianBlur(22))).astype(float)
s=np.sqrt(np.asarray(Image.fromarray(np.clip((u-m)**2/4,0,255).astype('uint8')).filter(F.GaussianBlur(22))).astype(float)*4)+6
z=(u-m)/s
out=np.clip(.62-z*.28,0,1)
v=Image.fromarray((255*out).astype('uint8')); v.save('work/rev2/lcn_all.png'); print(v.size)
v.crop((0,0,1680,1100)).save('work/rev2/lcn_top.png')
