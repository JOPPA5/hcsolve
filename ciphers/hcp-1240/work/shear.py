from PIL import Image, ImageOps
import numpy as np
im=Image.open('hires/cpc_1913-12-_HU__HU_Jasz-Arokszalas_jolanka-117_adr.jpg').convert('L')
A=np.asarray(im)
sl=0.04
out=np.full_like(A,255)
for x in range(A.shape[1]):
    d=int(round(sl*(x-80)))
    out[:,x]=np.roll(A[:,x],d)
o=Image.fromarray(out); o.save('crops/sheared.png')
ink=(out<140)
for s,(x0,x1) in enumerate(((60,840),(800,1580))):
    n=0
    for y in range(60,2010,300):
        r=o.crop((x0,y,x1,y+370)).resize((int(780*2.45),int(370*2.45)),Image.LANCZOS)
        ImageOps.autocontrast(r,cutoff=1).save(f'crops/s{"LR"[s]}{n}.png'); n+=1
print(n)
