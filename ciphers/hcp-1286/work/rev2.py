import sys
from PIL import Image, ImageEnhance, ImageOps
import numpy as np
P='/Users/tomaspavuk/.cache'
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1286/work/hires/cpc_1914-01-10_HU__HU_Jasz-Arokszalas_jolanka-47_adr.jpg').convert('RGB')
A=np.asarray(im).astype(float)
def crop(name,x0,y0,x1,y1,s=3,mode='rgb'):
    a=A[y0:y1,x0:x1]
    R,G,B=a[...,0],a[...,1],a[...,2]
    if mode=='rgb':
        out=Image.fromarray(a.astype('uint8'));out=ImageEnhance.Contrast(out).enhance(2.0)
    else:
        if mode=='violet':  # violet ink index: B minus R, suppresses grey-black and paper
            v=(B-R)
        elif mode=='R': v=-R
        elif mode=='G': v=-G
        lo,hi=np.percentile(v,2),np.percentile(v,99.7)
        v=np.clip((v-lo)/(hi-lo),0,1)
        out=Image.fromarray((255*(1-v)).astype('uint8'))
    out=out.resize((out.width*s,out.height*s),Image.LANCZOS)
    out.save('rev2/%s.png'%name)
if __name__=='__main__':
    a=sys.argv[1:]
    crop(a[0],*map(int,a[1:5]),s=int(a[5]) if len(a)>5 else 3,mode=a[6] if len(a)>6 else 'rgb')
