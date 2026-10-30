import sys
from PIL import Image
import numpy as np
im=Image.open(sys.argv[1]).convert('RGB')
O='review/work/crops/'
def c(n,x0,y0,x1,y1,s=4.0):
    r=im.crop((x0,y0,x1,y1)); r=r.resize((int(r.width*s),int(r.height*s)),Image.BICUBIC); r.save(O+n+'.png')
a=np.asarray(im).astype(float)
def f(n,x0,y0,x1,y1,s=4):
    r=a[y0:y1,x0:x1]; v=r[...,0]
    lo,hi=np.percentile(v,0.5),np.percentile(v,55)
    g=np.clip((v-lo)/(hi-lo),0,1)**1.4*255
    Image.fromarray(g.astype('uint8')).resize(((x1-x0)*s,(y1-y0)*s),Image.BICUBIC).save(O+n+'.png')
c('r14',560,1370,1300,1480,2.5)
c('r21a',640,1990,1100,2110,3)
f('s3',2760,380,3220,460,4)
f('s4',2760,440,3220,540,4); f('s6',2760,540,3220,640,4); f('s8',2760,690,3230,790,4)
c('c34',2760,370,3220,540,3.5); c('c67',2760,540,3220,800,3.5)
c('r7a',60,700,300,800,5); c('r19',640,1780,1000,1880,4); c('r2n',780,160,1000,280,5)
