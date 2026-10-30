from PIL import Image
im=Image.open('work/hires/cpc_1913-08-31_HU__HU_Jasz-Arokszalas_jolanka-41_adr.jpg').convert('RGB')
import numpy as np
a=np.asarray(im).astype(int)[100:2100,120:1400]
m=((a[:,:,2]-a[:,:,1])>35)&(a[:,:,1]<170)
p=m.sum(1)
p=np.convolve(p,np.ones(9)/9,'same')
rows=[];inr=False
for y,v in enumerate(p):
    if v>25 and not inr: s=y;inr=True
    if v<=25 and inr:
        inr=False; rows.append((s+100,y+100))
print(rows,len(rows))
