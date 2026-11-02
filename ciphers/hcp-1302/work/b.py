from PIL import Image, ImageOps
import numpy as np
im=Image.open('hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-78_adr.jpg').convert('RGB')
box=(870,1990,1120,2105)
c=im.crop(box); z=8
c.resize((c.width*z,c.height*z),Image.BICUBIC).save('crops2/bl_rgb.png')
a=np.asarray(c).astype(float)
g=a[:,:,1]
# stretch only the dark range
lo,hi=np.percentile(g,0.2),np.percentile(g,25)
x=np.clip((g-lo)/(hi-lo),0,1)*255
Image.fromarray(x.astype('uint8')).resize((c.width*z,c.height*z),Image.BICUBIC).save('crops2/bl_g.png')
b=a[:,:,2]; lo,hi=np.percentile(b,0.2),np.percentile(b,25)
x=np.clip((b-lo)/(hi-lo),0,1)*255
Image.fromarray(x.astype('uint8')).resize((c.width*z,c.height*z),Image.BICUBIC).save('crops2/bl_b.png')
s=im.crop((2640,200,3130,770)).rotate(270,expand=True)
s.crop((280,250,570,420)).resize((1450,850),Image.LANCZOS).save('crops2/st4r.png')
s.crop((0,60,300,240)).resize((1500,900),Image.LANCZOS).save('crops2/st1a.png')
s.crop((280,60,570,240)).resize((1450,900),Image.LANCZOS).save('crops2/st1b.png')
