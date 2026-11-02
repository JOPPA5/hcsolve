import sys
from PIL import Image
import numpy as np
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1286/work/hires/cpc_1914-01-10_HU__HU_Jasz-Arokszalas_jolanka-47_adr.jpg').convert('RGB')
A=np.asarray(im).astype(float)
def crop(name,x0,y0,x1,y1,s=3):
    a=A[y0:y1,x0:x1]
    R,G,B=a[...,0],a[...,1],a[...,2]
    v=B-G; 
    v=np.clip((v-(-6))/(30),0,1)
    black=(np.maximum(np.maximum(R,G),B)<105)&(abs(B-G)<14)
    out=np.uint8(255*(1-v))
    img=Image.fromarray(out).resize(((x1-x0)*s,(y1-y0)*s),Image.BICUBIC)
    rgb=np.stack([np.asarray(img)]*3,-1).copy()
    bm=np.asarray(Image.fromarray(np.uint8(black*255)).resize(img.size,Image.BILINEAR))>128
    rgb[bm,0]=np.maximum(rgb[bm,0],255); rgb[bm,1]=np.maximum(rgb[bm,1],215);rgb[bm,2]=np.maximum(rgb[bm,2],215)
    Image.fromarray(rgb).save('rev2/%s.png'%name)
a=sys.argv[1:]
crop(a[0],*map(int,a[1:5]),s=int(a[5]) if len(a)>5 else 3)
