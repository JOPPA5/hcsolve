from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1914-01-10_HU__HU_Jasz-Arokszalas_jolanka-47_adr.jpg').convert('RGB')
def c(name,x0,y0,x1,y1,s=3.6):
    b=tuple(int(v*1.72) for v in (x0,y0,x1,y1))
    r=im.crop(b); r=r.resize((int(r.width*s),int(r.height*s)),Image.BICUBIC)
    ImageEnhance.Contrast(r).enhance(1.6).save('crops/%s.png'%name)
c('z1',40,195,330,340); c('z2',300,195,590,340); c('z3',560,190,850,335)
c('z4',40,330,330,475); c('z5',300,330,590,475); c('z6',560,330,850,475)
c('z0',380,140,700,210)
