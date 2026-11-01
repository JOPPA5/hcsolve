import sys
from PIL import Image, ImageOps
import numpy as np
im=Image.open('ciphers/hcp-1267/work/hires/cpc_1913-07-13_HU__HU_Jasz-Arokszalas_jolanka-39_adr.jpg').convert('RGB')
n,x0,y0,x1,y1,s=sys.argv[1],*map(float,sys.argv[2:7])
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
a=np.asarray(c).astype(float)
# use red channel: green ink dark in R, brownish-red overlay stays lighter
r=a[...,0]; 
lo,hi=np.percentile(r,0.5),np.percentile(r,99)
o=np.clip((r-lo)/(hi-lo),0,1)*255
Image.fromarray(o.astype('uint8')).save(f'ciphers/hcp-1267/work/crops/{n}.png')
