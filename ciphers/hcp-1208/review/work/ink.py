# reviewer's own separation: violet pencil vs black, plus enlarged crops
import sys
from PIL import Image, ImageEnhance
import numpy as np
im=Image.open('../../work/hires/cpc_1914-10-15_HU__HU_Budapest_jolanka-55_adr.jpg').convert('RGB')
a=np.asarray(im).astype(float)
d=a[:,:,2]-a[:,:,1]
v=np.clip((d-np.median(d)-6)/40,0,1)
ink=Image.fromarray((255*(1-v)).astype('uint8'))
def crop(name,x0,y0,x1,y1,W=2000):
    s=W/(x1-x0); sz=(W,int((y1-y0)*s))
    A=ink.crop((x0,y0,x1,y1)).resize(sz,Image.LANCZOS).convert('RGB')
    B=ImageEnhance.Contrast(ImageEnhance.Color(im.crop((x0,y0,x1,y1))).enhance(2.2)).enhance(1.3).resize(sz,Image.LANCZOS)
    o=Image.new('RGB',(W,sz[1]*2+6),'red');o.paste(B,(0,0));o.paste(A,(0,sz[1]+6));o.save('crops/%s.jpg'%name,quality=88)
for l in open(sys.argv[1]) if len(sys.argv)>1 else []:
    p=l.split()
    if p: crop(p[0],*map(int,p[1:5]))
if len(sys.argv)==1:
    im.resize((1700,1081)).save('crops/full.jpg',quality=85)
