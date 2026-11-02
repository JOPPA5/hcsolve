from PIL import Image, ImageOps
import numpy as np,sys
src='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1295/work/hires/cpc_1912-06-06_HU__HU_Jasz-Arokszalas_jolanka-24_adr.jpg'
im=Image.open(src).convert('RGB').crop((80,40,1680,2150))
def prof(a):
    r=im.rotate(a,resample=Image.BILINEAR,fillcolor=(230,200,160)); x=np.asarray(r).astype(int); return ((x[...,0]-x[...,1])>70).sum(1)
for a in np.arange(-7,2.01,.5): print(a,int(np.var(prof(a))))
