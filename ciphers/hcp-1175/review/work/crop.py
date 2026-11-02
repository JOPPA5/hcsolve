import sys
from PIL import Image, ImageOps
im=Image.open('../../work/hires/cpc_1915-10-25_HU_Mezokovesd_HU_Szomolya_szomolya-03_adr.jpg').convert('RGB')
def c(n,b,s=3,red=False):
    x=im.crop(b)
    if red: x=ImageOps.autocontrast(x.split()[0],cutoff=1)
    x.resize(((b[2]-b[0])*s,(b[3]-b[1])*s),Image.LANCZOS).save(n+'.png')
for i,(y0,y1) in enumerate([(340,480),(450,590),(565,700),(690,820),(820,950)],1):
    c(f'a{i}',(50,y0,780,y1),2)
    c(f'b{i}',(740,y0,1500,y1),2)
c('full',(40,330,1520,960),1)
