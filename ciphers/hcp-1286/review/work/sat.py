import sys,glob
import numpy as np
from PIL import Image
im=Image.open(glob.glob('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1286/work/hires/*adr*')[0]).convert('RGB')
a=sys.argv[1:]
for i in range(0,len(a),6):
    n=a[i];x0,y0,x1,y1,s=map(int,a[i+1:i+6])
    A=np.asarray(im.crop((x0,y0,x1,y1))).astype(float)
    # violet score: blue relative to green; black ink low in all
    v=(A[...,2]-A[...,1]); v=(v-np.percentile(v,5))/(np.percentile(v,99.7)-np.percentile(v,5)); v=np.clip(v,0,1)
    r=Image.fromarray(np.uint8(255*(1-v))).resize(((x1-x0)*s,(y1-y0)*s),Image.BICUBIC); r.save('c/%s.png'%n)
