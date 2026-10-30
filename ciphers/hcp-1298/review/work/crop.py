import sys
from PIL import Image, ImageEnhance
im=Image.open('../../work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-77_adr.jpg').convert('RGB')
print(im.size)
def c(n,box,s=2.0,rot=0,con=1.7):
    x=im.crop(box)
    if rot: x=x.rotate(rot,expand=True)
    x=x.resize((int(x.width*s),int(x.height*s)),Image.LANCZOS)
    ImageEnhance.Contrast(x).enhance(con).save(n+'.png')
c('all',(0,0,im.width,im.height),0.55,0,1.3)
for i,(a,b) in enumerate([(50,300),(280,530),(510,760),(740,990),(970,1220),(1200,1450),(1430,1680),(1660,1910),(1880,2150)]):
    c(f'L{i}',(40,a,860,b),2.4); c(f'R{i}',(800,a,1640,b),2.4)
