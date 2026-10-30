from PIL import Image, ImageOps, ImageFilter
import sys
im=Image.open('../../work/hires/pc_hcp_43_adr.JPG').convert('RGB').rotate(90,expand=True)
print(im.size)
def c(n,b,z=4):
    r=im.crop(b); r=r.resize((r.width*z,r.height*z),Image.LANCZOS); r=ImageOps.autocontrast(r,cutoff=.3); r.save(n+'.png')
c('r_l1a',(330,1010,720,1160),3)
c('r_l1b',(700,1010,1090,1160),3)
c('r_l2a',(330,1110,720,1260),3)
c('r_l2b',(700,1110,1090,1260),3)
c('r_l3a',(330,1190,720,1350),3)
c('r_l3b',(700,1190,1090,1350),3)
c('r_l4a',(330,1290,720,1450),3)
c('r_l4b',(700,1290,1090,1450),3)
c('r_l5',(330,1420,1050,1640),2)
c('r_stamp',(80,150,420,420),3)
