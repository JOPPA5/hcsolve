import sys
from PIL import Image, ImageFilter
import numpy as np
SRC='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1314/work/hires/cpc_1913-03-20_HU__HU_Jasz-Arokszalas_jolanka-35_adr.jpg'
O='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1314/work/crops/'
im=Image.open(SRC).convert('RGB').rotate(-1.5,resample=Image.BICUBIC,fillcolor=(255,255,255))
a=sys.argv[1:]
for i in range(0,len(a),6):
    nm,x0,y0,x1,y1,s=a[i],*map(float,a[i+1:i+6])
    c=im.crop((int(x0),int(y0),int(x1),int(y1)))
    g=np.asarray(c,float)[:,:,1]
    g=np.asarray(Image.fromarray(g.astype('uint8')).filter(ImageFilter.GaussianBlur(1.6)),float)
    bg=np.asarray(Image.fromarray(g.astype('uint8')).filter(ImageFilter.GaussianBlur(30)),float)
    r=g-bg
    lo=np.percentile(r,0.5); hi=np.percentile(r,75)
    r=np.clip((r-lo)/(hi-lo),0,1)
    t=Image.fromarray((r*255).astype('uint8'));t.resize((int(t.width*s),int(t.height*s)),Image.BICUBIC).save(O+nm)
