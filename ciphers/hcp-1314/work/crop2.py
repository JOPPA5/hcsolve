import sys
from PIL import Image, ImageOps, ImageFilter, ImageChops
import numpy as np
SRC='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1314/work/hires/cpc_1913-03-20_HU__HU_Jasz-Arokszalas_jolanka-35_adr.jpg'
im=Image.open(SRC).convert('L')
O='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1314/work/crops/'
def crop(x0,y0,x1,y1,name,scale=2,rot=0):
    c=im.crop((x0,y0,x1,y1))
    a=np.asarray(c,float); b=np.asarray(c.filter(ImageFilter.GaussianBlur(40)),float)
    r=a/(b+1); lo,hi=np.percentile(r,0.3),np.percentile(r,70); r=np.clip((r-lo)/(hi-lo),0,1)**1.3
    c=Image.fromarray((r*255).astype('uint8')).resize((int(c.width*scale),int(c.height*scale)),Image.LANCZOS)
    if rot: c=c.rotate(rot,expand=True)
    c.save(O+name)
for line in sys.stdin:
    p=line.split()
    if p: crop(*map(int,p[:4]),p[4],float(p[5]) if len(p)>5 else 2,int(p[6]) if len(p)>6 else 0)
