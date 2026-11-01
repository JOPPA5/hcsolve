import sys
from PIL import Image
import numpy as np
im=np.asarray(Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1265/work/hires/cpc_--17_HU__HU_Jasz-Arokszalas_jolanka-86_adr.jpg').convert('RGB')).astype(float)
n,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:6]),float(sys.argv[6])
c=im[y0:y1,x0:x1]; d=c[...,0]-c[...,1]   # red ink high, paper ~small, green stamp negative
d=np.clip((d-d.min()*0-5)/(80-5),0,1); g=255-(d*255).astype('uint8')
o=Image.fromarray(g); o=o.resize((int(o.width*s),int(o.height*s)),Image.LANCZOS)
o.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1265/review/work/crops/%s.png'%n)
