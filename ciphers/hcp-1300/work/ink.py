import sys,os
import numpy as np
from PIL import Image, ImageOps, ImageFilter
D=os.path.dirname(os.path.abspath(__file__))
im=Image.open(D+'/hires/cpc_--26_HU__HU_Jasz-Arokszalas_jolanka-91_adr.jpg').convert('RGB')
name,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7]); al=float(sys.argv[7]) if len(sys.argv)>7 else 1.0
a=np.asarray(im.crop((int(x0),int(y0),int(x1),int(y1)))).astype(float)
R,G,B=a[...,0],a[...,1],a[...,2]
pap=np.median(R-G)
d=np.clip(G-R+pap,0,None)
g=G+al*d
lo,hi=np.percentile(g,0.5),np.percentile(g,98)
g=np.clip((g-lo)/(hi-lo),0,1)**1.5*255
c=Image.fromarray(g.astype('uint8')).resize((int((x1-x0)*s),int((y1-y0)*s)),Image.BICUBIC)
c.save(D+'/crops/%s.png'%name)
print(pap)
