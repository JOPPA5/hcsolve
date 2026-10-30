from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1914-01-10_HU__HU_Jasz-Arokszalas_jolanka-47_adr.jpg').convert('RGB')
def c(name,x0,y0,x1,y1,s=4.0):
    b=tuple(int(v*1.72) for v in (x0,y0,x1,y1))
    r=im.crop(b); r=r.resize((int(r.width*s),int(r.height*s)),Image.BICUBIC)
    ImageEnhance.Contrast(r).enhance(2.2).save('crops/%s.png'%name)
c('r9a',300,375,540,440); c('r9b',520,365,700,425,5)
c('r6a',285,240,535,300); c('r7a',40,300,300,350); c('r7b',280,285,540,345); c('r7c',540,275,830,325,3.6)
c('r8a',280,335,540,385)
