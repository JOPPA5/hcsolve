import sys
from PIL import Image,ImageFilter
import numpy as np
H='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1312/work/hires/cpc_1912-04-_HU__HU_Jasz-Arokszalas_jolanka-104_adr.jpg'
im=Image.open(H).convert('RGB')
n,mode,x0,y0,x1,y1,s=sys.argv[1:]
x0,y0,x1,y1=map(int,(x0,y0,x1,y1));s=float(s)
c=im.crop((x0,y0,x1,y1))
if mode=='rgb':
    o=c
else:
    a=np.asarray(c).astype(float);r,g,b=a[...,0],a[...,1],a[...,2]
    m=b-g if mode=='bg' else (g if mode=='g' else (r-g))
    if mode=='g': m=-m
    lo,hi=np.percentile(m,8),np.percentile(m,99.7)
    k=np.clip((m-lo)/(hi-lo),0,1)
    o=Image.fromarray(((1-k)*255).astype('uint8')).filter(ImageFilter.GaussianBlur(0.8))
o.resize((int(o.width*s),int(o.height*s)),Image.BICUBIC).save(n+'.png')
