import glob
from PIL import Image, ImageEnhance
import numpy as np
f='../../work/hires/cpc_1915--_HU_Mezokovesd_HU_Szomolya_szomolya-43_adr.jpg'
im=Image.open(f).convert('RGB'); s=im.size[0]/1024
def c(n,x0,y0,x1,y1,z=3,src=im):
    r=src.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
    r=r.resize((r.width*z,r.height*z),Image.LANCZOS)
    a=np.asarray(r).astype(float)
    o=np.clip(255-(a[...,2]-a[...,0]+25)*4,0,255).astype('uint8')
    Image.fromarray(o).save(n+'_sep.png')
    ImageEnhance.Contrast(r).enhance(1.6).save(n+'.png')
c('mark',232,572,300,612,8)
c('ang',20,75,500,145,2)
c('fuv',20,405,500,470,2)
c('rest',20,470,500,610,1)
c('top',495,8,955,48,2)
c('verse2',20,335,500,410,2)
sf=glob.glob('../../../hcp-1174/work/hires/*adr*')[0]
sim=Image.open(sf).convert('RGB'); s2=sim.size[0]/1024
s=s2
c('s74foot',20,540,470,620,2,sim)
c('s74r',440,540,960,620,2,sim)
