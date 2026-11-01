from PIL import Image
import numpy as np
a=np.array(Image.open('hires/cpc_1914-04-12_HU__HU_Jasz-Arokszalas_jolanka-52_adr.jpg').convert('RGB')).astype(int)
g=(a[:,:,1]-a[:,:,0]>10)
for x0,x1 in [(90,500)]:
    p=g[:,x0:x1].sum(1)
    p=np.convolve(p,np.ones(9)/9,'same')
    pk=[y for y in range(40,2150) if p[y]==p[max(0,y-22):y+23].max() and p[y]>8]
    print(pk,len(pk))
