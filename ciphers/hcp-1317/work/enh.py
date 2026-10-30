import sys
from PIL import Image, ImageOps, ImageEnhance
import numpy as np
f='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1317/work/hires/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-110_adr.jpg'
im=Image.open(f).convert('RGB')
x0,y0,x1,y1,s,out=sys.argv[1:7]
c=im.crop((int(x0),int(y0),int(x1),int(y1)))
a=np.asarray(c).astype(float)
# greenness: G minus R highlights the green ink on the paper
g=a[:,:,1]-a[:,:,0]
g=(g-np.percentile(g,2))/(np.percentile(g,99.7)-np.percentile(g,2)); g=1-np.clip(g,0,1)
c2=Image.fromarray((g*255).astype('uint8'))
s=float(s); c2=c2.resize((int(c2.width*s),int(c2.height*s)),Image.BICUBIC); c2.save(out)
c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS).save(out.replace('.png','_rgb.png'))
