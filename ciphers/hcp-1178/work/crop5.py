from PIL import Image
import numpy as np
im=Image.open('hires/cpc_1915--_HU_Mezokovesd_HU_Szomolya_szomolya-43_adr.jpg').convert('RGB')
s=im.size[0]/1024
def c(n,x0,y0,x1,y1,z=2.5):
    r=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s))).resize((int((x1-x0)*s*z),int((y1-y0)*s*z)),Image.LANCZOS)
    a=np.asarray(r).astype(float); R=a[...,0]
    lo,hi=np.percentile(R,1),np.percentile(R,90)
    o=np.clip((R-lo)/(hi-lo)*255,0,255).astype('uint8'); Image.fromarray(o).save('crops/%s_R.png'%n)
c('t1',495,10,730,48); c('t2',720,10,955,48); c('f',120,415,480,470,2); c('i',110,590,380,622,3); c('j',370,590,620,622,3)
