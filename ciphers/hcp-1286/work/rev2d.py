# violet-versus-black display: red channel as grey, postmark-black pixels (low blue) painted pale green
import sys
from PIL import Image
import numpy as np
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1286/work/hires/cpc_1914-01-10_HU__HU_Jasz-Arokszalas_jolanka-47_adr.jpg').convert('RGB')
def strip(name,x0,y0,x1,y1,s=4):
    r=im.crop((x0,y0,x1,y1)); W,H=r.width*s,r.height*s
    r=r.resize((W,H),Image.BICUBIC); a=np.asarray(r).astype(float)
    R,G,B=a[...,0],a[...,1],a[...,2]
    g=np.clip((R-90)/(215-90),0,1)**1.3
    out=np.stack([g,g,g],-1)
    bl=(B<92)&(G<105)
    out[bl]=[0.72,0.92,0.72]
    Image.fromarray(np.uint8(out*255)).save('rev2/%s.png'%name)
a=sys.argv[1:]
for i in range(0,len(a),6): strip(a[i],*map(int,a[i+1:i+6]))
