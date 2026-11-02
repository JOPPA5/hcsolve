from PIL import Image
import numpy as np
im=Image.open('hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-78_adr.jpg').convert('RGB')
s=im.crop((2640,200,3130,770)).rotate(270,expand=True)
a=np.asarray(s).astype(float)
m=a[:,:,0]-a[:,:,1]   # pink excess
bg=np.median(m)
x=255-np.clip((m-bg)/(np.percentile(m,97)-bg),0,1)*255
g=Image.fromarray(x.astype('uint8'))
g.resize((s.width*3,s.height*3),Image.BICUBIC).save('crops2/st_pink.png')
g.crop((280,140,570,380)).resize((1450,1200),Image.BICUBIC).save('crops2/st_pink_r.png')
s.crop((280,170,570,340)).resize((1450,850),Image.LANCZOS).save('crops2/st3r.png')
