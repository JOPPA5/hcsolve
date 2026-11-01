import sys
from PIL import Image, ImageEnhance
f='../../work/hires/cpc_1915--_HU_Mezokovesd_HU_Szomolya_szomolya-43_adr.jpg'
im=Image.open(f).convert('RGB'); s=im.size[0]/1024
def c(n,x0,y0,x1,y1,z=5,src=im):
    r=src.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
    r=r.resize((r.width*z,r.height*z),Image.LANCZOS); r=ImageEnhance.Contrast(r).enhance(1.6); r.save(n+'.png'); print(n,r.size)
c('d1',120,562,245,600,5)
c('d2',235,562,360,600,5)
c('d3',350,562,495,600,5)
c('note1',110,592,370,622,4)
c('note2',360,592,620,622,4)
c('sig',600,580,960,622,3)
sis=__import__('glob').glob('../../../hcp-1174/work/hires/*adr*')[0]
print(sis)
