# colour deconvolution of pink ink vs teal printed frame; the method that recovered the rubbed note
from PIL import Image, ImageFilter as F
import numpy as np
im=Image.open('work/hires/cpc_1912-03-27_HU__HU_Jasz-Arokszalas_jolanka-13_adr.jpg').convert('RGB')
paper=np.array([216.,185.,155.]); ink=np.array([.0474,.677,.361]); teal=np.array([.790,.635,.490])
Mi=np.linalg.pinv(np.stack([ink,teal,np.ones(3)],1))
def norm(x,lo,hi):
    l,h=np.percentile(x,[lo,hi]); return np.clip((x-l)/(h-l),0,1)
def run(name,box,S=7,blur=2.6,bg=45):
    c=im.crop(box); c=c.resize((c.width*S,c.height*S),Image.BICUBIC).filter(F.GaussianBlur(blur))
    a=np.asarray(c).astype(float)+1; I=(-np.log(a/paper)@Mi.T)[...,0]
    Image.fromarray((255*(1-norm(I,1,99.8))).astype('uint8')).save(f'work/rev2/{name}_d.png')
    g=Image.fromarray((255*norm(I,0,99.9)).astype('uint8'))
    hp=np.asarray(g).astype(float)-np.asarray(g.filter(F.GaussianBlur(bg))).astype(float)
    Image.fromarray((255*(1-norm(hp,3,99.7))).astype('uint8')).save(f'work/rev2/{name}_h.png')
run('L1',(2860,200,3250,290),S=5)
run('L2',(2860,265,3250,365),S=5)
run('L3',(2860,330,3250,420),S=5)
run('L4',(2860,385,3250,480),S=5)
run('L5',(2860,450,3250,560),S=5)
run('L6',(2860,530,3270,640),S=5)
