# strip viewer: rgb on top, B-R below, for one hires box
import sys
from PIL import Image, ImageEnhance
import numpy as np
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1286/work/hires/cpc_1914-01-10_HU__HU_Jasz-Arokszalas_jolanka-47_adr.jpg').convert('RGB')
A=np.asarray(im).astype(float)
def strip(name,x0,y0,x1,y1,s=3):
    a=A[y0:y1,x0:x1]
    top=Image.fromarray(a.astype('uint8'));top=ImageEnhance.Contrast(top).enhance(2.2)
    v=a[...,2]-a[...,0]; lo,hi=np.percentile(v,3),np.percentile(v,99.8); v=np.clip((v-lo)/(hi-lo),0,1)
    bot=Image.fromarray(np.uint8(255*(1-v))).convert('RGB')
    W,H=top.width*s,top.height*s
    o=Image.new('RGB',(W,2*H+6),(255,0,0))
    o.paste(top.resize((W,H),Image.LANCZOS),(0,0)); o.paste(bot.resize((W,H),Image.LANCZOS),(0,H+6))
    o.save('rev2/%s.png'%name)
a=sys.argv[1:]
for i in range(0,len(a),6):
    strip(a[i],*map(int,a[i+1:i+6]))
