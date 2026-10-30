from PIL import Image, ImageOps
import sys
im=Image.open('hires/cpc_1912-06-11_HU__HU_Jasz-Arokszalas_jolanka-25_adr.jpg').convert('RGB')
W,H=im.size; s=W/1024
def c(n,b,z=1.0,rot=0):
    x=im.crop(tuple(int(v*s) for v in b))
    if rot: x=x.rotate(rot,expand=True)
    x=x.resize((int(x.width*z),int(x.height*z)),Image.LANCZOS); x.save('crops/'+n+'.png')
c('a',(20,20,460,170),1.1); c('b',(20,160,460,310),1.1); c('c',(20,300,460,450),1.1); c('d',(20,440,460,610),1.1)
c('e',(420,560,970,612),0.9)
c('f',(400,60,470,550),1.1,-90)
c('g',(790,60,920,200),3)
c('h',(470,170,800,230),1.5)
c('i',(470,240,970,500),1)
