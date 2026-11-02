from PIL import Image
import numpy as np
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1302/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-78_adr.jpg').convert('RGB')
s=im.crop((2640,200,3130,770)).rotate(270,expand=True)
a=np.asarray(s).astype(float)
m=a[:,:,0]-a[:,:,1];bg=np.median(m)
x=255-np.clip((m-bg)/(np.percentile(m,97)-bg),0,1)*255
Image.fromarray(x.astype('uint8')).resize((s.width*2,s.height*2),Image.BICUBIC).save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1302/review/work/st_pink.png')
