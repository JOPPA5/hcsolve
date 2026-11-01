import glob
from PIL import Image, ImageEnhance
import numpy as np
f='../../work/hires/cpc_1915--_HU_Mezokovesd_HU_Szomolya_szomolya-43_adr.jpg'
im=Image.open(f).convert('RGB'); s=im.size[0]/1024
def c(n,x0,y0,x1,y1,z=3,src=im,sc=None):
    sc=sc or s
    r=src.crop((int(x0*sc),int(y0*sc),int(x1*sc),int(y1*sc)))
    r=r.resize((r.width*z,r.height*z),Image.LANCZOS)
    a=np.asarray(r).astype(float)
    # suppress brown: use blue channel, stretch
    b=a[...,2]; lo,hi=np.percentile(b,1),np.percentile(b,99)
    Image.fromarray(np.clip((b-lo)/(hi-lo)*255,0,255).astype('uint8')).save(n+'_b.png')
    ImageEnhance.Contrast(r).enhance(1.6).save(n+'.png')
c('anyu',240,85,500,145,4)
c('fuj',30,430,260,470,4)
c('fuj2',240,415,500,465,4)
c('vers',20,265,480,325,2)
c('top1',495,12,730,48,4)
c('top2',720,12,955,48,4)
sf=glob.glob('../../../hcp-1174/work/hires/*adr*')[0]
sim=Image.open(sf).convert('RGB'); s2=sim.size[0]/1024
c('foot74',20,590,240,622,6,sim,s2)
c('foot74b',120,590,260,622,8,sim,s2)
c('llek74',330,560,460,600,6,sim,s2)
c('head74',20,10,300,50,3,sim,s2)
