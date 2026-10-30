# reviewer crop tool: name x0 y0 x1 y1 scale [ink]
import sys,os
import numpy as np
from PIL import Image, ImageOps
D=os.path.dirname(os.path.abspath(__file__))
im=Image.open(D+'/../../work/hires/cpc_--26_HU__HU_Jasz-Arokszalas_jolanka-91_adr.jpg').convert('RGB')
n=sys.argv[1];x0,y0,x1,y1=map(int,sys.argv[2:6]);s=float(sys.argv[6]);ink=len(sys.argv)>7
c=im.crop((x0,y0,x1,y1))
if ink:
    a=np.asarray(c).astype(float);R,G=a[...,0],a[...,1];d=np.clip(G-R+np.median(R-G),0,None);g=G+float(sys.argv[7])*d
    lo,hi=np.percentile(g,.5),np.percentile(g,98);c=Image.fromarray((np.clip((g-lo)/(hi-lo),0,1)**1.5*255).astype('uint8'))
else: c=ImageOps.autocontrast(c.convert('L'),cutoff=1)
c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS).save(D+'/crops/%s.png'%n)
