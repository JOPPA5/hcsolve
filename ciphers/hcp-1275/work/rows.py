from PIL import Image
import numpy as np
im=Image.open('hires/cpc_1913-08-13_HU__HU_Jasz-Arokszalas_jolanka-40_adr.jpg').convert('RGB')
a=np.asarray(im).astype(int)
for x0,x1 in [(70,300),(1000,1300)]:
    g=(a[:,x0:x1,1]-a[:,x0:x1,0]>-5)&(a[:,x0:x1,0]<170)
    p=g.sum(1).astype(float)
    p=np.convolve(p,np.ones(15)/15,'same')
    pk=[y for y in range(40,2060) if p[y]==p[max(0,y-25):y+26].max() and p[y]>3]
    print(pk)
