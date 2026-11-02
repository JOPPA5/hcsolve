import sys,glob
from PIL import Image
import numpy as np
im=Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')
S=3468/1600
def go(n,x0,y0,x1,y1,z=3):
    c=im.crop((int(x0*S),int(y0*S),int(x1*S),int(y1*S)))
    a=np.asarray(c).astype(float)
    d=a[...,2]-a[...,0]   # blue ink: B>R; gray print ~0; paper B<R
    d=(d-d.min())/(np.percentile(d,99.7)-d.min()); d=np.clip(d,0,1)
    o=Image.fromarray((255*(1-d)).astype('uint8'))
    o=o.resize((o.width*z,o.height*z),Image.LANCZOS); o.save(f'crops/{n}.png')
    c.resize((c.width*z,c.height*z),Image.LANCZOS).save(f'crops/{n}_c.png')
for a in sys.argv[1:]:
    n,*v=a.split(','); go(n,*map(int,v))
