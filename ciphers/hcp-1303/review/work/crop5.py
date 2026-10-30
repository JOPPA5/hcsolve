from PIL import Image, ImageOps
import numpy as np
im=Image.open('../../work/hires/cpc_--13_HU__HU_Jasz-Arokszalas_jolanka-84_adr.jpg').convert('RGB')
s=1.72
def c(n,x0,y0,x1,y1,z=4):
    r=im.crop([int(v*s) for v in (x0,y0,x1,y1)]);r=r.resize((r.width*z,r.height*z),Image.LANCZOS)
    a=np.asarray(r).astype(float)
    # suppress brown watermark: use blue channel-boost (brown has low blue; pencil neutral): take R (brown is bright in R relative to pencil)
    g=a[:,:,0]
    g=(g-g.min())/(g.max()-g.min())*255
    ImageOps.autocontrast(Image.fromarray(g.astype('uint8')),cutoff=1).save('crops/%s.png'%n)
c('name',1150,1115,1560,1170,4)
c('name2',1460,1110,1760,1170,4)
c('szak',1380,1160,1740,1215,4)
