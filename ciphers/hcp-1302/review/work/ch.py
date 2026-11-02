from PIL import Image
import numpy as np
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1302/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-78_adr.jpg').convert('RGB')
c=im.crop((880,1985,1180,2105));a=np.asarray(c).astype(float)
for i,n in enumerate('rgb'):
    g=a[:,:,i];lo,hi=np.percentile(g,0.1),np.percentile(g,12)
    x=np.clip((g-lo)/(hi-lo),0,1)*255
    Image.fromarray(x.astype('uint8')).resize((1500,600),Image.BICUBIC).save(f'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1302/review/work/blot_{n}.png')
