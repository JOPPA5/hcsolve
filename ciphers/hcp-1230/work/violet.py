import sys
from PIL import Image, ImageOps, ImageFilter
import numpy as np
im=Image.open('hires/cpc_1913-12-_HU__HU_Jasz-Arokszalas_jolanka-116_adr.jpg').convert('RGB')
a=sys.argv[1:]
for i in range(0,len(a),6):
    n,x0,y0,x1,y1,s=a[i],*map(int,a[i+1:i+6])
    A=np.asarray(im.crop((x0,y0,x1,y1)).filter(ImageFilter.GaussianBlur(0.8))).astype(float)
    v=A[...,2]-A[...,1]  # blue minus green
    v=v-np.percentile(v,50)
    v=np.clip(v/np.percentile(v,99.7),0,1)
    o=Image.fromarray((255*(1-v)).astype('uint8')).resize(((x1-x0)*s,(y1-y0)*s),Image.BICUBIC)
    o.save(f'crops/{n}.png')
