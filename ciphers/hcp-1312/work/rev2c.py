import sys
from PIL import Image,ImageFilter
import numpy as np
im=Image.open('hires/cpc_1912-04-_HU__HU_Jasz-Arokszalas_jolanka-104_adr.jpg').convert('RGB')
n,*v=sys.argv[1:]
x0,y0,x1,y1,s=map(float,v)
a=np.asarray(im.crop((int(x0),int(y0),int(x1),int(y1)))).astype(float)
r,g,b=a[...,0],a[...,1],a[...,2]
m=(b-g)+0.5*(r-g)*0.0
def blur(x,rad):
    w=int(rad*3)+1; t=np.arange(-w,w+1); ker=np.exp(-t*t/(2*rad*rad)); ker/=ker.sum()
    p=np.pad(x,w,mode='edge')
    p=np.apply_along_axis(lambda v:np.convolve(v,ker,'same'),0,p)
    p=np.apply_along_axis(lambda v:np.convolve(v,ker,'same'),1,p)
    return p[w:-w,w:-w]
outs=[]
for sm,bg,amt in ((1.5,0,0),(1.5,28,0),(1.5,14,1)):
    k=blur(m,sm)
    if bg:
        k=k-blur(k,bg)
    k=np.clip((k-np.percentile(k,10))/(np.percentile(k,99.5)-np.percentile(k,10)),0,1)
    i=Image.fromarray(((1-k)*255).astype('uint8')).resize((int(k.shape[1]*s),int(k.shape[0]*s)),Image.BICUBIC)
    outs.append(i)
W,H=outs[0].size
c=Image.new('L',(W,H*3+16),128)
for j,i in enumerate(outs): c.paste(i,(0,j*(H+8)))
c.save('rev2/%s.png'%n)
