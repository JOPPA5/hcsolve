from PIL import Image, ImageEnhance
r=Image.open('review/work/rot_full.png').convert('RGB')
o=Image.open('work/hires/pc_hcp_65_adr.JPG').convert('RGB')
def c(n,src,b,z):
    a=src.crop(b); a=a.resize((a.width*z,a.height*z),Image.LANCZOS)
    ImageEnhance.Contrast(a).enhance(2).save(f'review/work/{n}.jpg',quality=90)
c('pm_date',o,(1385,250,1600,400),6)
c('n_compare',r,(155+200,890+540,155+420,890+640),6)
