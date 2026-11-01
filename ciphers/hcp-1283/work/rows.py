import numpy as np
from PIL import Image
f='ciphers/hcp-1283/work/hires/cpc_1913-03-20_HU__HU_Jasz-Arokszalas_jolanka-34_adr.jpg'
im=Image.open(f).convert('RGB')
A=np.array(im).astype(int)
x0,x1=50,1480; y0,y1=50,2090
red=(A[...,0]-A[...,1]>70)
best=None
for s in np.arange(-0.04,0.04,0.002):
    prof=np.zeros(2300)
    ys,xs=np.nonzero(red[y0:y1,x0:x1])
    yy=(ys+s*xs).astype(int)+100
    prof=np.bincount(yy[(yy>=0)],minlength=2500)
    v=(prof.astype(float)**2).sum()
    if best is None or v>best[0]: best=(v,s,prof)
print(best[1])
p=best[2]; p2=np.convolve(p,np.ones(9)/9,'same')
print([(i-100+y0,int(p2[i])) for i in range(5,len(p2)-5) if p2[i]==p2[i-25:i+26].max() and p2[i]>15])
