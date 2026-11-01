import glob
from PIL import Image, ImageEnhance
def c(n,src,x0,y0,x1,y1,z):
    im=Image.open(src).convert('RGB'); s=im.size[0]/1024
    r=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
    r=r.resize((r.width*z,r.height*z),Image.LANCZOS); ImageEnhance.Contrast(r).enhance(1.5).save(n+'.png')
a=glob.glob('../../../hcp-1174/work/hires/*adr*')[0]
c('c74',a,20,588,150,622,7)
b=glob.glob('../../../hcp-1179/work/hires/*adr*')[0]
c('r79a',b,15,545,500,605,3)
c('r79b',b,480,545,960,605,3)
me='../../work/hires/cpc_1915--_HU_Mezokovesd_HU_Szomolya_szomolya-43_adr.jpg'
c('sigz',me,700,580,960,622,4)
c('addr2',me,470,240,960,620,1)
