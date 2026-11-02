import sys
from PIL import Image, ImageOps
f='hires/cpc_1914-11-28_HU__HU_helyben-(locally)-Budapest_jolanka-57_adr.jpg'
im=Image.open(f).convert('RGB')
W,H=im.size
def c(n,b,s=1.0,rot=0):
    r=im.crop(b)
    if rot: r=r.rotate(rot,expand=True)
    r=r.resize((int(r.width*s),int(r.height*s)),Image.LANCZOS)
    g=ImageOps.autocontrast(r.convert('L'),cutoff=1)
    g.save('crops/'+n+'.png')
for i in range(6):
    y0=40+i*360
    c(f'L{i}',(60,y0,1720,y0+420),1.15)
c('stamp',(2650,120,3320,860),2)
c('addr',(1500,60,3400,2100),0.6)
c('corner',(1600,100,2300,400),2)
