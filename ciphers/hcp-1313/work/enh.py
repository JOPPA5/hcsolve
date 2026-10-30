from PIL import Image, ImageFilter
import numpy as np
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1313/work/'
im=Image.open(W+'hires/cpc_1912-04-07_HU__HU_Jasz-Arokszalas_jolanka-15_adr.jpg').convert('RGB')
g=im.split()[1].filter(ImageFilter.GaussianBlur(1.6))
a=np.asarray(g).astype(float)
def blur(x,r):
    for _ in range(3):
        for ax in (0,1):
            c=np.cumsum(np.pad(x,[(r+1,r) if i==ax else (0,0) for i in (0,1)],mode='edge'),axis=ax)
            x=(np.take(c,range(2*r+1,c.shape[ax]),axis=ax)-np.take(c,range(0,c.shape[ax]-2*r-1),axis=ax))/(2*r+1)
    return x
m=blur(a,24); d=a-m; s=np.sqrt(blur(d*d,40))+2.5
n=d/s
out=np.clip(170+n*55,0,255).astype('uint8')
Image.fromarray(out).save(W+'crops/enh_full.png')
