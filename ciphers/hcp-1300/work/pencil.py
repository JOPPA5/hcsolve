import sys,os
import numpy as np
from PIL import Image, ImageOps, ImageFilter
D=os.path.dirname(os.path.abspath(__file__))
im=Image.open(D+'/hires/cpc_--26_HU__HU_Jasz-Arokszalas_jolanka-91_adr.jpg').convert('RGB')
name,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
a=np.asarray(im.crop((int(x0),int(y0),int(x1),int(y1)))).astype(float)
R,G,B=a[...,0],a[...,1],a[...,2]
d=G-(0.75*R+0.25*B)   # paper near const; green ink high, pencil low
lo,hi=np.percentile(d,1),np.percentile(d,92)
g=np.clip((d-lo)/(hi-lo),0,1)*255
c=Image.fromarray(g.astype('uint8')).filter(ImageFilter.GaussianBlur(1.2))
c=c.resize((int(c.width*s),int(c.height*s)),Image.BICUBIC)
c.save(D+'/crops/%s.png'%name)
