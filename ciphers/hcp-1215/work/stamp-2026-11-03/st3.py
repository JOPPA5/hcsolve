import sys
from PIL import Image, ImageOps
f,out=sys.argv[1],sys.argv[2]
im=Image.open(f).convert('RGB')
b=(2780,260,3180,680)
r=im.crop(b)
r=r.resize((r.width*3,r.height*3),Image.LANCZOS)
ImageOps.autocontrast(r,cutoff=0.5).save(out+'/box_col3x.png')
for i,ch in enumerate('rgb'):
    ImageOps.autocontrast(r.split()[i],cutoff=1).save(out+f'/box_{ch}3x.png')
# hue-difference: G - R and B - R
import numpy as np
a=np.asarray(r).astype(float)
d=a[:,:,1]-a[:,:,0]
d=(d-d.min())/(d.max()-d.min())*255
Image.fromarray(d.astype('uint8')).save(out+'/box_gminusr.png')
print(a[ :, :, :].reshape(-1,3).mean(0))
