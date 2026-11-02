import glob
from PIL import Image, ImageOps
import numpy as np
im=np.asarray(Image.open(glob.glob('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1172/work/hires/*adr.jpg')[0]).convert('RGB')).astype(float)
for n,b in {'g3a':(780,440,1290,560),'g3b':(1270,440,1760,560),'g4a':(60,560,520,690),'g4b':(500,560,960,690)}.items():
    x0,y0,x1,y1=b; a=im[y0:y1,x0:x1]
    # blue channel gamma: shows pencil vs brown wash
    v=a[...,2]; lo,hi=np.percentile(v,1),np.percentile(v,60)
    o=np.clip((v-lo)/(hi-lo),0,1)**1.6*255
    I=Image.fromarray(o.astype('uint8')); I.resize((I.width*4,I.height*4),Image.BICUBIC).save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1172/work/crops/'+n+'.png')
