from PIL import Image, ImageOps
import numpy as np
im=Image.open('work/hires/cpc_1912-03-13_HU__HU_Jasz-Arokszalas_jolanka-09_adr.jpg').convert('RGB')
box=(2790,190,3260,640)
x=im.crop(box); x4=x.resize((x.width*3,x.height*3),Image.LANCZOS); x4.save('work/crops2/box3.png')
a=np.asarray(x).astype(float)
r,g,b=a[...,0],a[...,1],a[...,2]
# channels
for n,c in (('r',r),('g',g),('b',b),('gb',(g+b)/2),('rg',r-g),('rb',r-b)):
    c2=(c-np.percentile(c,0.5))/(np.percentile(c,99.5)-np.percentile(c,0.5))
    Image.fromarray((np.clip(c2,0,1)*255).astype('uint8')).resize((x.width*3,x.height*3),Image.LANCZOS).save(f'work/crops2/box3_{n}.png')
