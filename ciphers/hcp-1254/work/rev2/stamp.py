import sys
from PIL import Image, ImageOps, ImageFilter
import numpy as np
im=Image.open('work/hires/cpc_1912-03-27_HU__HU_Jasz-Arokszalas_jolanka-13_adr.jpg').convert('RGB')
a=np.asarray(im).astype(float)
# find strongly pink region in the top right
d=(a[...,0]-a[...,1])
H,W=d.shape
print(H,W)
tr=d[0:1000,2500:]
ys,xs=np.where(tr>60)
print(xs.min()+2500,xs.max()+2500,ys.min(),ys.max())
