from PIL import Image
import numpy as np
im=Image.open('work/hires/cpc_1912-04-04_HU__HU_Jasz-Arokszalas_jolanka-14_adr.jpg').convert('RGB')
c=im.crop((2820,120,3180,560))
a=np.asarray(c).astype(float)
# redness map: R minus G
d=np.clip((a[:,:,0]-a[:,:,1]-40)*3,0,255)
o=Image.fromarray((255-d).astype('uint8')).resize((c.width*4,c.height*4),Image.LANCZOS).rotate(32,expand=True,fillcolor=255)
o.save('review/work/stamp-top-red.png')
