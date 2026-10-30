import sys
from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-77_adr.jpg').convert('RGB')
def c(n,box,s=2.5,rot=0):
    x=im.crop(box)
    if rot: x=x.rotate(rot,expand=True)
    x=x.resize((int(x.width*s),int(x.height*s)),Image.LANCZOS)
    x=ImageEnhance.Contrast(x).enhance(1.6)
    x.save(f'crops/{n}.png')
# rows bands
ys=[(60,330),(310,580),(560,830),(810,1080),(1060,1330),(1310,1580),(1560,1830),(1810,2100)]
for i,(a,b) in enumerate(ys):
    c(f'b{i}L',(70,a,850,b)); c(f'b{i}R',(800,a,1600,b))
