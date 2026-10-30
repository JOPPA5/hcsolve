"""Row 24 crux: separate violet pencil from olive seal ink. Colour crop plus a map of B-(R+G)/2 (bright = violet pencil)."""
import os
import numpy as np
from PIL import Image
W=os.path.dirname(os.path.abspath(__file__))
im=Image.open(W+'/hires/cpc_--26_HU__HU_Jasz-Arokszalas_jolanka-91_adr.jpg').convert('RGB')
b=(2960,1770,3200,1880); s=7
c=im.crop(b); a=np.asarray(c).astype(float)
v=a[...,2]-(a[...,0]+a[...,1])/2
v=np.clip((v-np.percentile(v,5))/(np.percentile(v,99.7)-np.percentile(v,5)),0,1)
Image.fromarray((v*255).astype('uint8')).resize((c.width*s,c.height*s),Image.BICUBIC).save(W+'/crops2/r24_violet.png')
c.resize((c.width*s,c.height*s),Image.LANCZOS).save(W+'/crops2/r24_colour.png')
