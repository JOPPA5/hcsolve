"""reviewer blue-minus-green crops: name x0 y0 x1 y1 scale"""
import sys
from PIL import Image, ImageFilter
import numpy as np
im=Image.open('work/hires/cpc_1913-12-_HU__HU_Jasz-Arokszalas_jolanka-116_adr.jpg').convert('RGB')
a=sys.argv[1:]
for i in range(0,len(a),6):
    n,x0,y0,x1,y1,s=a[i],*map(int,a[i+1:i+6])
    A=np.asarray(im.crop((x0,y0,x1,y1)).filter(ImageFilter.GaussianBlur(1.0))).astype(float)
    v=A[...,2]-A[...,0]*0.5-A[...,1]*0.5
    v=v-np.percentile(v,40); v=np.clip(v/np.percentile(v,99.5),0,1)
    Image.fromarray((255*(1-v)).astype('uint8')).resize(((x1-x0)*s,(y1-y0)*s),Image.BICUBIC).save(f'review/work/crops/{n}.png')
