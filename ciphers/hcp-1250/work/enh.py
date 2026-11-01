from PIL import Image, ImageOps
import numpy as np
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1250/work/hires/cpc_1913-06-16_HU__HU_Jasz-Arokszalas_jolanka-38_adr.jpg').convert('RGB')
c=im.crop((2600,300,3060,720))
a=np.asarray(c).astype(float)
# green-channel darkness: red ink dark in green; orange seal lighter
g=a[:,:,1]; b=a[:,:,2]; r=a[:,:,0]
for n,x in (('g',g),('b',b),('gb',(g*1.0-(r-g)*0.25))):
    o=Image.fromarray(np.clip((x-x.min())/(np.percentile(x,99)-x.min())*255,0,255).astype('uint8'))
    o=o.resize((o.width*2,o.height*2),Image.LANCZOS); o.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1250/work/crops/stamp_%s.png'%n)
