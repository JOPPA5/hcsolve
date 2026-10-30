import sys
from PIL import Image
import numpy as np
im=Image.open(sys.argv[1]).convert('RGB'); a=np.asarray(im).astype(float)
def f(n,x0,y0,x1,y1,s=3):
    r=a[y0:y1,x0:x1]; v=r[...,1]-r[...,0]
    lo,hi=np.percentile(v,50),np.percentile(v,99.7)
    g=255-np.clip((v-lo)/(hi-lo),0,1)*255
    o=Image.fromarray(g.astype('uint8')); o=o.resize((int(o.width*s),int(o.height*s)),Image.LANCZOS); o.save('crops/%s.png'%n)
f('fB1',2350,1860,2950,2090); f('fB2',2850,1860,3300,2090,4)
f('fS1',2760,220,3200,500,4); f('fS2',2760,480,3200,780,4)
def c(n,x0,y0,x1,y1,s=5):
    r=im.crop((x0,y0,x1,y1)); r.resize((r.width*s,r.height*s),Image.LANCZOS).save('crops/%s.png'%n)
c('z_row2',420,150,1400,240,2); c('z_r7start',60,600,420,720); c('z_r7g',760,640,960,760)
c('z_r11',1050,960,1400,1060,4); c('z_r12',60,1090,960,1240,2); c('z_r16end',1100,1460,1620,1620,3);c('z_r19a',880,1800,1180,1960,4)
