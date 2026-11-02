import sys
from PIL import Image, ImageOps, ImageEnhance
im=Image.open('hires/cpc_1914--_HU__HU_Jasz-Arokszalas_jolanka-118_adr.jpg').convert('RGB')
def c(name,box,s=2,rot=0,gray=True):
    x=im.crop(box)
    if rot: x=x.rotate(rot,expand=True)
    if gray:
        x=ImageOps.autocontrast(x.split()[1],cutoff=1)
    x=x.resize((x.width*s,x.height*s),Image.LANCZOS)
    x.save('crops/%s.png'%name)
a=sys.argv
c(a[1],tuple(map(int,a[2:6])),int(a[6]) if len(a)>6 else 2,int(a[7]) if len(a)>7 else 0)
