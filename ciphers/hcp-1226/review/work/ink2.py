# stronger chroma separation: smooth chroma (JPEG blocks) then use violet-vs-green index, keep luminance detail
import sys
from PIL import Image, ImageOps, ImageFilter
import numpy as np
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1226/work/hires/cpc_--17_HU__HU_Jasz-Arokszalas_jolanka-85_adr.jpg').convert('RGB')
n,x0,y0,x1,y1,s=sys.argv[1:7]; x0,y0,x1,y1=map(int,(x0,y0,x1,y1)); s=float(s)
c=im.crop((x0,y0,x1,y1)).filter(ImageFilter.GaussianBlur(1.2))
a=np.asarray(c).astype(float)
v=(a[...,2]+a[...,0])/2-a[...,1]
lo,hi=np.percentile(v,40),np.percentile(v,99.5)
v2=np.clip((v-lo)/(hi-lo),0,1)
o=Image.fromarray((255*(1-v2)).astype('uint8')).resize((int(c.width*s),int(c.height*s)),Image.BICUBIC); o.save(n+'.png')
