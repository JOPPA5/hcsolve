import sys
from PIL import Image
im=Image.open('hires/cpc_1912-06-30_HU__HU_Jasz-Arokszalas_jolanka-26_adr.jpg')
s=1.72
# display coords
def c(n,x0,y0,x1,y1,z=2):
    r=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
    r=r.resize((r.width*z,r.height*z),Image.LANCZOS); r.save(f'crops/{n}.png')
ys=[(50,180),(165,300),(285,420),(405,530),(520,640),(625,740),(725,850),(835,960),(950,1080),(1060,1200)]
for i,(a,b) in enumerate(ys):
    c(f'b{i}L',40,a,540,b); c(f'b{i}R',500,a,1040,b)
c('stamp',1600,140,1860,420,3)
c('bottomR',860,1080,1880,1210,1)
