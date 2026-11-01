import numpy as np
from PIL import Image
im=Image.open('review/work/sheared.png').convert('RGB'); print(im.size)
a=np.asarray(im).astype(int); red=(a[...,0]-a[...,1]>70)&(a[...,0]>150)
h=red.sum(1)
# row bands
inb=False
for y,v in enumerate(h):
    if v>6 and not inb: s=y;inb=True
    if v<=6 and inb:
        inb=False
        if y-s>8:
            xs=np.where(red[s:y].any(0))[0]; print(s,y,xs.min(),xs.max())
