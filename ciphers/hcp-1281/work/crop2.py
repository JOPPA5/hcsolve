import sys
import numpy as np
from PIL import Image
a=np.asarray(Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1281/work/hires/cpc_1914-06-10_HU__HU_Jasz-Arokszalas_jolanka-54_adr.jpg').convert('RGB')).astype(float)
s=1.7225
od=-np.log((a+1)/256)
def sample(x0,y0,x1,y1,q):
    X0,Y0,X1,Y1=[int(v*s) for v in (x0,y0,x1,y1)]
    d=od[Y0:Y1,X0:X1].reshape(-1,3); L=d.sum(1)
    return d[L>=np.percentile(L,q)].mean(0)
paper=np.median(od[100:400,300:800].reshape(-1,3),0)
ink=sample(550,50,900,75,98)-paper   # clean row 1
post=sample(1130,290,1420,350,97)-paper
print(paper,ink,post)
M=np.stack([ink,post,paper],1)
Mi=np.linalg.inv(M)
c=(od-paper)@Mi.T
inkc=c[...,0]
def save(n,x0,y0,x1,y1,z=3.0):
    X0,Y0,X1,Y1=[int(v*s) for v in (x0,y0,x1,y1)]
    v=np.clip(inkc[Y0:Y1,X0:X1]/0.8,0,1)
    im=Image.fromarray((255*(1-v)).astype('uint8'))
    im=im.resize((int(im.width*z),int(im.height*z)),Image.LANCZOS)
    im.save('crops/%s.png'%n)
    cc=Image.fromarray(a[Y0:Y1,X0:X1].astype('uint8'))
    cc=cc.resize((int(cc.width*z),int(cc.height*z)),Image.LANCZOS); cc.save('crops/%s_c.png'%n)
for spec in sys.argv[1:]:
    n,x0,y0,x1,y1=spec.split(','); save(n,float(x0),float(y0),float(x1),float(y1))
