from PIL import Image
import numpy as np
im=np.asarray(Image.open('work/hires/cpc_1912-03-13_HU__HU_Jasz-Arokszalas_jolanka-09_adr.jpg').convert('RGB')).astype(float)[170:720,2790:3280]
r,g,b=im[...,0],im[...,1],im[...,2]
# red ink: low blue relative to pink dye (dye keeps blue high)
v=np.clip((b-g)*3+128,0,255); w=np.clip(b*1.6-60,0,255)
for n,a in (('sep1',v),('sep2',w)):
    Image.fromarray(a.astype('uint8')).resize((980,1100)).save(f'review/work/crops/{n}.png')
