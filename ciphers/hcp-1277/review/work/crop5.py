from PIL import Image, ImageEnhance
im=Image.open('work/hires/cpc_1914-03-01_HU__HU_Jasz-Arokszalas_jolanka-48_adr.jpg').convert('RGB')
def c(n,b,s=4):
    x=im.crop(b); x=x.resize((x.width*s,x.height*s),Image.LANCZOS); ImageEnhance.Contrast(x).enhance(1.4).save(f'review/work/{n}.png')
c('z28',(1640,1940,1900,2020),4)
c('z24',(60,1690,330,1830),4)
