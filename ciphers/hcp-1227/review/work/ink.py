import sys
from PIL import Image, ImageOps
import numpy as np
f='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1227/work/hires/cpc_-09-26_HU__HU_Jasz-Arokszalas_jolanka-95_adr.jpg'
x0,y0,x1,y1=2780,330,3220,620
a=np.asarray(Image.open(f).convert('RGB').crop((x0,y0,x1,y1))).astype(float)
r,g,b=a[...,0],a[...,1],a[...,2]
sc=4
def sv(arr,n):
    arr=np.clip(arr,np.percentile(arr,1),np.percentile(arr,99))
    arr=(arr-arr.min())/(arr.max()-arr.min())*255
    Image.fromarray(arr.astype('uint8')).resize(((x1-x0)*sc,(y1-y0)*sc),Image.LANCZOS).save('review/work/'+n)
sv(r,'st_r.png'); sv(g-r,'st_gr.png'); sv(b-r,'st_br.png')
