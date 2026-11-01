from PIL import Image
import numpy as np
im=Image.open('hires/cpc_1915--_HU_Mezokovesd_HU_Szomolya_szomolya-43_adr.jpg').convert('RGB')
s=im.size[0]/1024
def c(n,x0,y0,x1,y1,z=4):
    r=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s))).resize((int((x1-x0)*s*z),int((y1-y0)*s*z)),Image.LANCZOS)
    a=np.asarray(r).astype(float); R=a[...,0]-0.35*a[...,2]
    lo,hi=np.percentile(R,3),np.percentile(R,55)
    o=np.clip((R-lo)/(hi-lo)*255,0,255).astype('uint8'); Image.fromarray(o).save('crops/%s.png'%n)
c('tx1',640,14,770,42); c('tx2',765,14,880,42)
