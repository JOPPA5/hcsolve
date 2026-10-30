from PIL import Image, ImageOps, ImageFilter
im=Image.open('../../work/hires/pc_hcp_43_adr.JPG').convert('RGB').rotate(90,expand=True)
def c(n,b,z=6,rot=0):
    r=im.crop(b)
    if rot: r=r.rotate(rot,expand=True)
    r=r.resize((r.width*z,r.height*z),Image.BICUBIC); r=ImageOps.autocontrast(r,cutoff=.3); r.save(n+'.png')
c('z_blot',(560,1020,860,1150),4)
c('z_mjlf',(530,1120,860,1240),4)
c('z_uijt',(790,1120,1090,1240),4)
c('z_mjlf_gray',(530,1120,860,1240),4)
c('z_boe',(650,1220,860,1300),5)
c('z_ftu',(730,1020,870,1130),6)
c('z_year',(280,130,430,260),6,90)
