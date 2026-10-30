from PIL import Image, ImageFilter, ImageOps
import numpy as np
im=Image.open('hires/pc_hcp_1_adr.JPG').convert('RGB')
a=np.asarray(im).astype(float)
R,G,B=a[...,0],a[...,1],a[...,2]
# purple ink: blue is high relative to green and to red-paper tint
s=(B-G)+0.5*(R-G)*0  # blue-green
bg=np.asarray(Image.fromarray(np.uint8(np.clip(s+128,0,255))).filter(ImageFilter.GaussianBlur(25))).astype(float)-128
d=s-bg
d=np.clip(d/18,0,1)
out=Image.fromarray(np.uint8(255*(1-d)))
out.save('crops/ink.png')
for name,rot in (('ink90',90),('ink270',270)):
    x=out.crop((60,50,1000,1120)).rotate(rot,expand=True)
    x=x.resize((x.width*2,x.height*2),Image.LANCZOS); x.save(f'crops/{name}.png')
