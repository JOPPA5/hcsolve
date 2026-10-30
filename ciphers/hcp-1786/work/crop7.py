# Response-to-review crops: address lines, picture-side pencil note, hcp-1787 signature (read-only comparison).
from PIL import Image, ImageOps, ImageFilter
import numpy as np
s=1785/1024
A=Image.open('work/hires/pc_hcp_467_adr.JPG').convert('RGB')
P=Image.open('work/hires/pc_hcp_467_pic.JPG').convert('RGB')
print(A.size,P.size)
def c(im,box,z,n):
    r=im.crop([int(x*s) for x in box]); r.resize((r.width*z,r.height*z),Image.LANCZOS).save('work/crops2/'+n)
c(A,(540,275,1000,340),4,'addr_top.png')
c(A,(530,405,1000,455),4,'addr_street.png')
P.resize((P.width//1,P.height//1)).save('work/crops2/pic_full.png')
# pencil: local background subtraction on the green channel
g=np.asarray(P.split()[1]).astype(float)
bg=np.asarray(P.split()[1].filter(ImageFilter.GaussianBlur(9))).astype(float)
d=np.clip((g-bg)*-6+128,0,255).astype('uint8')
d=Image.fromarray(d).filter(ImageFilter.GaussianBlur(1.0))
b=[int(x*s) for x in (390,50,680,310)]
ImageOps.autocontrast(d.crop(b).resize(((b[2]-b[0])*2,(b[3]-b[1])*2),Image.LANCZOS),cutoff=1).save('work/crops2/pencil_hp.png')
