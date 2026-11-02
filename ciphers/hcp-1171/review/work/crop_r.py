from PIL import Image, ImageOps
import sys
f='../../work/hires/cpc_1915-11-22_HU_Mezokovesd_HU_Szomolya_szomolya-06_adr.jpg'
im=Image.open(f).convert('RGB')
S=2.477
def c(name,x0,y0,x1,y1,z=2,red=True):
    b=(int(x0*S),int(y0*S),int(x1*S),int(y1*S))
    p=im.crop(b)
    if red:
        p=ImageOps.autocontrast(p.split()[0],cutoff=1)
    p=p.resize((p.width*z,p.height*z),Image.LANCZOS)
    p.save(name+'.png')
    print(name,p.size)
c('top',80,20,620,75,z=2,red=False)
c('sig',30,825,540,865,z=2,red=False)
c('l1',30,60,700,185,z=1)
c('l2',30,180,700,310,z=1)
c('l3',30,300,700,430,z=1)
c('l4',30,420,700,560,z=1)
c('l5',30,570,700,740,z=1)
c('l6',30,745,700,865,z=1)
c('addr',700,130,1320,860,z=1,red=False)
