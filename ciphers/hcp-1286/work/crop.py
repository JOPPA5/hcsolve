import sys
from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1914-01-10_HU__HU_Jasz-Arokszalas_jolanka-47_adr.jpg').convert('RGB')
def c(name,x0,y0,x1,y1,s=2.5):
    b=tuple(int(v*1.72) for v in (x0,y0,x1,y1))
    r=im.crop(b); r=r.resize((int(r.width*s),int(r.height*s)),Image.LANCZOS)
    r=ImageEnhance.Contrast(r).enhance(1.8)
    r.save('crops/%s.png'%name)
ys=[(40,230),(210,400),(380,570),(550,740),(720,910),(890,1080),(1060,1210)]
for i,(a,b) in enumerate(ys):
    c('L%d'%i,40,a,500,b); c('R%d'%i,470,a,960,b)
c('stamp',1590,110,1860,460,3)
