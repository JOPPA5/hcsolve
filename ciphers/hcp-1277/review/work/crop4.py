from PIL import Image, ImageEnhance
im=Image.open('work/hires/cpc_1914-03-01_HU__HU_Jasz-Arokszalas_jolanka-48_adr.jpg').convert('RGB')
def c(n,b,s=4):
    x=im.crop(b); x=x.resize((x.width*s,x.height*s),Image.LANCZOS); ImageEnhance.Contrast(x).enhance(1.4).save(f'review/work/{n}.png')
c('z10',(900,640,1300,760),4)
c('z12',(1250,790,1570,890),4)
c('z25',(430,1740,860,1830),4)
c('z25b',(640,1745,770,1825),8)
c('z13',(790,850,1200,950),4)
c('z21',(790,1560,1250,1660),3)
c('z25tail',(860,1740,1570,1830),2)
