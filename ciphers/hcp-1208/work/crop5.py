from PIL import Image
import numpy as np, sys
im=Image.open('hires/cpc_1914-10-15_HU__HU_Budapest_jolanka-55_adr.jpg').convert('RGB')
a=np.asarray(im).astype(float)
print(a[1000,300],a[:,:,0].mean(),a[300:320,300:320].mean((0,1)))
d=a[:,:,2]-a[:,:,1]
print(np.percentile(d,[1,50,90,99,99.9]))
v=np.clip((d-np.median(d)-15)/40,0,1)
out=Image.fromarray((255*(1-v)).astype('uint8'))
for n,b in (('q1',(830,240,1530,540)),('q2',(830,480,1530,780))):
    r=out.crop(b); r.resize((r.width*3-100,r.height*3),Image.BICUBIC).save('crops/%s.png'%n)
