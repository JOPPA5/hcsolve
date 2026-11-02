import glob,sys
from PIL import Image
import numpy as np
f=glob.glob('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1172/work/hires/*adr.jpg')[0]
im=np.asarray(Image.open(f).convert('RGB')).astype(float)
def go(n,x0,y0,x1,y1,s):
    a=im[y0:y1,x0:x1]
    r,g,b=a[...,0],a[...,1],a[...,2]
    # violet-grey pencil keeps blue relative to red; brown ink and paper do not
    v=(b+1)/(r+1)
    lo,hi=np.percentile(v,5),np.percentile(v,99.7)
    o=255-np.clip((v-lo)/(hi-lo),0,1)*255
    I=Image.fromarray(o.astype('uint8')); I=I.resize((int(I.width*s),int(I.height*s)),Image.LANCZOS)
    I.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1172/work/crops/'+n+'.png')
go('i3a',60,430,950,560,2.1);go('i3b',900,430,1760,560,2.1);go('i4',60,540,950,690,2.1);go('i9',150,1880,560,2040,4);go('i2',60,300,1760,450,1.1)
