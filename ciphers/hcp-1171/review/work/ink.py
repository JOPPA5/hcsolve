from PIL import Image, ImageOps
import numpy as np
f='../../work/hires/cpc_1915-11-22_HU_Mezokovesd_HU_Szomolya_szomolya-06_adr.jpg'
im=np.asarray(Image.open(f).convert('RGB')).astype(float)
S=2.477
x0,y0,x1,y1=[int(v*S) for v in (120,785,370,850)]
a=im[y0:y1,x0:x1]
r,g,b=a[...,0],a[...,1],a[...,2]
# blue ink: small R-B compared with paper; olive print & brown have large R-B or low-G
d=r-b
out=np.clip((d-20)/(np.percentile(d,95)-20),0,1)*255
p=Image.fromarray(out.astype('uint8')).resize(((x1-x0)*5,(y1-y0)*5),Image.LANCZOS); p.save('w_rb.png'); print(p.size)
gray=Image.fromarray(a.astype('uint8')).resize(((x1-x0)*5,(y1-y0)*5),Image.LANCZOS); gray.save('w_col.png')
