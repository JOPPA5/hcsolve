import sys
from PIL import Image, ImageOps
import numpy as np
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1226/work/hires/cpc_--17_HU__HU_Jasz-Arokszalas_jolanka-85_adr.jpg').convert('RGB')
n,x0,y0,x1,y1,s=sys.argv[1:7]; x0,y0,x1,y1=map(int,(x0,y0,x1,y1)); s=float(s)
a=np.asarray(im.crop((x0,y0,x1,y1))).astype(float)
r,g,b=a[...,0],a[...,1],a[...,2]
# violet ink: b high relative to g; green print: g>=r. 
v=(b-g)
v2=np.clip((v-v.min())/(np.percentile(v,99.7)-v.min()),0,1)
o=Image.fromarray((255*(1-v2)).astype('uint8'))
o=ImageOps.autocontrast(o).resize((int(o.width*s),int(o.height*s)),Image.LANCZOS); o.save(n+'.png')
