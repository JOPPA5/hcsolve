from PIL import Image
import numpy as np
im=Image.open('hires/cpc_1914-10-15_HU__HU_Budapest_jolanka-55_adr.jpg').convert('RGB')
a=np.asarray(im).astype(float)
d=a[:,:,2]-a[:,:,1]
v=np.clip((d-np.median(d)-8)/35,0,1)
out=Image.fromarray((255*(1-v)).astype('uint8'))
out.save('crops/ink.png')
for n,b in (('s1',(80,280,790,560)),('s2',(80,520,790,800)),('s3',(700,280,1410,560)),('s4',(700,520,1410,800)),('s5',(1000,300,1540,540)),('s6',(1000,520,1540,760))):
    r=out.crop(b); s=2000/r.width; r.resize((2000,int(r.height*s)),Image.BICUBIC).save('crops/%s.png'%n)
