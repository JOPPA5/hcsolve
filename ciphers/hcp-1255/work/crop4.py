from PIL import Image
import numpy as np
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1255/work/'
im=Image.open(W+'hires/cpc_1912-03-11_HU__HU_Jasz-Arokszalas_jolanka-08_adr.jpg').convert('RGB')
p=im.crop((70,850,420,1280)); a=np.array(p).astype(float)
# red-minus-green map: red ink high; green print low/neg; paper mid
d=a[:,:,0]-a[:,:,1]
g=255-np.clip((d-20)*3,0,255)
Image.fromarray(g.astype('uint8')).resize((1050,1290),Image.LANCZOS).save(W+'rows/print_red.png')
p.resize((1050,1290),Image.LANCZOS).save(W+'rows/print_rgb.png')
