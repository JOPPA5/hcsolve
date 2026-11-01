from PIL import Image
import numpy as np
im=Image.open('hires/cpc_1915--_HU_Mezokovesd_HU_Szomolya_szomolya-43_adr.jpg').convert('RGB')
s=im.size[0]/1024
def c(n,x0,y0,x1,y1,z=4):
    r=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s))); r=r.resize((r.width*z,r.height*z),Image.LANCZOS)
    a=np.asarray(r).astype(float); v=a[...,2]-a[...,0]
    lo,hi=np.percentile(v,2),np.percentile(v,99.5)
    Image.fromarray(255-np.clip((v-lo)/(hi-lo)*255,0,255).astype('uint8')).save('crops/%s_v.png'%n)
    r.save('crops/%s_c.png'%n)
c('L6a',30,415,270,472,4); c('L6b',240,415,490,472,4); c('T1',495,8,730,50,4); c('T2',720,8,960,50,4)
