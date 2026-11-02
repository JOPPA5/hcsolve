import sys
from PIL import Image,ImageChops,ImageOps,ImageFilter
import numpy as np
im=Image.open('hires/cpc_1912-04-_HU__HU_Jasz-Arokszalas_jolanka-104_adr.jpg').convert('RGB')
n,*v=sys.argv[1:]
x0,y0,x1,y1,s=map(float,v)
a=np.asarray(im.crop((int(x0),int(y0),int(x1),int(y1)))).astype(float)
r,g,b=a[...,0],a[...,1],a[...,2]
# saturation-like: pink ink has b>g; foxing brown has b<g
m=b-g
m=np.clip(m,-5,None)
def norm(m,lo,hi):
    return np.clip((m-np.percentile(m,lo))/(np.percentile(m,hi)-np.percentile(m,lo)+1e-6),0,1)
A=norm(m,5,99.5)
# lower gamma to lift faint ink
B=A**0.55
# ratio r/g
C=norm(r/(g+1),5,99.7)**0.7
out=[]
for k in (B,C):
    i=Image.fromarray(((1-k)*255).astype('uint8')).filter(ImageFilter.GaussianBlur(1.2))
    out.append(i.resize((int(i.width*s),int(i.height*s)),Image.BICUBIC))
W,H=out[0].size
c=Image.new('L',(W,H*2+8),128)
c.paste(out[0],(0,0));c.paste(out[1],(0,H+8))
c.save('rev2/%s.png'%n)
