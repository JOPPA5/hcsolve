from PIL import Image, ImageOps
import numpy as np
im=Image.open('../../work/hires/pc_hcp_43_adr.JPG').convert('RGB').rotate(90,expand=True)
def c(n,b,z=6,rot=0):
    r=im.crop(b)
    if rot: r=r.rotate(rot,expand=True)
    r=r.resize((r.width*z,r.height*z),Image.BICUBIC); r=ImageOps.autocontrast(r,cutoff=.3); r.save(n+'.png')
# whole postmark upright (text is inverted in the card-reading orientation)
c('z_pm',(80,70,460,430),3,180)
c('z_M1',(535,1130,650,1200),10)
c('z_M2',(330,1195,500,1320),5)
c('z_N',(330,1020,460,1120),5)
c('z_G',(330,1500,520,1620),5)
