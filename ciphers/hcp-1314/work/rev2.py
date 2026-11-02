import sys
from PIL import Image, ImageFilter
import numpy as np
SRC='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1314/work/hires/cpc_1913-03-20_HU__HU_Jasz-Arokszalas_jolanka-35_adr.jpg'
O='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1314/work/rev2/'
im=Image.open(SRC).convert('RGB').rotate(-1.2,resample=Image.BICUBIC,fillcolor=(230,210,170))
R=np.asarray(im,float)[...,0]*0.7+np.asarray(im,float)[...,1]*0.3
def crop(x0,y0,x1,y1,name,scale=2):
    a=R[y0:y1,x0:x1]
    b=np.asarray(Image.fromarray(a.clip(0,255).astype('uint8')).filter(ImageFilter.GaussianBlur(25)),float)
    r=a/(b+1)
    r=np.asarray(Image.fromarray((r.clip(0,1.3)/1.3*255).astype('uint8')).filter(ImageFilter.GaussianBlur(1.0)),float)
    lo,hi=np.percentile(r,0.5),np.percentile(r,75); r=np.clip((r-lo)/(hi-lo),0,1)**1.6
    c=Image.fromarray((r*255).astype('uint8'))
    c=c.resize((int(c.width*scale),int(c.height*scale)),Image.LANCZOS); c.save(O+name)
for l in sys.stdin:
    p=l.split()
    if p: crop(*map(int,p[:4]),p[4],float(p[5]) if len(p)>5 else 2)
