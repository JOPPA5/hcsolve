import glob
import numpy as np
from PIL import Image,ImageOps,ImageFilter
f=glob.glob('hires/*adr.jpg')[0]
im=Image.open(f).convert('RGB').crop((2780,240,3160,640)).filter(ImageFilter.GaussianBlur(1.2))
a=np.asarray(im).astype(float)
r,g,b=a[...,0],a[...,1],a[...,2]
# green excess vs paper hue (paper r>g>b). gray pencil: r~g~b
ge=np.clip(g-r+12,0,None)   # green-ness
dark=255-g
sc=dark-3.0*ge
sc=np.clip(sc,0,None)
o=Image.fromarray((255-np.clip(sc*2.2,0,255)).astype('uint8'))
o=ImageOps.autocontrast(o,cutoff=0.5).resize((1140,1200),Image.LANCZOS);o.save('crops/pencil.png')
