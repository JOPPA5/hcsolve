from PIL import Image, ImageFilter
import numpy as np
im=Image.open('work/hires/cpc_1912-03-13_HU__HU_Jasz-Arokszalas_jolanka-09_adr.jpg').convert('RGB')
def norm(c,lo=1,hi=99):
    l,h=np.percentile(c,lo),np.percentile(c,hi); return (np.clip((c-l)/(h-l),0,1)*255).astype('uint8')
def blur(c,s):
    l,h=c.min(),c.max()
    u=Image.fromarray(((c-l)/(h-l)*255).astype('uint8')).filter(ImageFilter.GaussianBlur(s))
    return np.asarray(u).astype('float32')/255*(h-l)+l
def go(name,box,S=5):
    x=im.crop(box); a=np.asarray(x).astype('float32'); r,g,b=a[...,0],a[...,1],a[...,2]
    out=[]
    c=(g+b)/2
    out.append(c)
    out.append(c-blur(c,8))          # high-pass fine
    out.append(c-blur(c,4))
    # PCA
    p=a.reshape(-1,3); p=p-p.mean(0); w,v=np.linalg.eigh(np.cov(p.T))
    for i in range(3):
        out.append((a-a.reshape(-1,3).mean(0))@v[:,i])
    out.append(g-b)
    H=[]
    for i,c in enumerate(out):
        Image.fromarray(norm(c)).resize((x.width*S,x.height*S),Image.BICUBIC).save(f'work/crops2/{name}_{i}.png')
    x.resize((x.width*S,x.height*S),Image.LANCZOS).save(f'work/crops2/{name}_c.png')
go('rt',(3000,205,3240,450),4)
go('r2',(2830,270,3240,350),4)
go('r3',(2830,335,3240,420),4)
