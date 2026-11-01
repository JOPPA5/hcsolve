from PIL import Image, ImageOps
import numpy as np
im=Image.open('hires/cpc_1914-04-12_HU__HU_Jasz-Arokszalas_jolanka-52_adr.jpg').convert('RGB')
c=im.crop((2820,160,3200,650))
a=np.array(c).astype(float)
# greenness vs red: ink = low red
r=a[:,:,0]
r=(r-r.min())/(r.max()-r.min())*255
g=Image.fromarray(r.astype('uint8'))
g=ImageOps.autocontrast(g,cutoff=1)
W=380*4
g.crop((0,0,380,250)).resize((W,1000),Image.LANCZOS).save('tiles/st_a.png')
g.crop((0,240,380,490)).resize((W,1000),Image.LANCZOS).save('tiles/st_b.png')
