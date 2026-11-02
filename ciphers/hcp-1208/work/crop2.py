import sys
from PIL import Image, ImageOps, ImageChops
import numpy as np
im=Image.open('hires/cpc_1914-10-15_HU__HU_Budapest_jolanka-55_adr.jpg').convert('RGB')
a=np.asarray(im).astype(float)
# purple-ness: B relative to R, ignoring brightness; black ink has B~R
p=a[:,:,2]-a[:,:,0]*0.72
print(np.percentile(p,[1,50,99]))
p=p-np.median(p)
# keep ink: B high rel to paper
v=np.clip(p/ (np.percentile(p,99.7)),0,1)
out=Image.fromarray((255*(1-v)).astype('uint8'))
out.save('crops/purple.png')
def c(name,box,s=2.5):
    r=out.crop(box); r=r.resize((int(r.width*s),int(r.height*s)),Image.LANCZOS); r.save('crops/%s.png'%name)
c('p1',(780,250,1560,650))
c('p2',(780,560,1560,960))
c('p3',(80,250,860,650))
c('p4',(80,560,860,960))
