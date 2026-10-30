import sys
from PIL import Image, ImageFilter
import numpy as np
SRC='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1314/work/hires/cpc_1913-03-20_HU__HU_Jasz-Arokszalas_jolanka-35_adr.jpg'
O='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1314/work/crops/'
im=Image.open(SRC).convert('L')
a=np.asarray(im,float); b=np.asarray(im.filter(ImageFilter.GaussianBlur(40)),float)
r=a/(b+1); lo,hi=np.percentile(r,0.3),np.percentile(r,70); r=np.clip((r-lo)/(hi-lo),0,1)**1.3
n=Image.fromarray((r*255).astype('uint8')).rotate(-1.5,resample=Image.BICUBIC,fillcolor=255)
n.save(O+'desk.png')
arr=255-np.asarray(n,float)
p=arr[:,100:1350].mean(1); p=np.convolve(p,np.ones(15)/15,'same')
print([ (i,int(p[i])) for i in range(0,2210,20)])
n.resize((1378,884)).save(O+'deskfull.png')
