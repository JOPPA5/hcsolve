from PIL import Image, ImageOps
import numpy as np, glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
a=np.asarray(im.crop((2660,170,3160,740))).astype(float)+1
od=-np.log(a/255)
paper=np.median(od.reshape(-1,3),axis=0)
d=od-paper
# find colors: blue = pixels with B>>R ; purple = pixels with G lowest
blue=d[(a[...,2]>a[...,0]+50)&(a[...,0]<120)]
pur=d[(a[...,1]<a[...,0]-15)&(a[...,1]<a[...,2]-5)&(a[...,1]<110)]
print(len(blue),len(pur))
B=np.median(blue,axis=0);P=np.median(pur,axis=0);print(B,P)
M=np.stack([B,P,np.cross(B,P)],1); inv=np.linalg.inv(M)
c=d@inv.T
for i,n in enumerate(['blue','pur']):
    x=c[...,i]; x=np.clip(x/np.percentile(x,99.5),0,1)
    Image.fromarray((255*(1-x)).astype('uint8')).resize((1500,1710),Image.LANCZOS).save(f'crops/un_{n}.png')
