from PIL import Image, ImageFilter
import numpy as np
exec(open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1313/work/enh.py').read().split("m=blur")[0])
r,gg,b=im.split()
gb=np.asarray(gg.filter(ImageFilter.GaussianBlur(2.2))).astype(float)
bb=np.asarray(b.filter(ImageFilter.GaussianBlur(2.2))).astype(float)
a=gb-0.75*bb
m=blur(a,22); d=a-m; s=np.sqrt(blur(d*d,40))+2
n=d/s
Image.fromarray(np.clip(175+n*62,0,255).astype('uint8')).save(W+'crops/enh2_full.png')
