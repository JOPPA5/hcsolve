from PIL import Image, ImageOps
import numpy as np
im=np.asarray(Image.open('hires/cpc_--_HU__HU_Budapest_jolanka-62_adr.jpg').convert('RGB')).astype(float)
x=im[1780:2030,2150:3320]
p=(x[...,2]-x[...,0])  # purple pencil raises B relative to R
p=np.clip((p+110)/(90),0,1)*255
i=ImageOps.autocontrast(Image.fromarray(p.astype('uint8'))).resize((1872,400))
i.save('crops/purple.png')
