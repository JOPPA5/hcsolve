from PIL import Image, ImageFilter
import numpy as np
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1313/work/'
im=Image.open(W+'hires/cpc_1912-04-07_HU__HU_Jasz-Arokszalas_jolanka-15_adr.jpg').convert('RGB').crop((50,640,1150,1200))
a=np.asarray(im.filter(ImageFilter.GaussianBlur(2.2))).astype(float)+1
l=-np.log(a/255)
X=l.reshape(-1,3);m=X.mean(0);u,s,vt=np.linalg.svd((X-m)[::7],full_matrices=False)
def bl(x,r):
    k=np.exp(-np.arange(-3*r,3*r+1)**2/(2*r*r));k/=k.sum()
    x=np.apply_along_axis(lambda v:np.convolve(np.pad(v,3*r,mode='edge'),k,'valid'),0,x)
    x=np.apply_along_axis(lambda v:np.convolve(np.pad(v,3*r,mode='edge'),k,'valid'),1,x)
    return x
for i in range(2):
    p=((X-m)@vt[i]).reshape(l.shape[:2])
    d=p-bl(p,20)
    lo,hi=np.percentile(d,[1,99.5])
    if abs(lo)>abs(hi): d=-d;lo,hi=-hi,-lo
    o=np.clip((d-lo)/(hi-lo),0,1)
    Image.fromarray(((1-o)*255).astype('uint8')).resize((1650,840),Image.LANCZOS).save(W+f'rev2/pca{i}.png')
