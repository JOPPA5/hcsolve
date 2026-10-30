import sys
from PIL import Image
import numpy as np
a=np.asarray(Image.open(sys.argv[1]).convert('RGB')).astype(float)
def f(n,x0,y0,x1,y1,s=5):
    r=a[y0:y1,x0:x1]; v=r[...,0]   # red channel: green ink and teal print dark; keep darkest
    lo,hi=np.percentile(v,1),np.percentile(v,60)
    g=np.clip((v-lo)/(hi-lo),0,1)**1.6*255
    o=Image.fromarray(g.astype('uint8')).resize(((x1-x0)*s,(y1-y0)*s),Image.BICUBIC); o.save('crops/%s.png'%n)
f('t1',2770,540,3230,640,4); f('t2',2770,430,3230,540,4); f('t3',2770,690,3230,790,4)
