# isolate green ink from black postmark: map (G-R) excess to darkness
import sys
import numpy as np
from PIL import Image
im=np.asarray(Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1279/work/hires/cpc_1914-04-12_HU__HU_Jasz-Arokszalas_jolanka-53_adr.jpg').convert('RGB')).astype(float)
n,x0,y0,x1,y1,s=sys.argv[1],*map(int,sys.argv[2:7])
r=im[y0:y1,x0:x1]
v=np.clip((r[:,:,1]-r[:,:,0]+40)/50,0,1)
o=Image.fromarray((255*(1-v)).astype('uint8'))
o=o.resize((o.width*s,o.height*s),Image.LANCZOS)
o.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1279/work/crops/'+n+'.png')
